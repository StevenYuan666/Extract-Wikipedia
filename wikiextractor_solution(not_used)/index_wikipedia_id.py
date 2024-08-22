import json
import os
from wikimapper import WikiMapper
mapper = WikiMapper("index_enwiki-latest.db")

extracted_files_path = 'extracted_files/'

index = {}

# Iterate over all files in the extracted_files directory
count = 0
empty_text = 0
for foldername in os.listdir(extracted_files_path):
    # Check if the entry is a directory and Iterate over all files in the directory
    if os.path.isdir(os.path.join(extracted_files_path, foldername)):
        for filename in os.listdir(os.path.join(extracted_files_path, foldername)):
            # Each line in the file is a JSON object
            with open(os.path.join(extracted_files_path, foldername, filename)) as file:
                offset = 0
                for line in file:
                    # Load the JSON object
                    data = json.loads(line)
                    # Convert Wikipedia ID to Wikidata ID
                    wikidata_id = mapper.title_to_id(data['title'])
                    index[wikidata_id] = {'folder': foldername, 'file': filename, 'offset': offset}
                    # Update the offset for the next JSON object
                    offset += len(line)
                    count += 1
                    if data['text'] == '':
                        empty_text += 1
                    if count % 100000 == 0:
                        print(f"Processed {count} articles")

# Save the index to a file
with open('index_wikipedia_id.json', 'w') as file:
    json.dump(index, file, indent=4)

print(f"Total articles processed: {count}")
print(f"Articles with empty text: {empty_text}")
print("Indexing complete.")

