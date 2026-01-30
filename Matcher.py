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
    for hospital in matches:
        if matches[hospital] == -1:
            return hospital
    return -1
