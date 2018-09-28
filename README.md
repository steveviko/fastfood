# Fast-Food-Fast

[![Build Status](https://travis-ci.org/steveviko/fastfood.svg?branch=develop)](https://travis-ci.org/steveviko/fastfood)
[![Coverage Status](https://coveralls.io/repos/github/steveviko/fastfood/badge.svg?branch=develop)](https://coveralls.io/github/steveviko/fastfood?branch=develop)

- Fast-Food-Fast is a food delivery service app for a restaurant.

# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

# Installation
**Clone this _Repository_**

 - [clone](https://github.com/steveviko/fastfood/tree/develop) to your computer


 # Tools
 ``` 
●	Server-Side Framework: <Flask Python Framework>
●	Linting Library: <Pylint, a Python Linting Library>
●	Style Guide: <PEP8 Style Guide>
●	Testing Framework: <unittest, test runner package>
 ```
# Running the tests
To run tests run this command below in your terminal

```
$ nosetests example_unit_test.py
```
**Create virtual environment and install it**
```
$ virtualenv - -python = python3 venv
$ source / venv/bin/activate
```
**Install all the necessary _dependencies_ by**
```
$ pip install - r requirements.txt
```
**Run _app_ by**
```
$ Python run.py
$ Run the server At the terminal or console type
```
# Project APIs
|           End Point | Functionality |
| -------------------------------------- | ----------------------------------------- |
|     POST   api/v1/orders                  | Place a new order |
|     PUT api/v1/orders/<int: orderId >     | Update the status of an order |
|     GET  api/v1/orders/<int: questionId > | Fetch a specific order |
|     GET  api/v1/orders                    | Get all orders |

Open the browser to view the endpoints with their specifications
* localhost:5000 


# Contributors
- [Steven Opio](https://github.com/steveviko)

# This Platform is served by  
- Git-pages [GitHub Pages](https://steveviko.github.io/fastfood/). 

# Demo
- The API is hosted [Here](https://fast-food-steven.herokuapp.com/api/v1/orders)

### License
- MIT License

Copyright (c) 2018 **VenViko**
