import json
from extract_api import get_wikipedia_article

# load the index from the JSON file
with open('index_wikipedia_id.json') as file:
    index = json.load(file)

def get_article_text(wikidata_id):
    if wikidata_id in index:
        entry = index[wikidata_id]
        folder = entry['folder']
        filename = entry['file']
        offset = entry['offset']
        print(f"Found article for Wikidata ID {wikidata_id} in folder '{folder}' and file '{filename}' at offset {offset}.")
        with open(f'all_wikipedia_articles/{folder}/{filename}') as file:
            file.seek(offset)
            line = file.readline()
            data = json.loads(line)
            return data['text']
    else:
        print("No article found for the given Wikidata ID in stored files.")
        print("Attempting to fetch the article from Wikipedia API...")
        return get_wikipedia_article(wikidata_id)


# Example usage
if __name__ == '__main__':
    # wikidata_id = 'Q42'  # Example: Q42 is the Wikidata ID for Douglas Adams
    # article_text = get_article_text(wikidata_id)
    # print(article_text)

    # Test retrieval time
    import time
    start = time.time()
    id_list = ['Q42', 'Q25272', 'Q1425109', 'Q21730', 'Q54321']
    for wikidata_id in id_list:
        article_text = get_article_text(wikidata_id)
        # print(article_text)
    end = time.time()
    print(f"Time taken to retrieve 5 articles: {end - start:.2f} seconds.")
