import json
from wikimapper import WikiMapper
from wiki_dump_reader import extract_wikipedia_pages, Cleaner
import os


store_path = "all_wikipedia_articles/"
file_path = 'enwiki-latest-pages-articles.xml.bz2'
cleaner = Cleaner()
count = 0
empty_text = 0
mapper = WikiMapper("index_enwiki-latest.db")
offset = 0
index_table = {}
for title, text in extract_wikipedia_pages(file_path):
    text = cleaner.clean_text(text)
    # Convert Wikipedia title to Wikidata ID
    wikidata_id = mapper.title_to_id(title)
    # Save 100 articles per file
    # Save 100 files per directory
    # Save one JSON per line in the file
    folder = str(count // 10000)
    file = str(count // 100 % 100)
    if not os.path.exists(store_path + folder):
        os.makedirs(store_path + folder)
    if not os.path.exists(store_path + folder + "/" + file):
        offset = 0
        with open(store_path + folder + "/" + file, 'w') as f:
            f.write(json.dumps({'title': title, 'text': text}) + '\n')
    else:
        with open(store_path + folder + "/" + file, 'a') as f:
            f.write(json.dumps({'title': title, 'text': text}) + '\n')
    index_table[wikidata_id] = {'folder': folder, 'file': file, 'offset': offset}
    offset += len(json.dumps({'title': title, 'text': text}) + '\n')
    count += 1
    if text == '':
        empty_text += 1
    if count % 1000 == 0:
        print(f"Processed {count // 1000}k articles")
# Save the index to a file
with open('index_wikipedia_id.json', 'w') as file:
    json.dump(index_table, file, indent=4)
print(f"Total articles processed: {count}")
print(f"Articles with empty text: {empty_text}")
print("Processing complete.")
'''
Total articles processed: 5284051
Articles with empty text: 15636
'''
