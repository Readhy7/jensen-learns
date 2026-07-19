with open(r'C:\Users\jense\Desktop\jensen-learns\assessments\week01\results.txt') as f:
    data = f.read().split()
    counts={}
    corrects={}
    for item in data:
        if "," in item:
            category, verdict = item.split(",")
            if verdict == 'correct':
                if category not in corrects:
                    corrects[category]=0
                corrects[category]+=1
            if category not in counts:
                counts[category]=0
            counts[category]+=1

    print(f"Overall accuracy: {sum(corrects.values())/sum(counts.values())*100}% ({sum(corrects.values())}/{sum(counts.values())})")
    for category in sorted(corrects, key=lambda i: corrects[i]/counts[i]):
        print(f"{category}: {corrects[category]/counts[category]*100}% ({corrects[category]}/{counts[category]})")
