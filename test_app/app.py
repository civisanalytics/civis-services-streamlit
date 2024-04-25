"""Test app for checking that the built Docker image works.

This test app is not meant to test or show any Civis API or other Streamlit features.
"""

import streamlit as st
import pandas as pd


def main():
    st.write("Showing a table from a dataframe:")
    st.write(pd.DataFrame({"column1": [1, 2, 3], "column2": [10, 20, 30]}))


if __name__ == "__main__":
    main()
