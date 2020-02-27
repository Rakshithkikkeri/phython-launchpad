number=[1, 1, 2, 3, 4, 64, 35, 93, 35, 87, 4, 3]
duplicate=[]

for i in number:
	if i not in duplicate:
		duplicate.append(i)

print(duplicate)
