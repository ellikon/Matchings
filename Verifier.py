def read_in(path):
    hospitalPreferences = []
    studentPreferences = []

    with open(path, 'r') as file:
        first = file.readline()
        if first == "":
            raise ValueError("INVALID INPUT: empty file")

        first = first.strip()
        if first == "":
            raise ValueError("INVALID INPUT: missing n")

        try:
            n = int(first)
        except ValueError:
            raise ValueError("INVALID INPUT: first line must be an integer n")

        if n < 0:
            raise ValueError("INVALID INPUT: n must be a non negative integer")

        # Hospital preferences
        for i in range(n):
            line = file.readline()
            if line == "":
                raise ValueError(f"INVALID INPUT: missing hospital preference in line {i + 2}")
            hospitalPreferences.append(list(map(int, line.split())))

        #Student preferences
        for i in range(n):
            line = file.readline()
            if line == "":
                raise ValueError(f"INVALID INPUT: missing hospital preference in line {i+n+2}")
            studentPreferences.append(list(map(int, line.split())))

        #Remainder
        rest = file.read().strip()
        if rest != "":
            raise ValueError("INVALID INPUT: extra data after hospital and student preferences")

    #Checking preference lengths
    def is_1_to_n(arr):
        if len(arr) != n:
            return False, f"expected {n} values, got {len(arr)}"
        seen = [False] * (n + 1)
        for x in arr:
            if x < 1 or x > n:
                return False, f"value out of range {x}"
            if seen[x]:
                return False, f"duplicate value {x}"
            seen[x] = True
        return True, ""

    for i in range(n):
        ok, reason = is_1_to_n(hospitalPreferences[i])
        if not ok:
            raise ValueError(f"INVALID INPUT: hospital preference line {i + 1} invalid: {reason}")

    for i in range(n):
        ok, reason = is_1_to_n(studentPreferences[i])
        if not ok:
            raise ValueError(f"INVALID INPUT: student preference line {i + 1} invalid: {reason}")

    return n, hospitalPreferences, studentPreferences



def main():
    input_path = 'data/example.in'
    output = 'data/matching.out'

    try:
        n, hospitalPreferences, studentPreferences = read_in(input_path)
    except ValueError as e:
        print(str(e))
        return

    print(n,hospitalPreferences,studentPreferences)



if __name__ == '__main__':
    main()