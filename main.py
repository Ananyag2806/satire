import os
import openai
import constants

openai.api_key = constants.APIKEY
openai.File.create(
    file=open("prompt1_prepared.jsonl", "rb"),
    purpose='fine-tune'
)
