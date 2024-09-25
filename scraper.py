import requests
from bs4 import BeautifulSoup

# URL of the article to scrape
url = "https://www.nature.com/articles/s41467-024-51438-y"

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
            abstract_file.write(abstract + '\n\n')
        print("Abstract saved to abstracts.txt")
    else:
        print("Abstract not found.")

    # Extract the title and save it to keywords.txt
    title_section = soup.find('h1', {'class': 'c-article-title'})
    if title_section:
        title = title_section.get_text(strip=True)
        # Append title to keywords.txt
        with open('keywords.txt', 'a') as keywords_file:
            keywords_file.write(title + '\n\n')
        print("Title saved to keywords.txt")
    else:
        print("Title not found.")
else:
    print(f"Failed to retrieve the article. Status code: {response.status_code}")
