with open(r'C:\Users\jense\Desktop\jensen-learns\assessments\week04\deals.txt') as f:
    data = f.read().split()
    reps={}
    sales={}
    for item in data:
        if "," in item:
            rep,k=item.split(",")
            dealsize=int(k)
            print(rep,dealsize)
            if rep not in reps:
                reps[rep]=0
            reps[rep]+=dealsize
            if rep not in sales:
                sales[rep]=0
            sales[rep]+=1

print(f'Overall average deal size: ${sum(reps.values())/sum(sales.values())} ({sum(reps.values())}/{sum(sales.values())} sales)')
for rep in sorted(sales, key = lambda i: reps[i]/sales[i], reverse=True):
    print(f'{rep}: ${reps[rep]/sales[rep]} (${reps[rep]}/{sales[rep]} sales)')

# ```

# Overall average deal size: 2400.0 (24000/10)
# bob: 1000.0 (5000/5)
# alice: 5000.0 (10000/2)
# carol: 3000.0 (9000/3)
# ```

#We have reps with dealsizes.
#Reps are the key to a dict.
#Can we reference the value of a dict, inside a dict? That's my attempt to solve here:
#AKA, we can create a dict of quantity of $X deal sizes that BOB has made, and give it it's own dict, scaleable through the rep dict.
#So, to start, we get the rep dict.
#Then, we take the values in the rep dict and run them through the data.
#When we encounter a new $ result, we create a new dict based on rep name.
#but how do you create variables like this iteratively - can you? If not, we'll need a way around.
#I don't think we can do that.
#there's probably tooling I'm not aware of.

#Ok, when I average something, I take the sum and divide it by the occurences.
#So I don't need separate values - i just need How many entries does Bob have, and what the total amount was.
