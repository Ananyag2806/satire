import csv
import json

# Read CSV file
with open('data.csv', 'r') as f:
    data = list(csv.reader(f))
    headers = data[0]
    data = data[1:]

# Create prompt and completion pairs
pairs = []
for row in data:
    if len(row) == 2:  # Ensure each row has two columns
        prompt_text = row[1]
        ideal_generated_text = row[0]
        # Create a dictionary for each pair and append it to the list
        pair = {
            "messages": [
                {
                    "role": "system",
                    "content": "generate satirical, witty, ironic, comedic, sarcastic headlines/sentences that have rich vocabulary from the prompt"
                },
                {"role": "user", "content": prompt_text},
                {
                    "role": "assistant",
                    "content": ideal_generated_text
                }
            ]
        }
        pairs.append(pair)

# Export to JSON file
with open('prompt_completion_pairs.json', 'w') as f:
    json.dump(pairs, f)
