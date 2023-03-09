color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('/Users/amina/Desktop/lab 6/a.txt', "w") as fp:
        for c in color:
                fp.write("%s\n" % c)
print('Done')