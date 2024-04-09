from openai import OpenAI
import json
import os  # used to read in environment variable

APIKEY = os.environ['OPENAI_API_KEY']
ORG = os.environ['ORGANIZATION']
client = OpenAI()


