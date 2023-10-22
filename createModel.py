import openai
import constants

openai.api_key = constants.APIKEY
res = openai.FineTuningJob.create(
    training_file="file-TZBHnDlkalBzSL7mEEU2rnJ1", model="gpt-3.5-turbo")

job_id = res['id']
print(f"Job ID: {job_id}")
