import nltk
import os
from nltk.stem import PorterStemmer
nltk.download('punkt')
import nltk
from nltk.corpus import stopwords
from collections import defaultdict

nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('stopwords')


def seperatefiles():

    # Read abstracts from the file
    with open('abstracts.txt', 'r') as file:
        abstracts = file.read()

    #seperate the abstracts
    abstract_list = abstracts.split('\n\n')


    for i, abstract in enumerate(abstract_list, start=1):
        filename = f"A{i}.txt"


        with open("Abstracts/"+filename, 'w') as output_file:
            output_file.write(abstract)
        print(filename)


# now files have been seperated 




# Function to stem keywords and remove duplicates
def stemkeywords():
    # Initialize Porter Stemmer
    stemmer = PorterStemmer()

    # Read keywords from the processedKeywords.txt file
    with open('processedKeywords.txt', 'r') as file:
        keywords = file.read()

    # Split the keywords (assuming they are separated by commas or spaces)
    keyword_list = keywords.split(', ')

    # Remove duplicates by converting the list to a set
    uniq_keywords = set(keyword_list)

    # Stem each unique keyword
    stemmed_keywords = [stemmer.stem(keyword) for keyword in uniq_keywords]

    # Write the stemmed keywords to invertedKeyWords.txt
    with open('invertedKeyWords.txt', 'w') as output_file:
        output_file.write(', '.join(stemmed_keywords))

    print("Stemmed keywords (with duplicates removed) saved to invertedKeyWords.txt")


def make_inverted_abstract_file():
    # will read all the words from all the files and clean them and then save them in a new abstract inverted file
    stemmer = PorterStemmer()
    stop_words = set(nltk.corpus.stopwords.words('english'))
    inverted_index = defaultdict(set)
    abstracts_dir = "Abstracts"

    for filename in os.listdir(abstracts_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(abstracts_dir, filename)

            # Read the content of the abstract file
            with open(file_path, 'r') as file:
                abstract = file.read()

            # Tokenize the abstract into words
            words = nltk.word_tokenize(abstract)

            # Filter out stopwords and non-alphabetic tokens, and stem the remaining words
            for word in words:
                word = word.lower()  # Convert to lowercase
                if word.isalpha() and word not in stop_words:
                    stemmed_word = stemmer.stem(word)  # Stem the word
                    inverted_index[stemmed_word].add(os.path.splitext(filename)[0])  # Add file to the inverted index without .txt

    with open("inverted_abstracts.txt", 'w') as output_file:
        for word, files in inverted_index.items():
            output_file.write(f"{word}: {', '.join(files)}\n")

    print("Inverted index saved to inverted_abstracts.txt")














# to make the 20 files
# seperatefiles()
# Call the func for keywords stemming
# stemkeywords()
make_inverted_abstract_file()






