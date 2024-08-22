import json

# Load the index from the JSON file
with open('index_wikipedia_id.json') as file:
    index = json.load(file)


# Define a function to retrieve the article text given a Wikidata ID
def get_article_text(wikidata_id):
    if wikidata_id in index:
        entry = index[wikidata_id]
        folder = entry['folder']
        filename = entry['file']
        offset = entry['offset']
        print(f"Found article for Wikidata ID {wikidata_id} in folder '{folder}' and file '{filename}' at offset {offset}.")
        with open(f'extracted_files/{folder}/{filename}') as file:
            file.seek(offset)
            line = file.readline()
            data = json.loads(line)
            return data['text']
    else:
        return "No article found for the given Wikidata ID."


# Example usage
if __name__ == '__main__':
    wikidata_id = 'Q28865'  # Example: Q42 is the Wikidata ID for Douglas Adams
    article_text = get_article_text(wikidata_id)
    print(article_text)
