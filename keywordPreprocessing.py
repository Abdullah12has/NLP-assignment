import nltk
from nltk.corpus import stopwords

# Download the stopwords corpus
nltk.download('stopwords')

# Define the lang
stop_words = set(stopwords.words('english'))

# Read keywords from the file
with open('keywords.txt', 'r') as file:
    keywords = file.read()

# Split the keywords into individual words
words = keywords.split()

filtered_keywords = [word for word in words if word.lower() not in stop_words]

# Join the filtered keywords back into a string
processed_keywords = ', '.join(filtered_keywords)

# Write the processed keywords to a new file
with open('processedKeywords.txt', 'w') as output_file:
    output_file.write(processed_keywords)

print("Processed keywords saved to processedKeywords.txt")
