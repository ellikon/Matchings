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


def get_h_prime(s):
    h_prime = -1
    for match in matches:
        if matches[match] == s:
            h_prime = match
    return h_prime


def check_student_swap(s, h):
    h_prime = get_h_prime(s)
    if h_prime == -1:
        return True

    return studentPreferences[s].index(h) > studentPreferences[h].index(h_prime)

# while find_unmatched_hospital() != -1:
#     hospital = find_unmatched_hospital()
#     hospitalPreference = hospitalPreferences[hospital-1]
#
#     student = find_next_student(hospital)
#     studentPreferences[student] = studentPreferences[student-1]
#
#     if student not in matches.values():
#         matches[hospital] = student
#     else if
