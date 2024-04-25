# civis-services-streamlit

This repository provides a Docker image for deploying a Streamlit application
on Civis Platform.

## Building and Deploying Your Streamlit Application

1. Your Streamlit application must have its source code hosted on a GitHub repository.
   The Civis Platform user account that's going to deploy this Streamlit app must have
   access to this GitHub repo
   (either because this GitHub repo is public, or because the Civis Platform user account
   is associated with a GitHub credential that can access this private GitHub repo).
   For a test app, you may [fork this GitHub repository](https://github.com/civisanalytics/civis-services-streamlit/fork)
   where the app's source code is provided at [`test_app/`](test_app).
2. The following explains the expected files for your app:

   ```shell
   app.py
   # A required file.
   # app.py is your Streamlit app's entry point.
   # For which Python version you should use (e.g., Python 3.12),
   # it is determined by which Docker image name and tag you're going to use
   # to deploy your app on Civis Platform.
   # The Python version is specified by the base image in the file `Dockerfile`
   # of this GitHub repo.

   requirements.txt
   # A strongly recommended, though not required, file.
   # requirements.txt specifies the Python dependencies to be installed for your Streamlit app to work.
   # Note that "streamlit" itself should be one of the packages specified
   # (so that you can pin the specific Streamlit version for your use case).
   # If requirements.txt is presented,
   # the command `pip install -r requirements.txt` will be run to install these dependencies.

   pyproject.toml
   # An optional file.
   # If a Python package needs to be installed in order for your Streamlit app
   # to work, pyproject.toml plus the associated package code must be present.
   # If pyproject.toml is detected, `pip install --no-deps -e .` will be run to install
   # your Python package (`--no-deps` for not installing dependencies defined
   # in pyproject.toml, because they should already be specified in requirements.txt above).

   .streamlit/config.toml
   # An optional file.
   # These are Streamlit options, if you need to configure them. Reference:
   # https://docs.streamlit.io/develop/api-reference/configuration/config.toml
   ```

3. Once your app code is on a GitHub repo, create a new service on Civis Platform
   by following [this page](https://support.civisanalytics.com/hc/en-us/articles/360001335031-Civis-Service-Deployment).
   Most importantly, specify the GitHub repo URL as well as the Git tag (or branch, or Git commit hash).
4. If your code comes from the test app in this GitHub repository,
   specify the path `test_app` that points to where the app code is located.
   If this path is unspecified, the app code must be at the root level of your GitHub repository.
5. For the Docker image, the name is `civisanalytics/civis-services-streamlit`,
   and the tag is one of those [listed on DockerHub](https://hub.docker.com/repository/docker/civisanalytics/civis-services-streamlit/tags).
   Note that the specific Docker image name and tag you've chosen determines which Python version
   your app is going to run on.

## Support

For feature inquiries, bug reports, and other questions,
Civis client users should reach out to their Civis point-of-contact person,
whereas Civis employees should file an internal ticket.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

BSD-3

See [LICENSE.txt](LICENSE.txt).
