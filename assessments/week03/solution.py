with open(r'C:\Users\jense\Desktop\jensen-learns\assessments\week03\results.txt') as data:
    f = data.read().split()
    totals={}
    results={}
    for item in f:
        if "," in item:
            modality,result = item.split(",")
            if result == "resolved":
                if modality not in results:
                    results[modality]=0
                results[modality]+=1
            if modality not in totals:
                totals[modality]=0
            totals[modality]+=1

print(f'Overall resolution rate: {sum(results.values())/sum(totals.values())*100}% ({sum(results.values())}/{sum(totals.values())})')
for modality in sorted(results, key = lambda i: results[i]/totals[i]):
    print(f'{modality}: {results[modality]/totals[modality]*100}% ({results[modality]}/{totals[modality]})')





# #
# ```
# Overall resolution rate: 50.0% (11/22)
# phone: 60.0% (6/10)
# email: 25.0% (2/8)
# chat: 75.0% (3/4)
# ```
