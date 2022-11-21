students = [('John', 'A', 25), ('Mike', "C", 19),
            ('Mike', "B", 12), ('Mike', 'C', 18),
            ('Bom', 'D', 10), ('Mike', 'D', 19)]

stuA = students.copy()
stuA.sort()
print(stuA)


def myKey(students):
    return lambda x: x[2] % 10


stuB = sorted(students, key=myKey)
print(stuB)
