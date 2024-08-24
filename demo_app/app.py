"""Demo app for civis-services-streamlit."""

import streamlit as st
import civis
import plotly.express as px

import pandas as pd


# Function to fetch data from Civis Platform using Civis Python client
def fetch_data(job_id, run_id=None):
    # Initialize Civis client
    client = civis.APIClient()

    # This is a placeholder for the actual logic to fetch run outputs
    # The structure and exact method to retrieve outputs will depend on your Civis setup
    # You might need client.scripts.get_containers_runs_outputs or a similar method
    if run_id is not None:
        outputs = client.jobs.list_runs_outputs(job_id, run_id)
    else:
        latest_run = client.jobs.list_runs(job_id, limit=1)[0]
        outputs = client.jobs.list_runs_outputs(job_id, latest_run.id)

    # Fetch the file_id for the run_results object
    oid = [obj["object_id"] for obj in outputs if obj["name"] == "run_results.json"][0]
    run_results = civis.io.file_to_json(oid)

    # Convert the results into a dataframe
    df = pd.DataFrame(run_results["results"])
    df_timing = pd.DataFrame(
        [
            (t["started_at"], t["completed_at"])
            for res in run_results["results"]
            for t in res["timing"]
            if t["name"] == "execute"
        ],
        columns=["started_at", "completed_at"],
    )
    df_timing = df_timing.apply(pd.to_datetime)

    # append timing columns to dataframe
    df = pd.concat([df, df_timing], axis=1)

    df["model_type"] = df["unique_id"].str.split(".").str[0]
    df["dbt_model"] = df["unique_id"].str.split(".").str[-1]
    return df


# Streamlit UI
st.set_page_config(page_title="Civis dbt Pipeline Dashboard", layout="wide")
st.title("Civis dbt Pipeline Dashboard")

# Input fields for job_id and an optional run_id
job_id = st.text_input("Job ID", "")
run_id = st.text_input("Run ID (optional)", "")
# Add checkbox to the UI for filtering
filter_test_relations = st.checkbox("Filter out testing tasks", True)

# Button to fetch data and display Gantt chart
if st.button("Display Pipeline Information"):
    if job_id:
        df = fetch_data(job_id, run_id if run_id else None)

        if filter_test_relations:
            df = df[df.model_type != "test"]

        # Display some metrics
        col1, col2, col3 = st.columns(3)

        col1.metric("# Tasks Executed", df.shape[0])
        col2.metric(
            "Total Task Duration (minutes)", (df.execution_time.sum() / 60).round(2)
        )
        col3.metric("Avg Task Duration (seconds)", df.execution_time.mean().round(2))

        # Check if the DataFrame is not empty
        if not df.empty:
            # add gantt chart
            fig = px.timeline(
                df,
                x_start="started_at",
                x_end="completed_at",
                y="dbt_model",
                color="status",
                hover_data=[
                    "unique_id",
                    "status",
                    "started_at",
                    "completed_at",
                    "execution_time",
                ],
                labels={"dbt_model": "Task", "status": "Status"},
                title="Execution Timeline",
            )
            # This makes sure that the y-axis is from first to last task
            fig.update_yaxes(autorange="reversed")
            st.plotly_chart(fig, theme="streamlit")

            # Add a table to display the top 10 longest running tasks
            cols_to_display = [
                "unique_id",
                "status",
                "execution_time",
                "started_at",
                "completed_at",
            ]
            st.header("Top 10 Longest Running Tasks", divider=True)
            st.dataframe(
                df[cols_to_display]
                .sort_values("execution_time", ascending=False)
                .head(10),
                column_config={
                    "unique_id": "Task ID",
                    "status": "Status",
                    "execution_time": "Execution Time (seconds)",
                    "started_at": "Start",
                    "completed_at": "Finish",
                },
                hide_index=True,
            )
        else:
            st.error(
                "No data available to display. Please check your Job ID and Run ID."
            )
    else:
        st.error("Please enter a valid Job ID.")
