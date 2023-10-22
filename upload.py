import os
import openai
import constants

openai.api_key = constants.APIKEY
res = openai.File.create(
    file=open("data1.jsonl", "rb"),
    purpose='fine-tune'
)
file_id = res['id']
print(f"File ID: {file_id}")
