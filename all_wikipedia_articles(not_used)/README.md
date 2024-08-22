# Retrieve Wikipedia article based on the given Wikidata ID
## To try our tool, please run the following script:
```bash
python retrieve_wikipedia_article.py
```



## Process of Constructing This Tool
**(1) Download the Wikipedia dump from the [Wikipedia Dumps](https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2) page.**

**(2) Install the `wikimapper` package using the following command:**
```bash
pip install wikimapper
```

**(3) Download Wikimapper Index Database from the [Wikimapper Index Database](https://public.ukp.informatik.tu-darmstadt.de/wikimapper/index_enwiki-20190420.db) page.**

**(4) Run the python script `extract_all_articles.py` to extract all articles from the Wikipedia dump and build indexing table.**
```bash
python extract_all_articles.py
```

The Wikipedia XML dump has the following structure:
```xml
<mediawiki>
  <page>
    <ns>0</ns>
    <title>Page title</title>
    <text>Wikipedia source for page text</text>
  </page>
    ...
</mediawiki>
```
where `<ns>` is the namespace of the page, `<title>` is the title of the page, and `<text>` is the source text of the page.

We only keep the articles with namespace 0 (main articles) and ignore the other pages such as user pages, talk pages, etc.

Please see the details of namespace in the [Wikipedia documentation](https://en.wikipedia.org/wiki/Wikipedia:Namespace).

The indexing table has the following format:
```json
{
  "WIKIDATA_ID": {
    "folder": "Folder name",
    "file": "File name",
    "offset": "Offset in the file"
  }
}
```