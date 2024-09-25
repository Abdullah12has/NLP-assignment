import requests
from bs4 import BeautifulSoup

# Array of URLs to scrape
urls = [
    "https://www.nature.com/articles/s41467-024-51438-y",
    "https://www.nature.com/articles/s41592-024-02418-z",
    "https://www.nature.com/articles/s41564-024-01791-x",
    "https://www.nature.com/articles/s41467-024-51771-2",
    "https://www.nature.com/articles/s41467-024-52060-8",
    "https://www.nature.com/articles/s41467-024-52263-z",
    "https://www.nature.com/articles/s43588-024-00700-w",
    "https://www.nature.com/articles/s41550-024-02322-8",
    "https://www.nature.com/articles/s41467-024-51433-3",
    "https://www.nature.com/articles/s43588-024-00679-4",
    "https://www.nature.com/articles/s42256-024-00883-x",
    "https://www.nature.com/articles/s41467-024-51260-6",
    "https://www.nature.com/articles/s41467-024-50911-y",
    "https://www.nature.com/articles/s41591-024-03166-5",
    "https://www.nature.com/articles/s41586-024-07711-7",
    "https://www.nature.com/articles/s41467-024-51511-6",
    "https://www.nature.com/articles/s41467-024-50334-9",
    "https://www.nature.com/articles/s41598-024-71245-1",
    "https://www.nature.com/articles/s41551-024-01243-1",
    "https://www.nature.com/articles/s41467-024-52491-3"

]

# Loop through each URL
for url in urls:
    # Send a GET request to the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the webpage content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the abstract
        abstract_section = soup.find('div', {'class': 'c-article-section__content'})
        if abstract_section:
            abstract = abstract_section.get_text(strip=True)
            # Append abstract to abstracts.txt
            with open('abstracts.txt', 'a') as abstract_file:
                # abstract_file.write(f"URL: {url}\n")
                abstract_file.write(abstract + '\n\n')
            print(f"Abstract saved to abstracts.txt for {url}")
        else:
            print(f"Abstract not found for {url}")

        # Extract the title and save it to keywords.txt
        title_section = soup.find('h1', {'class': 'c-article-title'})
        if title_section:
            title = title_section.get_text(strip=True)
            # Append title to keywords.txt
            with open('keywords.txt', 'a') as keywords_file:
                # keywords_file.write(f"URL: {url}\n")
                keywords_file.write(title + '\n\n')
            print(f"Title saved to keywords.txt for {url}")
        else:
            print(f"Title not found for {url}")
    else:
        print(f"Failed to retrieve the article at {url}. Status code: {response.status_code}")
