print("List Duplicates")
dups = [11,11,23,44,44,2344]
noDupes = []

for num in dups:
    if num not in noDupes:
        noDupes.append(num)

print(noDupes)

