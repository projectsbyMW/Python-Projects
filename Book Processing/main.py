import re
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
 
with open("miracle_in_the_andes.txt",'r', encoding='utf-8') as file:
    book = file.read()

pattern = re.compile("[A-Z]{1}[^.]*[^a-zA-z]love[^a-zA-z][^.]*")
print (len(re.findall(pattern,book)))

pat = re.compile("[a-zA-Z]+")
findings = re.findall(pat,book.lower())

d = {}

for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

d_list = [(value,key) for (key,value) in d.items()]

stop_words = stopwords.words("english")

filtered_words = []

d_list = sorted(d_list,reverse=True)

for n,i in d_list:
    if i not in stop_words:
        filtered_words.append((i,n))
        #print(f"The most used word is {i} and it is used {n} times.")

print(filtered_words[:10])

analyzer = SentimentIntensityAnalyzer()

anazer = re.compile("Chapter [0-9]+")
chapters = re.split(anazer,book)
n = 0
for i in chapters[1:]:
    scores = analyzer.polarity_scores(i)
    n +=1
    if scores["pos"] > scores["neg"]:
        print(f"Chapter {n} is a positive chapter")
    else:
        print(f"Chapter {n} is a negative chapter")