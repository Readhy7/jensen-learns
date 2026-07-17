with open(r'C:\Users\jense\Desktop\jensen-learns\assessments\week01\results.txt') as f:
    data = f.read().split()
    counts={}
    corrects={}
    categories=[]
    verdicts=[]
    for item in data:
        if "," in item:
            # this one just separates the categories and verdicts
            category, verdict = item.split(",")
            categories.append(category)
            verdicts.append(verdict)
            if verdict == 'correct':
                if category not in corrects:
                    corrects[category]=0
                corrects[category]+=1

    for item in categories:
        # this one gives us the total amount of each category, i.e math: 5
        if item not in counts:
            counts[item]=0
        counts[item]+=1

    print(f"Overall accuracy: {sum(corrects.values())/sum(counts.values())*100}% ({sum(corrects.values())}/{sum(counts.values())})")
    for category in sorted(corrects, key=lambda i: corrects[i]/counts[i]):
        print(f"{category}: {corrects[category]/counts[category]*100}% ({corrects[category]}/{counts[category]})")





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
