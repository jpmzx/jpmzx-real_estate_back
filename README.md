# Real estate app - Backend

Real estate app is a test - mock app for track and get the stored information
about properties around the cities, Note: this is just a test case. 

## App design strategy

This application is intended to serve a set of REST APIs using a basic implementation of Python's built-in http.server module and configuration files to declare paths, settings, drivers, and queries to the database (MySQL).

Focusing on the specification of this test case (full application), this application has been developed without using any Python web framework like Django, Falcon, Flask, FastAPI, Tornado, etc. Instead, I opted to use Python's built-in http.server capabilities for TCP and socket request handling and I concentrated on extending it to be able to handle 'application / json' requests. At the top, this project is intended to serve as a minimal framework for building API REST endpoints that handle http requests and return valid http json responses.

The interaction between the logical layer (Drivers) and the data layer (Database) was created using pure SQL queries with the help of the standard Mysql connector for Python.

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

Follow the subtopics below to set up your environment, run the web server, and work with Rest API endpoints. 
### OS Requirements

Please make sure the following requirements are met before getting started
 - [git client](https://git-scm.com/downloads)
 - [Python](https://www.python.org/downloads/) >= 3.8
 - python3-venv (Usually comes with python 3.3+ versions)
 - A web client like [Postman](https://www.postman.com/downloads/) or [Insomnia](https://insomnia.rest/download)


### Cloning the repository

Clone the app in a regular path and enter to the created folder
``` bash
$ git clone https://github.com/jpmzx/jpmzx-real_estate_back
$ cd jpmzx-real_estate_back/
```

### Creating a new virtual environment
Create a new virtualenv to install the python required dependencies

```bash
python3 -m venv .venv
```

### Activating the virtualenv

Once the virtualenv is created, proceed to activate it using your
operating system command from the following table

|Platform   |Shell   |Command to activate virtual environment|
|---|---|---|
|POSIX   |bash/zsh   |$ source .venv/bin/activate|
|POSIX   |fish   |$ source .venv/bin/activate.fish|
|POSIX   |csh/tcsh   |$ source .venv/bin/activate.csh|
|WINDOWS   |PowerShell Core|$ .venv/bin/Activate.ps1|
|WINDOWS   |cmd.exe   |C:\> .venv\Scripts\activate.bat|
|WINDOWS   |PowerShell   |PS C:\> .venv\Scripts\Activate.ps1|

i.e using bash in linux

```bash
$ source .venv/bin/activate
(.venv) $
```
Note that the (.venv) should appear at the beginning of the line after activating your virtualenv
More information about venv [here](https://docs.python.org/3/library/venv.html)

### Installing python dependencies

In order to install the required python dependencies listed in requirements.txt file do:

```bash
(.venv) $ python -m pip install -r requirements.txt
```

### Configuring the settings file

The settings file is required to start the web server, so you'll need to create a file called .env at the root of the repository, you can find an example file called .env-template that contains the required properties to configure.

Use your preferred text editor to setup the configurations fill the values with a real data and save the file.

```bash
(.venv) $ cp .env-template .env
(.venv) $ nano .env # or use your preferred text editor
```

### Starting the web server

Execute the following line to start the web server using the .env file settings

```bash
(.venv) $ python src/main.py
```
Note: Press CTRL+C to stop the web server
## Making HTTP requests to the exposed REST APIs

Once you saw a message like "Starting http server at localhost: 5000" in your terminal, open your preferred webclient to make requests to the following API REST endpoints: 

-   GET http://localhost:5000/property/public/
-   GET http://localhost:5000/property/public/?city=bogota
-   GET http://localhost:5000/property/public/?year=2020
-   GET http://localhost:5000/property/public/?status=pre_venta
-   GET http://localhost:5000/property/public/?year=2011&city=bogota
-   GET http://localhost:5000/property/


Feel free to import the file named postman-export.json into your installed Postman to ease the endpoint consumption process.
## Checking grammar and pep8 compliance

To verify compliance with the pep8 standard, you can run the following commands, those commands will return an output in your terminal for each non-compliant line of code that it finds.

```bash
(.venv) $ pycodestyle tests/*
(.venv) $ pycodestyle src/*
```

## Testing and code coverage

This section explains how to execute tests an how those test script have been designed and developed. 

### Testing strategy

Writing specific test cases before starting the development of the functionality is an excellent way to save validations or unnecessary scope extensions, following the ideology of TDD (Test driven development) I have written specific test cases for the endpoints that allow to develop only the code necessary to fulfill them. 
### Executing the tests

```bash
(.venv) $ pytest --cov-report html --cov=src tests/
```
To review the coverage tests, be sure to open the generated htmlcov / index.html file in your browser after the pytest command completes. 

## Encountered problems and how I solved them

### Overriding the http.server.SimpleHTTPRequestHandler to handle json responses

I had to inspect the library a bit, understand how the binary writing works on files that are the ones that finally serve as input and response to requests through sockets 

### Setting up the PYTHONPATH accordingly in execution time

When different programs try to run the same python code from different locations in the local file system, module imports usually fail because by default the initial execution path is the only known one, to solve it and be able to correctly execute the test cases As well as executing the src / main.py from the root of the repository, I had to use the os and sys modules to register the execution root of the code in the PYTHONPATH (List of directories to detect python modules) 

### Setting up the mockserver for testing the API endpoints

In order to test the test cases through http requests, I had to do a lot of research in different resources to generate a mockserver that would allow the execution of the test cases locally, in addition to implementing data parsing functions for the coding of the assertions. in test cases. 
### Using dotenv library to "hide" sensitive information from git repositories

It seems like a straightforward requirement, however, hiding sensitive execution credentials like passwords from public source code in a repository can be complex. Using dotenv I managed to use configuration files similar to those of bash to configure the execution configurations of the application from the root of the repository. 