# auto arrange name
write = None
filename = 'names.txt'  # input("Enter file name(with file extension): ")
while True:
    try:
        fh = open(filename, 'rt')
        break
    except Exception:
        print('Error: File not found!\nTry again.')
        filename = input("Enter file name(with extension): ")
        continue
names = []
for line in fh:
    names.append(line.strip())
names.sort()

print(names)
print('\nYour names has been sorted in ascending order.')
with open('sorted_' + filename, 'wt') as f:
    f.write('Sorted list of names.\n')
    for name in names:
        f.write(name + '\n')
print("Check 'sorted_" + filename + "'\nBye..")
exit()
