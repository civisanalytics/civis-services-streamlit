# civis-services-streamlit

This repository provides the following components:

* A Docker image to support Streamlit applications on Civis Platform
* A demo Streamlit app that's readily deployable on Civis Platform

## Quickstart Using the Demo Application

To get a sense of what a Streamlit app looks like on Civis Platform:

* Log on to Civis Platform.
* From the top navigation bar, click "Publish".
* Under "Services", click "Streamlit Demo".

These steps create a new Civis Platform service configured for a Streamlit demo app
pointing to this GitHub repository.
The app is now ready to be deployed.
Please follow [these instructions](https://support.civisanalytics.com/hc/en-us/articles/360001335031-Civis-Service-Deployment#StartaService/PreviewaDeployment)
for service deployment.

If you would like to start making the demo app your own
by making code changes,
you may [fork this GitHub repository](https://github.com/civisanalytics/civis-services-streamlit/fork)
(note: your fork would be public; GitHub only allows public forks from a public repository)
where the demo app's source code is in the directory [`demo_app/`](demo_app).
If you would like to host and use your own Docker image,
[`Dockerfile`](Dockerfile) and [`entrypoint.sh`](entrypoint.sh) from this GitHub repository
define the `civisanalytics/civis-services-streamlit` image that you may like to modify
and then host on your own DockerHub account.

## Building and Deploying Your Streamlit Application

If you would like to build your own Streamlit application from scratch
and deploy it on Civis Platform,
here are the requirements.

1. Your Streamlit application must have its source code hosted on a GitHub repository.
   The Civis Platform user account that's going to deploy this Streamlit app must have
   access to this GitHub repo.
2. The following explains the expected files for your app.
   Note that these files listed must be at the same directory in your GitHub repository.

   * Your app's entry-point Python script

     A required file, with a file extension name `.py` for a Python script.
     This is your Streamlit app's entry point
     (i.e., `streamlit run <something>.py` will be executed to spin up your app).
     The recommended filename is `app.py`, but if you use a different filename,
     you must specify its file path
     (starting from your repo's root, e.g., `from/repo_root/to/your_custom_app.py`)
     in the Civis Platform service your're going to set up (see below).
     For which Python version you should use (e.g., Python 3.13),
     it is determined by which Docker image name and tag you're going to use
     to deploy your app on Civis Platform.
     The Python version is specified by the base image in the file `Dockerfile`
     of this GitHub repo.

   * `requirements.txt`

     A strongly recommended file, though not strictly required.
     `requirements.txt` specifies the Python dependencies to be installed for your Streamlit app to work.
     Note that `streamlit` itself should be one of the packages specified
     (so that you can pin the specific Streamlit version for your use case).
     If `requirements.txt` is present,
     the command `pip install -r requirements.txt` will be run to install these dependencies.

   * `pyproject.toml`

     An optional file.
     If a Python package needs to be installed in order for your Streamlit app to work,
     `pyproject.toml` plus the associated package code must be present.
     If `pyproject.toml` is detected,
     `pip install --no-deps -e .` will be run to install your Python package
     (`--no-deps` for not installing dependencies defined in `pyproject.toml`,
     because they should already be specified in `requirements.txt` above).

   * `.streamlit/config.toml`

     An optional file.
     These are Streamlit options, if you need to configure them. Reference:
     https://docs.streamlit.io/develop/api-reference/configuration/config.toml

3. Once your app code is on a GitHub repo, either create a new service on Civis Platform
   by following [this page](https://support.civisanalytics.com/hc/en-us/articles/360001335031-Civis-Service-Deployment),
   or launch a Streamlit template service from Civis Platform's top navigation bar -> Publish
   -> Services -> Streamlit Demo.
   Specify or adjust the GitHub repo URL as well as the Git tag (or branch, or Git commit hash).
4. If your code is at a directory in your repo (rather than directly at the root level of your repo),
   specify the directory path that points to where the app code is located.
   (For the demo app in the previous section above, the directory path would be `demo_app` from this current repo.)
   By default, your Streamlit app's entry point Python script is assumed to be named `app.py`.
   If you use a filename other than `app.py`,
   you must specify its file path starting from the repo root, e.g., `from/repo_root/to/your_custom_app.py`.
5. For the Docker image, the name is `civisanalytics/civis-services-streamlit`,
   and the tag is one of those [listed on DockerHub](https://hub.docker.com/r/civisanalytics/civis-services-streamlit/tags).
   Note that the specific Docker image name and tag you've chosen determines which Python version
   your app is going to run on.

## Support

For feature inquiries, bug reports, and other questions,
Civis client users should reach out to support@civisanalytics.com.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

BSD-3

See [LICENSE.txt](LICENSE.txt).
