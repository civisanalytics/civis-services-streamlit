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

    df["is_test_relation"] = df["unique_id"].str.startswith("test.")
    return df


# Streamlit UI
st.title("Civis dbt Pipeline Dashboard")

# Input fields for job_id and an optional run_id
job_id = st.text_input("Job ID", "")
run_id = st.text_input("Run ID (optional)", "")
# Add checkbox to the UI for filtering
filter_test_relations = st.checkbox("Filter out testing tasks")

# Button to fetch data and display Gantt chart
if st.button("Display Pipeline Information"):
    if job_id:
        df = fetch_data(job_id, run_id if run_id else None)
        # breakpoint()

        if filter_test_relations:
            df = df[~df.is_test_relation]

        # Display the metrics on the app
        st.text(f"Total Tasks Executed: {df.shape[0]}")
        st.text(f"Total Task Time: {df.execution_time.sum() / 60} minutes")
        st.text(f"Average Task Time: {df.execution_time.mean():.2f} seconds")

        # Check if the DataFrame is not empty
        if not df.empty:
            fig = px.timeline(
                df,
                x_start="started_at",
                x_end="completed_at",
                y="unique_id",
                color="status",
                hover_data=[
                    "unique_id",
                    "status",
                    "started_at",
                    "completed_at",
                    "execution_time",
                ],
                # execution_time="execution_time",
            )
            fig.update_yaxes(autorange="reversed")
            st.plotly_chart(fig, theme="streamlit")
        else:
            st.error(
                "No data available to display. Please check your Job ID and Run ID."
            )
    else:
        st.error("Please enter a valid Job ID.")
