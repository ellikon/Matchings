path_in = '../data/test_512.in'
path_out = '../data/matchings_512.out'

import time

hospitalPreferences = []
studentPreferences = []

with open(path_in, 'r') as file:
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
    for m in matches:
        if matches[m] == s:
            return m
    return -1


def check_student_swap(s, h):
    h_prime = get_h_prime(s)
    if h_prime == -1:
        return True

    return studentPreferences[s - 1].index(h) < studentPreferences[s - 1].index(h_prime)

start = time.perf_counter()

while find_unmatched_hospital() != -1:
    hospital = find_unmatched_hospital()
    student = find_next_student(hospital)
    if student not in matches.values():
        matches[hospital] = student
    elif check_student_swap(student, hospital):
        hospital_prime = get_h_prime(student)
        matches[hospital] = student
        matches[hospital_prime] = -1

    previousMatches.append([hospital, student])

end = time.perf_counter()

with open(path_out, 'w') as file:
    for match in matches:
        file.write(f"{match} {matches[match]}\n")

print("Number of Proposals Made: ", len(previousMatches))
print()
print("Final Matching:")
for match in matches:
    print(match, matches[match])
print(f"Matcher runtime: {(end - start)*1000:.3f} ms")
