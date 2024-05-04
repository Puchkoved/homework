students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
mid={' ':0}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students=list(students)
students.sort()
for i in students:
    m=students.index(i)
    mid[i]=round(sum(grades[m])/len(grades[m]),2)
del mid[' ']
print(mid)








