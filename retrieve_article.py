import os
import indexed_bzip2 as ibz2
from xml.etree import ElementTree
import json
from record_offset import Cleaner


def retrieve_content(wikidata_id):
    with open('wikidata_id_index_table.json') as file:
        index_table = json.load(file)
    if wikidata_id in index_table:
        entry = index_table[wikidata_id]
        if len(entry) == 1:
            offset = entry["0"]
            print(f"Found article for Wikidata ID {wikidata_id} at offset {offset}.")
        else:
            print("Multiple articles found for the given Wikidata ID.")
            print("Please specify the index of the article you want to retrieve.")
            return None
        with ibz2.IndexedBzip2File('enwiki-latest-pages-articles.xml.bz2', parallelization=os.cpu_count()) as reader:
            reader.seek(offset)
            content = None
            for line in reader:
                line = line.decode('utf-8').strip()
                if line == '<page>':
                    content = [line]
                elif line == '</page>':
                    content.append(line)
                    content = '\n'.join(content)
                    return content
                else:
                    if content is not None:
                        content.append(line)
    else:
        print("No article found for the given Wikidata ID.")
        return None


def retrieve_article(wikidata_id):
    content = retrieve_content(wikidata_id)
    cleaner = Cleaner()
    tree = ElementTree.fromstring(content)
    title_elem = tree.find('title')
    text_elem = tree.find('revision/text')
    title = title_elem.text
    text = text_elem.text
    text = cleaner.clean_text(text)
    return title, text


# Example usage
if __name__ == '__main__':
    title, article = retrieve_article('Q101038')
    print(f"The title of the article is: {title}")
    print(article)
