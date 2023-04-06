# Alura Space

This project is the implementaion of a simple photo gallery for spatial images.

The _home_ page displays thumbnails of the images, which can be clicked and
opened on a separate page with further information about the image.

The project was implemented in Django as part of the course [_Django: templates
e boas
práticas_](https://cursos.alura.com.br/course/django-templates-boas-praticas)
\[_Django: templates and good practices_\] from
[Alura](https://www.alura.com.br/).

## Virtual development environment

The files `environment.yml` and `requirements.txt` are provided for creating the
virtual development environment with either _conda_ or _virtualenv_.

If using _conda_, the environment can be created in the local folder `venv/`
with the command

### Using _conda_

The following command will install the virtual environment in the local
directory `venv/`

```sh
conda create --prefix ./venv --file environment.yml
```

To use the environment, it can be activated with

```sh
conda activate ./venv
```

Further details on environment management with _conda_ can be found
[here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#).

### Using _virtualenv_

In this case, the environment can be created and activated before installing the
packages:

```sh
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Updating the virtual environment

If new packages are installed in the virtual environment, `environment.yml` and
`requirements.txt` must be updated.

Once the environment has been activated, the following commands can be used

```sh
# Make sure that the venv has been activated!
conda list -e > environment.yml
pip list --format=freeze > requirements.txt
```

---

