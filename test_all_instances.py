import pytest
import requests
import sys
import os
import time

os.environ['NO_PROXY'] = '127.0.0.1'
# exec(open("start_app.py").read())
# execfile('start_app.py')

# time.sleep(5)

HOME_URL="http://127.0.0.1:5000"
csv="ttrfastapi.csv"

class Custom_FastAPITest_Plugin:
    def pytest_sessionfinish(self):
        print("*** test run reporting finishing")


def test_mainlink_working(): #Check working of GET request
    response = requests.get(HOME_URL)
    assert response.status_code == 200, "URL not working"
    
# def test_sublink_working(): #Check working of POST Request
# 	# with open("ttrfastapi.csv", "rb") as a_file:
# 	# 	file_dict = {"ttrfastapi.csv": a_file}
# 	# 	response = requests.post(HOME_URL+"/uploadfiles/", files=file_dict)
# 	# response = requests.post(HOME_URL+"/uploadfiles/", files={'ttrfastapi.csv': f})
# 	with open(csv, 'rb') as f:
# 		r = requests.post("http://127.0.0.1:5000/files", files={'file': ('ttrfastapi.csv', f, 'text/csv', {'Expires': '0'})})
# 		print(r.text)
# 		# print(response.text)
# 	assert r.status_code == 200, "URL not working"
 
 

if __name__ == "__main__":
    sys.exit(pytest.main( ['-s'],plugins=[Custom_FastAPITest_Plugin()]))