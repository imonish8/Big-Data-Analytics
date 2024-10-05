favColors = {
    'Arham' : 'Blue',
    'Lisa' : 'Yellow',
    'Vinod' : 'Purple',
    'Jenny' : 'Pink'
    }

lengthOfStudent = len(favColors.keys())
print(lengthOfStudent) # 4
print()
favColors['Lisa'] = 'Orange'
print(favColors) #yellow  to orange
print()
del favColors['Jenny']
print(favColors)
print()
sorted_students = sorted(favColors.items())
print(sorted_students)
print()
