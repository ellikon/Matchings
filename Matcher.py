hospitalPreferences = []
studentPreferences = []

with open('data/example.in', 'r') as file:
    n = int(file.readline().strip())
    for i in range(n):
        hospitalPreferences.append(list(map(int, file.readline().split())))
    for i in range(n):
        studentPreferences.append(list(map(int, file.readline().split())))

matches = {}

for i in range(n):
    matches[i + 1] = -1


def find_unmatched_hospital():
    for h in matches:
        if matches[h] == -1:
            return h
    return -1


previousMatches = []


def find_next_student(h):
    for s in hospitalPreferences[h - 1]:
        if [h, s] not in previousMatches:
            return s
    return -1
