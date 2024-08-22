# Retrieve Wikipedia article based on the given Wikidata ID

## To try our tool, please run the following script:
```bash
python3 retrieve_article.py
```

## Potential Issues
**(1) Currently, to avoid the memory issue, the Wikipedia dump is not decompressed. The `indexed_bzip2` package is used to read the Wikipedia dump file so that we can record the offset of each article as same as the normal decompressed file. However, since `indexed_bzip2` is still decompressing the dump file on the fly, for retrieving large amount of articles, we'd better to decompress the bz2 dump completely first. This may need a while of time and a server with enough memory. Fortunately, the indexing we constructed should be useful for the completely decompressed file as well.** 

## Process of Constructing This Tool
**(1) Download the Wikipedia dump from the [Wikipedia Dumps](https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2) page.**

**(2) Install the `wikimapper` package using the following command:**
```bash
pip install wikimapper
```

**(3) Download Wikimapper Index Database from the [Wikimapper Index Database](https://public.ukp.informatik.tu-darmstadt.de/wikimapper/index_enwiki-20190420.db) page.**

And rename the downloaded file to `index_enwiki-latest.db` by running the following command:
```bash
mv index_enwiki-20190420.db index_enwiki-latest.db
```

We can also construct the index database by ourselves, please refer to the [Wikimapper documentation](https://github.com/jcklie/wikimapper) for more details.

**(4) Install `indexed_bzip2` package using the following command:**
```bash
pip install indexed_bzip2
```

**(5) Run the python script `record_offset.py` to build indexing table.**
```bash
python3 record_offset.py
```

This will create two indexing tables `index_table.json` and `wikidata_id_index_table.json`.

The `index_table.json` has the following format, where the key is the title of the Wikipedia article and the value is the offset in the Wikipedia dump file:
```json
{
  "AccessibleComputing": {
        "0": 2253
    },
    "Anarchism": {
        "0": 3146
    }
}
```

The `wikidata_id_index_table.json` has the following format, where the key is the Wikidata ID of the Wikipedia article and the value is the offset in the Wikipedia dump file:
```json
{
    "Q8055": {
        "0": 126704
    },
    "Q101038": {
        "0": 127495
    }
}
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

**(6) Run the python script `retrieve_article.py` to retrieve the Wikipedia article based on the given Wikidata ID.**
```bash
python3 retrieve_article.py
```
