# Documentation on using FastAPI

This space provides information on the use of FastAPI from an approach that covers the basic concepts and its implementation for the development of APIs with python.

## General description

FastAPI is a high-performance framework created by the Colombian Sebastian Ramirez for creating APIs with python. This is based on the frameworks of :

- **Starlette:**  is a lightweight ASGI framework/toolkit, which is ideal for building async web services in Python.
- **Pydanic:**  is a python library for performing data validation
- **Uvicorn:** A library that works as a server, allows any computer to become a server. Allows you to run applications

## Installation

1. **Creation of the virtual environment.**

```bash
  - pip install fastapi
  - pip install uvicorn
```

2. **Creation of main.py file.**
  This file contains variables, information about     versions and functions

3. **Execution**
```bash
  - uvicorn main:app --reload
  
```
## Automatic Documentation With Swagger


The automatic documentation describes each of the endpoints that the application has.
To access this documentation we must add "/docs" to the main url:

```bash
  http://127.0.0.1:5000/docs
```
## Command for route label
 Example routes for "Home" and "Movies"
```bash
  - @app.get('/',tags = ['Home'])
  - @app.get('/movies', tags = ['movies'])

```

## QUERY parameters
They are a string of key and values that allow the search action to be further extended. Its structure is composed of: url, ?, key, =, value. An explample is shown

```bash
  - http://127.0.0.1:5000/movies/?category=acci%C3%B3n
  
```

![Logo](https://user-images.githubusercontent.com/107004251/225199464-f5c959c1-02a1-4ab2-a106-2018c06c540a.jpeg)

