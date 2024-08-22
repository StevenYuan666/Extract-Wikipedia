# Extract Wikipedia page based on the Given Wikidata ID

## This solution is not quite useful due to the outdated version of wikiextractor package.
## It is not updated for more than 1 year and cannot work with the latest version of the Wikipedia dump.

## Process of Constructing This Tool
### 1. Extract All Articles from the Wikipedia Dump
**(a) Download the Wikipedia dump from the [Wikipedia Dumps](https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2) page.**

**(b) Install the `wikiextractor` package using the following command:**
```bash
pip install wikiextractor
```

**(c) Create a directory named `extracted_files` in the root directory of the project.**
```bash
mkdir extracted_files
```

**(d) Extract the Wikipedia dump using the following command:**
```bash
python -m wikiextractor.WikiExtractor enwiki-latest-pages-articles.xml.bz2 -o ./extracted_files/ --json --links
```

This will save the extracted files in the `extracted_files` directory with the following JSON format and preserve the links:
```json
{"id": "", "revid": "", "url": "", "title": "", "text": "..."}
```

### 2. Construct the Indexing Table
**(a) Install Wikimapper**
```bash
pip install wikimapper
```

**(b) Download Wikimapper Index Database from the [Wikimapper Index Database](https://public.ukp.informatik.tu-darmstadt.de/wikimapper/index_enwiki-20190420.db) page.**

**(c) Run the python script `index_wikipedia_id.py` to create the index table.**
```bash
python index_wikipedia_id.py
```

This will create an index table with the following format:
```json
{
  "WIKIDATA_ID": {
    "folder": "", 
    "file": "", 
    "offset": ""
  }
}
```

