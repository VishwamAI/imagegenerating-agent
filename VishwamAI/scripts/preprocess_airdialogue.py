import json
import os
from transformers import GPT2Tokenizer

def preprocess_airdialogue(data_dir, output_file):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    dialogues = []

    # Iterate through all JSON files in the data directory
    for filename in os.listdir(data_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(data_dir, filename)
            with open(file_path, "r") as file:
                for line in file:
                    try:
                        data = json.loads(line)
                        # Check if 'dialogue' key exists in the JSON object
                        if 'dialogue' in data:
                            # Extract the dialogue text
                            dialogue_text = " ".join([turn.split(": ")[1] for turn in data["dialogue"]])
                            dialogues.append(dialogue_text)
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON in file {file_path}: {e}")
                    except KeyError as e:
                        print(f"Key error in file {file_path}: {e}")
                    except IndexError as e:
                        print(f"Index error in file {file_path}: {e}")

    # Tokenize the dialogues and save to the output file
    with open(output_file, "w") as file:
        for dialogue in dialogues:
            tokens = tokenizer.encode(dialogue, add_special_tokens=True)
            file.write(" ".join(map(str, tokens)) + "\n")

if __name__ == "__main__":
    data_dir = "/home/ubuntu/VishwamAI/data/airdialogue_data_1.3/airdialogue"
    output_file = "/home/ubuntu/VishwamAI/data/airdialogue_data_1.3/airdialogue_preprocessed.txt"
    preprocess_airdialogue(data_dir, output_file)
    print(f"Preprocessing complete. Tokenized dialogues saved to {output_file}.")
