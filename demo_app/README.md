For Python dependency management,
we strongly recommend pinning in `requirements.txt` the exact package versions
(i.e., using double-equals `==`) of both the dependencies
your code imports and their transitive dependencies for stability.
For this purpose, we recommend [pip-tools](https://pip-tools.readthedocs.io/en/latest/):

* A requirements file, such as `requirements-core.txt` as shown, specifies
  only the dependencies that are actually imported by your app's code.
  This file is meant to be manually edited as necessary.
  (Alternatively, if you have a Python package defined by `pyproject.toml`,
  your core requirements can be pinned in `pyproject.toml` instead.)
* Use `pip-tools` (install it with `pip install pip-tools`)
  to generate `requirements.txt` as shown.
  `requirements.txt` is _not_ meant to be manually edited,
  and pins the exact versions for the dependencies specified in `requirements-core.txt`
  as well as their transitive dependencies.

To test run this demo app locally:

```shell
pip install -r requirements.txt
streamlit run app.py
```
