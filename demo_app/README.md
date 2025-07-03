## Python dependency management

We strongly recommend pinning the exact package versions
(i.e., using double-equals `==`) in `requirements.txt`.

For stability in production, we recommend locking down the execution environment by
pinning the exact versions of both the dependencies
your code imports and their transitive dependencies.
Tools for generating a "full" `requirements.txt` include
[uv](https://docs.astral.sh/uv/) and 
[pip-tools](https://pip-tools.readthedocs.io/en/latest/).

## Running the demo app locally

```shell
pip install -r requirements.txt
streamlit run app.py
```
