with open(r'C:\Users\jense\Desktop\jensen-learns\assessments\week02\results.txt') as f:
    data = f.read().split()
    totals={}
    enrollment_status={}
    for item in data:
        if "," in item:
            program,status=item.split(",")
            if status == "enrolled":
                if program not in enrollment_status:
                    enrollment_status[program]=0
                enrollment_status[program]+=1
            if program not in totals:
                totals[program]=0
            totals[program]+=1

    print(f'Overall enrollment rate: {sum(enrollment_status.values())/sum(totals.values())*100}% ({sum(enrollment_status.values())}/{sum(totals.values())})')
    for program in sorted(enrollment_status, key = lambda i: enrollment_status[i]/totals[i]):
        print(f'{program}: {(enrollment_status[program]/totals[program])*100}% ({enrollment_status[program]}/{totals[program]})')


# #```
# Overall enrollment rate: 60.0% (12/20)
# business: 60.0% (6/10)
# nursing: 75.0% (3/4)
# data-science: 50.0% (3/6)
# ```
