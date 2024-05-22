"""Demo app for civis-services-streamlit."""

import os

import civis
import streamlit as st
import pandas as pd
from sklearn import datasets


@st.cache_data
def load_data():
    iris = datasets.load_iris()
    data = pd.DataFrame(iris.data, columns=iris.feature_names)
    data["label"] = [iris.target_names[i] for i in iris.target]
    return data


def get_civis_platform_username():
    """Get the username of the current Civis Platform user."""
    # The Civis API key is available as an environment variable on Civis Platform.
    # The check for `if os.getenv("CIVIS_API_KEY"):` below allows us to
    # test run this app locally when a key isn't available.
    if os.getenv("CIVIS_API_KEY"):
        civis_client = civis.APIClient()
        return civis_client.username


def main():
    data = load_data()

    # You can interact with the Civis API using the "civis" Python package:
    # https://civis-python.readthedocs.io/
    # Here, we demo a simple example of getting the username of the current user.
    username = get_civis_platform_username()

    st.write(
        "This is a demo Streamlit app "
        f"currently run by Civis Platform user '{username}'."
    )

    st.write(
        "To create your own app, "
        "fork the [civis-services-streamlit GitHub repository](https://github.com/civisanalytics/civis-services-streamlit) "  # noqa: E501
        "and follow the instructions."
    )

    st.title("The Iris Dataset")
    st.write(data)

    st.subheader("Sepal Length vs. Sepal Width")
    st.scatter_chart(data, x="sepal length (cm)", y="sepal width (cm)", color="label")

    st.subheader("Petal Length vs. Petal Width")
    st.scatter_chart(data, x="petal length (cm)", y="petal width (cm)", color="label")


if __name__ == "__main__":
    main()
