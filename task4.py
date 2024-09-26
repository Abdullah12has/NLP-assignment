import os
import difflib

# check similarity
def is_similar(word1, word2, threshold=0.9):
    similarity = difflib.SequenceMatcher(None, word1, word2).ratio()
    return similarity >= threshold

# Function to compare keywords
def search_keywords_in_abstract(abstract_file, keyword_file):
    # Read the abstract
    with open(abstract_file, 'r') as file:
        abstract = file.read()

    # Tokenize 
    abstract_words = abstract.split()

    # Read  keywords
    with open(keyword_file, 'r') as file:
        keywords = file.read().split(', ')

    # Dictionary
    matched_results = {}

    # Iterate over each keyword
    for keyword in keywords:
        matched_results[keyword] = []  # Initialize with an empty list for each keyword
        for word in abstract_words:
            if is_similar(keyword.lower(), word.lower()):
                matched_results[keyword].append(word)

    # Display the result
    print(f"\nMatching Results for Abstract ({abstract_file}):\n")
    for keyword, matched_words in matched_results.items():
        if matched_words:
            print(f"Keyword '{keyword}' matched with: {', '.join(matched_words)}")
        else:
            print(f"Keyword '{keyword}' did not match any word in the abstract.")
    print("\n")


abstracts_dir = "Abstracts"


keyword_file = 'invertedKeyWords.txt'

# Loop through each abstract file in the directory and perform relaxed matching
for filename in os.listdir(abstracts_dir):
    if filename.endswith(".txt"):
        file_path = os.path.join(abstracts_dir, filename)
        search_keywords_in_abstract(file_path, keyword_file)
