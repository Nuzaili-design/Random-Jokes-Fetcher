import requests
import json
import pandas as pd

# Fetch 10 random jokes from the API
data2 = requests.get("https://official-joke-api.appspot.com/jokes/ten")
results2 = json.loads(data2.text)

# Create DataFrame and drop unnecessary columns
df3 = pd.DataFrame(results2)
df3.drop(columns=["type", "id"], inplace=True)

# Print the jokes nicely
for idx, row in df3.iterrows():
    print(f"Joke {idx+1}:")
    print(f"Setup: {row['setup']}")
    print(f"Punchline: {row['punchline']}\n")

# Ask user if they want to save the data to a CSV file
save_to_file = input("Save jokes to CSV file? (yes/no): ").strip().lower() == 'yes'

if save_to_file:
    df3.to_csv("jokes.csv", index=False)
    print("Jokes saved to jokes.csv")
else:
    print("Jokes not saved.") 
