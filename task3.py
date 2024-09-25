import nltk
from nltk.stem import PorterStemmer
nltk.download('punkt')

#first part
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


# now files have been seperated into A1-An

# Now making inverted files of each of the abstract files in the folder InvertedAbstract and also stemming the keywords because
# right now they're also not inverted which is needed for this task 




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
        output_file.write(','.join(stemmed_keywords))

    print("Stemmed keywords (with duplicates removed) saved to invertedKeyWords.txt")

# Call the func for keywords stemming
stemkeywords()






