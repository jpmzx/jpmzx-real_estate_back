# Real estate app - Backend

Real estate app is a test - mock app for track and get the stored information
about properties around the cities, Note: this is just a test case. 

## App design strategy

This app is meant to serve a set of REST APIs using a basic implementation of the Python's built-in http.server module and configurations files in order to declare routes, configurations, controllers and queries to the database(MySQL).

Focusing on the specification of this test case (entire app), this app has been developed without using any python web framework such Django, Falcon, Flask, FastAPI, Tornado, etc. Instead, I opted for use the python's built-in http.server capabilities for the socket and TCP requests management and I focused on extending it to be able to manage 'application/json' requests. On the top, this project intents to serve as a minimal framework for build API REST endpoints managing http requests an returning valid http json responses.

The interaction between the logic layer(Controllers) and the data layer(Database) was built using pure SQL queries with help from standard Mysql connector for Python.

## Table of contents
- [Real estate app - Backend](#real-estate-app---backend)
  - [App design strategy](#app-design-strategy)
  - [Table of contents](#table-of-contents)
  - [Getting started](#getting-started)
    - [OS Requirements](#os-requirements)
    - [Cloning the repository](#cloning-the-repository)
    - [Creating a new virtual environment](#creating-a-new-virtual-environment)
    - [Activating the virtualenv](#activating-the-virtualenv)
    - [Installing python dependencies](#installing-python-dependencies)
    - [Configuring the settings file](#configuring-the-settings-file)
    - [Starting the web server](#starting-the-web-server)
  - [Making HTTP requests to the exposed REST APIs](#making-http-requests-to-the-exposed-rest-apis)
  - [Checking grammar and pep8 compliance](#checking-grammar-and-pep8-compliance)
  - [Testing and code coverage](#testing-and-code-coverage)
    - [Testing strategy](#testing-strategy)
    - [Executing the tests](#executing-the-tests)
  - [Encountered problems and how I solved them](#encountered-problems-and-how-i-solved-them)
    - [Overriding the http.server.SimpleHTTPRequestHandler to handle json responses](#overriding-the-httpserversimplehttprequesthandler-to-handle-json-responses)
    - [Setting up the PYTHONPATH accordingly in execution time](#setting-up-the-pythonpath-accordingly-in-execution-time)
    - [Setting up the mockserver for testing the API endpoints](#setting-up-the-mockserver-for-testing-the-api-endpoints)
    - [Using dotenv library to "hide" sensitive information from git repositories](#using-dotenv-library-to-hide-sensitive-information-from-git-repositories)


## Getting started

Follow up the following sub-topics in order to setup the envirnment, execute the web server, and work with the API Rest endpoints.

### OS Requirements

Please make sure the following requirements are met before getting started
 - [git client](https://git-scm.com/downloads)
 - [Python >= 3.8](https://www.python.org/downloads/)
 - A web client like [Postman](https://www.postman.com/downloads/) or [Insomnia](https://insomnia.rest/download)


### Cloning the repository

Clone the app in a regular path and enter to the created folder
``` bash
$ git clone https://github.com/jpmzx/jpmzx-real_estate_back
$ cd real_estate_test_back/
```

### Creating a new virtual environment
Create a new virtualenv to install the python required dependencies

```bash
python3 -m venv .venv
```

### Activating the virtualenv

|Platform   |Shell   |Command to activate virtual environment|
|---|---|---|
|POSIX   |bash/zsh   |$ source .venv/bin/activate|
|POSIX   |fish   |$ source .venv/bin/activate.fish|
|POSIX   |csh/tcsh   |$ source .venv/bin/activate.csh|
|WINDOWS   |PowerShell Core|$ .venv/bin/Activate.ps1|
|WINDOWS   |cmd.exe   |C:\> .venv\Scripts\activate.bat|
|WINDOWS   |PowerShell   |PS C:\> .venv\Scripts\Activate.ps1|

```bash
$ source .venv/bin/activate
(.venv) $
```
More information about venv [here](https://docs.python.org/3/library/venv.html)

### Installing python dependencies

In order to install the required python dependencies listed in requirements.txt file do:

```bash
(.venv) $ python -m pip -r requirements.txt
```

### Configuring the settings file

The settings file is required to start the web server, so you'll need to create a file called .env at the root of the repository, you can find an example file called .env-template that contains the required properties to configure.

Use your preferred text editor to setup the configurations fill the values with a real data and save the file.

```bash
(.venv) $ cp .env-template .env
(.venv) $ nano .env # or use your preferred text editor
```

### Starting the web server

```bash
(.venv) $ python src/main.py
```

## Making HTTP requests to the exposed REST APIs

Open your preffered web client to make requests to the following API REST endpoints:

-   GET http://localhost:5000/property/public/
-   GET http://localhost:5000/property/public/?city=bogota
-   GET http://localhost:5000/property/public/?year=2020
-   GET http://localhost:5000/property/public/?status=pre_venta
-   GET http://localhost:5000/property/public/?year=2011&city=bogota
-   GET http://localhost:5000/property/

Feel free to import the file called postman-export.json to your installed Postman to facilitate the process of endpoints consumption.

## Checking grammar and pep8 compliance

In order to check the pep8 code compliance you can run the followinf commands, those commands will return an output in your terminal for each encountered non-compliant lines of code.

```bash
(.venv) $ pycodestyle tests/*
(.venv) $ pycodestyle src/*
```

## Testing and code coverage

This section explains how to execute tests an how those test script have been designed and developed.

### Testing strategy



### Executing the tests

```bash
(.venv) $ pytest --cov-report html --cov=src tests/
```
To review the coverage tests, be sure to open the generated file htmlcov / index.html in your browser after the pytest command execution is completed. 

## Encountered problems and how I solved them

### Overriding the http.server.SimpleHTTPRequestHandler to handle json responses 

### Setting up the PYTHONPATH accordingly in execution time

### Setting up the mockserver for testing the API endpoints

### Using dotenv library to "hide" sensitive information from git repositories
 