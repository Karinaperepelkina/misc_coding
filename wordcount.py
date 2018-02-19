
#9

file = open('./Alexa.txt', 'r')
wordCount = {}

for word in file.read().split():
    if word not in wordCount:
        wordCount[word] = 1
    else:
        wordCount[word] += 1
        
num =(sorted(wordCount.items(), key=lambda t: t[1], reverse=True))


for k, v in num:
    print(k, v)
