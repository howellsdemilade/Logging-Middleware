import logging
from logtail import LogtailHandler
import sys
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("token")

#get logger
logger = logging.getLogger()

#create formatter
formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s")

# create handlers
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("app.log")
better_stack_handler = LogtailHandler(source_token= token)


# set formatters
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

#add handlers to the logger
logger.handlers= [stream_handler, file_handler, better_stack_handler]

#set log-level
logger.setLevel(logging.INFO)

