

with open('processedKeywords.txt', 'r') as file:
    keywords = file.read()

with open('abstracts.txt', 'r') as file:
    abstract = file.read().lower()


selectedWords = list()

# dic = dict()

for i in range(5):
    selectedWords.append(keywords.split(', ')[i])



# tells which words are being matched and which are not being matched
for word in selectedWords:
    if word in abstract:
        print(word+":1")
    else:
        print(word+":0")










