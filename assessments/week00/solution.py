#this code is used to count the top words in a file.

import os
import re
import array

print(os.getcwd())

with open(r'C:\Users\jense\Desktop\jensen-learns\assessments\week00\sample.txt') as f:
    data = f.read()
    print(data)
    newcase = data.lower()
    newcases = re.sub(r'[.,\\/#!$%\^&\*;:{}=\-_`~()]', '', newcase)
    words = newcases.split()
    count = 0
    eachword = 0
    uniques = []
    count += len(words)
    finallist = ""
    finalcount = []
    for x in words:
        UniqueWord = words[eachword]
        if UniqueWord in uniques:
            eachword+=1
        else:
            uniques.append(words[eachword])
            eachword+=1
    wordcounter = 0
    for y in uniques:
        for z in words:
            if y == z:
                wordcounter += 1
            else:
                wordcounter +=0
        finalcount.append(wordcounter)
        wordcounter = 0

    finallist2 = (sorted(range(len(finalcount)), key=lambda i: finalcount[i])[-5:])
    finallist = list(reversed(finallist2))

    print("'''")
    counta = 0
    for item in finallist:
        print(uniques[item], "= ", finalcount[item])
        counta+=1
    print("'''")

# ## Expected output for sample.txt (Parts 1–2)
# ```
# the: 7
# sales: 4
# model: 3
# data: 2
# evaluation: 2
# ```

# If your output matches, Parts 1–2 are correct.



#take a look at a word - if we already have that word saved, we add it to that words count.
#for each word in the file, we check to see if we already have the word. so we need a list with the words we find.
#to make that list, we need to iterate through each word in the file.
#each iteration needs to check the list. if the list does not contain that word, we add the word to the list.
#we also create a variable that contains the numerical value of that word - so if we detect "the", the first time, we create WordCounter1 = 1 or something.
#




