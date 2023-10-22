import openai

openai.api_key = "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"
res = openai.FineTuningJob.retrieve("ftjob-Y8cvGVHPLWwv4HMKOzmU7wty")
print(res)
