## Local testing environment setup
### Pip

Even though the package management for this repo is handled by Poetry, `pip` is still required to download and
configure Python modules. To install pip:

```shell
sudo apt update
sudo apt install python3-pip
```

To check this has been installed correctly, simply run:

```shell
pip --help
```

To verify you have the latest version installed, run:

```shell
pip --version
pip 21.2.4
```

If an older version is installed, upgrade by running:

```shell
pip install --upgrade pip
```

### Pyenv

Pyenv is used to easily control the versions of Python being used across different projects and repositories.
To install pyenv:

```shell
sudo apt install -y make build-essential \
                         libssl-dev \
                         zlib1g-dev \
                         libbz2-dev \
                         libreadline-dev \
                         libsqlite3-dev \
                         wget \
                         curl \
                         llvm \
                         libncurses5-dev \
                         libncursesw5-dev \
                         xz-utils \
                         tk-dev \
                         libffi-dev \
                         liblzma-dev \
                         python-openssl \
                         git
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```

Ensure to restart your terminal after performing the above. To check this has been installed correctly, simply run:

```shell
pyenv --help
```

Please ensure to install the `pyenv-update` plugin so that it can be updated from the command line. To do this:

```shell
git clone https://github.com/pyenv/pyenv-update.git $(pyenv root)/plugins/pyenv-update
```

This will allow `pyenv` to be updated by running the following. It is important to do this as `pyenv` caches the
versions of Python available and so major and/or minor patches may not appear available to use without doing this.

```shell
pyenv update
```

This repository uses Python 3.9, so to install the latest version of that via `pyenv`:

```shell
pyenv install -v 3.9.7
```

This will take a few minutes as it builds Python from source. To then use this version of Python going forward:

```shell
pyenv local 3.9.7
pyenv global 3.9.7
```

To confirm the correct python version is being used, run the following command:

```shell
python --version
Python 3.9.7
```

To confirm the correct python version is being used by pyenv, run the following command:

```shell
pyenv version
3.9.7 (set by <directory>/pipeline-testing/.python-version)
```

### Poetry

The project is managed by [Poetry](https://python-poetry.org/). To install poetry, please follow the
[official guide](https://python-poetry.org/docs/).

Once Poetry is installed, to create the virtual environment and install the necessary packages, run the following
command from the root of this repo:

```shell
poetry config virtualenvs.in-project true
poetry install
```

This should create a `.venv` directory at the root of the repo.

### PyCharm

After opening the `my-project` repo as a project inside PyCharm, it needs attaching as a standalone project
within PyCharm. This allows it to be assigned its own Python interpreter (i.e. the virtual environment created by
Poetry above). To do this:

- Click `File -> Open...`
- Select the `my-project` directory
- Click `OK`
- Select the `Attach` option to attach this as an additional project

Once done, the `my-project` directory in the `Project` pane should be bolded.

To configure the Python interpreter for the `my-project` project:

- Open the PyCharm settings dialog (`Ctrl+Alt+S`)
- Expand the `Project` caret in the pane on the left-hand side
- Select `Python Interpreter`
- Select `my-project`
- Click the cog on the right-hand side of the dialog
- Select `Show All...`
- Click `+` to add a new interpreter
- Select the `Existing Environment` radio button
- Click the `...` button
- Navigate to `my-project/.venv/bin/python`
- Click `OK`
- Rename the new interpreter to `my-project` (for easier traceability)
- Click `OK`
- Click `Apply`

This should have correctly configured the `my-project` project to use the Python interpreter
created by Poetry. To confirm:

- Open any Python file in the `my-project` project
- Expand the `Imports` section at the top of the file
- All imports should be recognised and not underlined in red

### ChromeDriver

Install the latest release of the [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).

Ensure to move the ChromeDriver executable to a location available to the system path:

```shell
sudo mv ~/Downloads/chromedriver /usr/local/bin
```

To test this is installed correctly, open a new terminal and run:

```
chromedriver
```
## Docker
This repo contains a [Dockerfile](./Dockerfile) so that the framework and tests can be run in a container within
Jenkins. If changes are being made to this file, it is a requirement that the Docker image is built locally and the
tests are run via that Docker image to ensure that they continue to work.

- Before building the docker image, verify that the latest version of Docker is installed. Run:

```shell
docker --version
Docker version 20.10.12, build 20.10.12-0ubuntu2~20.04.1
```

- If you have a lower version, upgrade Docker. Simply run:

```shell
sudo apt-get install docker-ce
```
- Make sure you are connected to the Docker registry
```shell
docker pull hello-world
```
If got `Failed to lookup host: registry-1.docker.io`, login/signup into the Docker registry. For WSL, open Docker GUI and hit login button at the top right.

- To build the Docker image, run the following command from the root of this repo:

```shell
docker build -t "aut:local" .
```

# Running Tests
## Via Pycharm
Confirm that the project has been installed and PyCharm project interpreter, running configuration and environment variables has been configured correctly.
Use the PyCharm UI to run the test, and it should pass first time. Pycharm is automatically put root folder into `sys.path`, which updates `PYTHONPATH` and prevents ImportError

## Via CLI
By using `python -m` we are adding root to `sys.path` see https://stackoverflow.com/questions/36022892/how-to-know-if-docker-is-already-logged-in-to-a-docker-registry-server
- `poetry run python -m pytest [OPTIONS]` will temporarily activate specific environment
- `poetry shell` will permanently activate environment, then we could run `python -m pytest [OPTIONS]`

## Via Docker

To run the tests inside a container using the image built above:

```shell
docker run aut:local /bin/bash -c "pytest -v --tb=line --reruns 3"
```
## Via Jenkins
- Open Jenkins in your local machine
- Create a new Job.
- Choose type of job "Pipeline"
- In the page that opens, click tab Pipeline
- In field "Definition" choose "Pipeline script from SCM"
- In field "SCM" choose "Git"
- Enter this repository URL "https://github.com/hannachrnvsk/tms_final_project"
- In field "branches to build" emter "*/main"
- Save
- Move to job page
- Click "Build now"
