# FastAPI task: CodeBerry

This repository contains a solution to the task provided by Codeberry.


## Working

The application has been developed UAT Ready. 
The code has been deployed live on Heroku:
#### [https://codeberry-app.herokuapp.com/](https://codeberry-app.herokuapp.com/)

A HTML powered UI has also been provided to access the API with ease.

You can [use this file](https://raw.githubusercontent.com/felirox/codeberry-fastapi/main/ttrfastapi.csv) for instantly uploading and checking how the file is working.

***Right click and click "save as" to save this file to your PC.***

## Installation

You can clone this repo by running
```bash
git clone https://github.com/felirox/codeberry-fastapi
```

The program was written using Python3. The code is available in a Python (.py) file. 

No additional application is necessary if you have Jupyter installed. However, certain libraries need to be installed. Check below for more information.

## Requirements

To install the requirements, open your terminal and head over to the directory where this cloned code is present. 

Run the following command to install all the necessary libraries:

```bash
pip install -r requirements.txt
```
## Pointers

- FastAPI has been used to develop the Application
- The same has been deployed on Heroku
- async has been used in the program to fasten the process and increase efficiency
- The time taken to complete each task is printed in the console
- PyTest has been used to implement testing scenarios wherever possible *(test_all_instances.py)*
- Sending a POST request to /uploadfiles along with the optional parameters will return back with the processed file

## Running Locally

- To run the application locally, make sure all the requirements are installed, as mentioned above. 

- To make the running easier, all you need to do is simply run the *start_app.py* file and uvicorn will start the server.

## References
- FastAPI Documentation for Python
- Uvicorn Documentation for Python
- Gunicorn Documentation for Python
- PyTest Documentation for Python
- https://pypi.org/ for all the pip-based downloads
- https://www.makeareadme.com/ to make this readme
- https://stackoverflow.com/ for the countless doubts and silly errors that popped up

## License
MIT