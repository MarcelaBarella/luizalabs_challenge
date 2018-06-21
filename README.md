# Teste Luizalabs

Simple API to manage the use of meeting rooms

## Technologies 

In this solution, Python 3.6.5 was used with the following technologies:
-[Flask](http://flask.pocoo.org/) - Python icroframework based on Jinja 2.
-[flask_request_validator](https://github.com/d-ganchar/flask_request_validator) - Package to valide Flask requests.
-[MongoDB](https://www.mongodb.com/) - Document database for querying and indexing with scalability and flexibility.
-[pymongo](https://api.mongodb.com/python/current/) - Python distribution containing tools for working with MongoDB.
-[assertpy](https://github.com/ActivisionGameScience/assertpy) - Simple library that beautifies assertions on tests.


## Running the solution

### With Docker

If you want to run this solution without install anything on your machine, you must to use docker to run this solution. To build this solution with docker, you need to install it before (please refeer to [official docker docs](https://docs.docker.com/install/)).

Due to the fact that the requirements contains only the necessary to run this solution, the docker image uses Linux Alpine 3.7.

To build the container em follow the steps:

Go to the root of the project
>$ cd ../

Build the docker image (this will install all the listed dependencies on requirements)
>$ docker-compose build

Run app by executing container:  
>$ docker-compose up

## Usage
 To see more details about the usage of this API, please read the [USAGE](USAGE.md).


## Improvements

- Create app to consume this API and expose data to users
- Check if the number os participants in a meeting is higher then the capacity of the room
- Search a room by schedule



