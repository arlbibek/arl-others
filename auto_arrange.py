# auto arrange name
filename = 'names.txt'  # input("Enter file name(with file extension): ")
while True:
    try:
        fh = open(filename, 'rt')
        break
    except Exception:
        print("Error: Ccouldn't locate {} \nTry again.".format(filename))
        filename = input("Enter file name(with extension): ")
        continue
    except KeyboardInterrupt: exit("Abort!")
names = list()
for line in fh:
    names.append(line.strip())
names.sort()

with open('sorted_' + filename, 'wt') as f:
    f.write('Sorted list of names.\n')
    for name in names:
        f.write(name + '\n')
print(names)
print('\nYour names has been sorted in ascending order.')
print("Check 'sorted_" + filename)
exit('Bye..')
