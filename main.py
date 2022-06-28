#############################################
## IMPORTING THE NECESSARY LIBRARIES ##
#############################################
from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from typing import List, Union
from fastapi.responses import HTMLResponse
import csv
from fastapi.responses import FileResponse
from io import StringIO
import pandas as pd
import email_function as ef
from threading import Thread
import asyncio
import functools
import time
from datetime import datetime

#############################################
#Initialising FastAPI by calling it's class
#############################################
app = FastAPI()

class User(BaseModel):
    user_name: dict

#Initialising a main DataFrame in order to store and process easily
maindf=pd.DataFrame()

#############################################
#A Decorator Function to understand the time taken in each function
#############################################
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print("Finished {} in {} secs".format(repr(func.__name__), round(run_time, 3)))
        return value

    return wrapper


# A spoof URL to check if POST is working perfectly
@app.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    
    return {"file_sizes": [len(file) for file in files]}

##########################################################################################
#Function to call the provided email function and work accordingly
#Note that an additional argument is being passed to the email function in order to smoothen the process
##########################################################################################
@timer            
async def emailCheckFunc(indf):
    global maindf
    # mainop=[]
    if 'Email' in indf:
        op=await asyncio.gather(*(ef.get_details(i,r["Email"]) for i,r in indf.iterrows()))
        resultDf = pd.DataFrame(op)
        # print(resultDf)
        maindf['index'] = range(0, len(maindf))
        # maindf['index_col'] = maindf.index
        maindf=pd.merge(maindf,resultDf, on='index')
        # for iter in op:
        #     maindf.at[iter['index']] = restaurant_latitude
        #     maindf
        # print(maindf)
        del maindf['index']
        maindf.to_csv("result.csv")
            # mainop.append(await wholeRowThreaded(r))
            
            # t = Thread(target=wholeRowThreaded, args=(r,))
            # t.start()
    # i=input()
    # print("MOP",mainop)
#############################################
#URL to perform POST Request of Uploading the file  
#############################################
@timer
@app.post("/uploadfiles/") 
async def create_upload_files(files: UploadFile = File(...),header_row: Union[bool, None] = True,column_identifier: Union[str, None] = None):
    start = datetime.now()
    global maindf
    contents = await files.read()
    decoded = contents.decode()
    buffer = StringIO(decoded)
    csvReader = csv.DictReader(buffer)
    # maindf_2=maindf
    if header_row==False: 
        print("Feed Received: Data has no header")
        maindf = pd.DataFrame(csvReader,header=None)
    else:
        maindf = pd.DataFrame(csvReader)
    print(maindf)
    await emailCheckFunc(maindf)
    print("Time taken to complete {} records: {}".format(len(maindf.index),datetime.now()-start))
    # buffer.close()
    return FileResponse("result.csv",media_type='application/octet-stream',filename="result.csv")
    # return {"filenames": [file.filename for file in files]}
    
#######################################################################################################################################
#Home PAGE which can have a hypothetical UI to provide interface to user to fetch the data from the client using forms/etc.
#######################################################################################################################################
@timer   
@app.get("/")
async def main():
    content = """
<body>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)