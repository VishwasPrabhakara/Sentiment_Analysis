import string
from collections import Counter
import matplotlib.pyplot as plt
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

# Tokenization of the words
tokenized_words = clean_text.split()

# words that do not add any meaning to the sentence in NLP are called stop words
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# removing stop words
final_words = []
for word in tokenized_words:
    if word not in stop_words:
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

# graph to show the analysis in a more better way
fig , axl = plt.subplots()
axl.bar(count.keys(),count.values())
fig.autofmt_xdate()
plt.title('Sentiment Analysis')
plt.savefig('SentimentGraph.png')
plt.show()