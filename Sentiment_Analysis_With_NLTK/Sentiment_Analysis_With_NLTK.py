import string
from collections import Counter

import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# reading text file
text = open('read.txt', encoding='utf-8').read()


# converting to lowercase
lower_case = text.lower()

# Removing Punctuations
# str1 Specifies the list of characters that need to be replaced.
# str2 Specifies the list of characters with which the characters need to be replaced.
# str3 Specifies the list of characters that needs to be deleted.
# Returns : Returns the translation table which specifies the conversions that can be used
clean_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Tokenization of the words using NLTK Library
tokenized_words = word_tokenize(clean_text,"english")

# we are using the built in stop words in NLTK library

# removing stop words
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

print(final_words)

# NLP Emotion Algorithm
# 1) Check if the word in the final word list is also present in emotion .txt
# - open the emotion file
# - Loop through each line and clear it
# - Extract the word and emotion using split
# 2) If word is present - > Add the emotion to emotion list
# 3) Finally count each emotion in the emotion list


emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        # clearing the new line,comma,colon and extra spaces before the word for cleaner line
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        # extracting word and emotion by splitting based on colon
        word, emotion = clear_line.split(':')
        # checking for the word presence in the final words
        if word in final_words:
            emotion_list.append(emotion)


# it automatically creates a dictionary of the emotion word with its frequency
count = Counter(emotion_list)
print(count)

def sentinment_anlayse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("Negative Vibe")
    elif pos > neg:
        print("Postive Vibe")
    else:
        print("Neutral Vibe")

sentinment_anlayse(clean_text)
# graph to show the analysis in a more better way
fig , axl = plt.subplots()
axl.bar(count.keys(),count.values())
fig.autofmt_xdate()
plt.title('Sentiment Analysis')
plt.savefig('SentimentGraph.png')
plt.show()