For Python dependency management,
we strongly recommend pinning in `requirements.txt` the exact package versions of both the dependencies
your code imports and their (sub-)dependencies for stability.
While there exist multiple frameworks for locking down Python dependencies,
we recommend [pip-tools](https://pip-tools.readthedocs.io/en/latest/):

* A requirements file, such as `requirements-core.txt` as shown, specifies
  only the dependencies that are actually imported by your app's code.
  This file is meant to be manually edited as necessary.
  (Alternatively, if you have a Python package defined by `pyproject.toml`,
  your core requirements can be pinned in `pyproject.toml` instead.)
* Use `pip-tools` (install it `pip install pip-tools`)
  to generate `requirements.txt` as shown.
  `requirements.txt` is _not_ meant to be manually edited,
  and pins the exact versions for the dependencies specified in `requirements-core.txt`
  as well as their sub-dependencies.
