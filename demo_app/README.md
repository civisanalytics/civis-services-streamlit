## Python dependency management

We strongly recommend pinning the exact package versions
(i.e., using double-equals `==`) in `requirements.txt`.

For stability in production, especially if you have more complicated requirements,
we recommend pinning the exact versions of both the dependencies
your code imports and their transitive dependencies.
For this purpose, we recommend [pip-tools](https://pip-tools.readthedocs.io/en/latest/)
to generate `requirements.txt`.

## Running the demo app locally

```shell
pip install -r requirements.txt
streamlit run app.py
```
