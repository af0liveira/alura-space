Alura Space Photo Gallery
=========================

Welcome to Alura Space, a web application for space photos!

The application is a platform for visualizing and sharing astronomy images.
To use the application, users are required to sign up.
Once logged in, the user will have access to the full photo gallery and will be able to upload their own images.

This project implements the backend of the application using Python 3.10 with the Django 4.1 framework.
Additionaly, the Amazon S3 service is used for storing the images files in the cloud.

> ⚠️ You should note that **only the image files are stored in the cloud**.
> The application's database will remain local and is not part of this repository.

This project was developed as part of the [Django formation](https://cursos.alura.com.br/formacao-django) at the [Alura](https://www.alura.com.br/) tech school.
The original frontend project and assets were obtained from [here](https://github.com/alura-cursos/alura_space/tree/projeto_front).

Getting Started
---------------

To run the Alura Space application, you'll need to have Python, Django, and all required dependencies installed.
You can do this by setting up a virtual environment with the required dependencies using either `conda` or `virtualenv`.

You'll also need to set up a bucket on Amazon S3 for storing the image files.

You can follow the steps below to have the application up and running.

1. Clone the repository to your local machine.

    ```sh
    git clone https://github.com/af0liveira/alura-space.git
    ```

2. Navigate to the root directory of the project

    ```sh
    cd alura-space
    ```

3. Create and activate a new virtual development environment

    If you're using `conda`:[^1]

    [^1]: If necessary, append `conda-forge` to your channels list using the command

        ```sh
        conda config --append channels conda-forge
        ```

    ```sh
    conda create --prefix ./venv --file environment.yml
    conda activate 
    ```

    If you're using `virtualenv` + `pip`:

    ```sh
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

4. Set up the environment variables of the application.
   This should be done by creating a `.env` file in the root directory of the project with the following content:

    ```sh
    # Django key
    SECRET_KEY=<django_secret_key>
    # Amazon S3 keys
    AWS_ACCESS_KEY_ID=<your_access_key>
    AWS_SECRET_ACCESS_KEY=<your_secret_key>
    AWS_STORAGE_BUCKET_NAME=<your_bucket_name>
    ```

    Replace `<django_secret_key>` with your own Django key.
    You can use `python scripts/secret_key_generator.py` to create a new key, if necessary.

    Replace `<your_access_key>`, `<your_secret_key>`, and `<your_bucket_name>` with your own Amazon S3 keys and bucket name.

5. Migrate the database by running the command

    ```sh
    python manage.py migrate
    ```

6. Start the application server by running the command

    ```sh
    python manage.py runserver
    ```

Now you should be able to access the Alura Space application by visiting `http://localhost:8000` in your web browser.

> ⚠️ At this point the application will display an empty photo gallery, since no images have been added yet.

Managing the application
------------------------

The application can be managed via `Django Admin` by visiting the URL `http://localhost:8000/admin` on your web browser.
However, you'll need to create a superuser.

To create a superuser:

1. Navigate to the root directory of the project.
2. Make sure that the virtual development environment has been activated (see above).
3. Run the command

    ```sh
    python manage.py createsuperuser
    ```

4. Follow the instructions to enter the user name, email, and password.
5. Start the server with the command

    ```sh
    python manage.py runserver
    ```

6. Access Django Admin on your browser via the URL `http://localhost:8000/admin`.
