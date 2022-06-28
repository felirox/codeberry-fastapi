import uvicorn 

#######################################################################################################################################
#Since FastAPI does not have the capability to run as a server by itself, we will be using uvicorn to help us with the server creation
#######################################################################################################################################

config = uvicorn.Config("main:app", port=5000, log_level="info")
server = uvicorn.Server(config)
server.run()