# Alura Space

This project is the backend implementation of a website for displaying space
photographs, _Alura Space_.

This project was developed within the online formation [Django: crie aplicações
em Python](https://cursos.alura.com.br/formacao-django) \[Django: develop
applications in Python\] of the [Alura school](https://www.alura.com.br/).

The main page displays a thumbnail gallery of the photos in reverse
chronological order or inclusion.
The user can click the thumbnail to open the full-size image on a separate page
with additional information about the photo.

A search mechanism has also been implemented, by which the user can search for
image titles matching the search terms.

## Running the application

To run the application:

1. Clone the repository from GitHub

    ```sh
    git clone https://github.com/af0liveira/alura-space.git
    ```

2. Enter the cloned repository and create the virtual environment (the example
   shows the use of _conda_, but you can use _virtualenv_ as well, as explained
   below)

    ```sh
    cd alura-space
    conda create --prefix ./venv --file environment.yml
    conda activate ./venv
    ```

3. Start the server

    ```sh
    python manage.py runserver
    ```

The development server should not be available at `http://127.0.0.1:8000/`.

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
