import requests


def get_wikipedia_article(wikidata_id, language='en'):
    """
    Fetches the full text of a Wikipedia article corresponding to a given Wikidata item ID.

    Parameters:
    wikidata_id (str): The Wikidata item ID (e.g., 'Q42' for Douglas Adams).
    language (str): The language of the Wikipedia article (default is 'en' for English).

    Returns:
    str: The full text of the Wikipedia article in the specified language.
    """
    # Construct the URL to access the Wikidata API
    url = f"https://www.wikidata.org/wiki/Special:EntityData/{wikidata_id}.json"

    # Make a request to the Wikidata API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        entities = data['entities']
        if wikidata_id in entities:
            sitelinks = entities[wikidata_id]['sitelinks']
            if f'{language}wiki' in sitelinks:
                # Extract the Wikipedia page title
                page_title = sitelinks[f'{language}wiki']['title'].replace(' ', '_')

                # Construct the URL to access the Wikipedia API for full page content
                wiki_api_url = f"https://{language}.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&titles={page_title}&explaintext=1"

                # Make a request to the Wikipedia API
                wiki_response = requests.get(wiki_api_url)

                if wiki_response.status_code == 200:
                    wiki_data = wiki_response.json()
                    pages = wiki_data['query']['pages']
                    page = next(iter(pages.values()))  # Get the first (and only) page
                    return page.get('extract', 'No content available.')
                else:
                    print(f"Failed to retrieve Wikipedia page content: {wiki_response.status_code}")
                    return "No content available."
            else:
                print(f"No Wikipedia article found in {language} for Wikidata ID {wikidata_id}.")
                return "No content available."
        else:
            print(f"Wikidata ID {wikidata_id} not found.")
            return "No content available."
    else:
        print(f"Failed to retrieve data from Wikidata: {response.status_code}")
        return "No content available."


# Example usage
if __name__ == '__main__':
    wikidata_id = 'Q42'  # Example: Q42 is the Wikidata ID for Douglas Adams
    article_text = get_wikipedia_article(wikidata_id)
    print(article_text)
