import os
from collections import Counter

with open(r'C:\Users\jense\Desktop\jensen-learns\assessments\week01\results.txt') as f:
    data = f.read().split()
    listy = []
    addy = []
    count_up = 0
    math_right = 0
    reading_right = 0
    science_right = 0
    math_wrong = 0
    reading_wrong = 0
    science_wrong = 0
    for x in data:
        count_up += 1
        if "math" in x:
            if ",c" in x:
                math_right+=1
            elif ",i" in x:
                math_wrong+=1
        elif "reading" in x:
            if ",c" in x:
                reading_right+=1
            elif ",i" in x:
                reading_wrong+=1
        elif "science" in x:
            if ",c" in x:
                science_right+=1
            elif ",i" in x:
                science_wrong+=1

    total_right = math_right + science_right + reading_right
    total_wrong = math_wrong + science_wrong + reading_wrong

    print(f"Overall Accuracy: {(total_right/count_up)*100}% ({total_right}/{count_up})")

    counta = 0
    while counta < 10:
        if math_right == counta:
            print(f"math: {(math_right/(math_right+math_wrong))*100}% ({math_right}/{math_right+math_wrong})")
        elif science_right == counta:
            print(f"science: {(science_right/(science_right+science_wrong))*100}% ({science_right}/{science_right+science_wrong})")
        elif reading_right == counta:
            print(f"reading: {(reading_right/(reading_right+reading_wrong))*100}% ({reading_right}/{reading_right+reading_wrong})")

        counta += 1




    #     if addy == "," or "\n":
    #         print(f"Addy: {addy}")
    #         word = ''.join(addy)
    #         word.replace(r'\n',"")
    #         listy.append(word)
    #         addy =[]
    #         word = ''
    # print(listy)






#We need to parse this list, similarly to the first problem.
#We need to count instances of strings.
#Current issue, is that data is currently a list of single characters... not a list of words.
#Why is this different than the first solution..?
#One path I see forward is to use line breaks and commas as indicators of strings.
#When we run into a comma or a break, we combine the strings up until that point to a list.
