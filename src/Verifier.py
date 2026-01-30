path_in = '../data/test_512.in'
path_out = '../data/matchings_512.out'


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

def read_match(path, n):
    matches = {}

    with open(path, 'r') as file:
        lines = [ln.strip() for ln in file.readlines() if ln.strip() != ""]

    if len(lines) != n:
        raise ValueError(f"INVALID: expected {n} matching lines and got {len(lines)}")

    seenH = set()
    seenS = set()

    for idx, ln in enumerate(lines, start = 1):
        parts = ln.split()
        if len(parts) != 2:
            raise ValueError(f"INVALID: line {idx} should have 2 integers")

        try:
            h = int(parts[0])
            s = int(parts[1])
        except ValueError:
            raise ValueError(f"INVALID: line {idx} contains non integer values")

        if not (1 <=h <= n and 1 <= s <= n):
            raise ValueError(f"INVALID: line {idx} has out-of-range value (h={h}, s={s})")

        if h in seenH:
            raise ValueError(f"INVALID: duplicate hospital {h}")
        if s in seenS:
            raise ValueError(f"INVALID: duplicate student {s}")


        seenH.add(h)
        seenS.add(s)
        matches[h] = s

    if len(seenH) != n:
        raise ValueError("INVALID: not all hospitals appear exactly once")
    if len(seenS) != n:
        raise ValueError("INVALID: not all students appear exactly once")

    return matches

def stability(matches, hospitalPreferences, studentPreferences, n):
    student_to_hospital = {}
    for h in matches:
        student_to_hospital[matches[h]] = h
    #Student rank of hospitals
    rankS = [[0] * (n + 1) for _ in range(n + 1)]
    for s in range(1, n + 1):
        for pos, h in enumerate(studentPreferences[s - 1]):
            rankS[s][h] = pos
    #Hospital rank of student
    rankH = [[0] * (n + 1) for _ in range(n + 1)]
    for h in range(1, n + 1):
        for pos, s in enumerate(hospitalPreferences[h - 1]):
            rankH[h][s] = pos

    for h in range(1, n + 1):
        assigned_s = matches[h]
        # Check students that h prefers more than student matched
        for s in hospitalPreferences[h - 1]:
            if s == assigned_s:
                break  # Reached matched student, everyone after is worse
            assigned_h_of_s = student_to_hospital[s]
            if rankS[s][h] < rankS[s][assigned_h_of_s]:
                return False, f"blocking pair ({h}, {s})"

    return True, ""



def main():
    import time

    start = time.perf_counter()
    try:
        n, hospitalPreferences, studentPreferences = read_in(path_in)
    except ValueError as e:
        print(str(e))
        return
    except Exception:
        print("INVALID: cannot open/read input file")
        return

    try:
        matches = read_match(path_out, n)
    except ValueError as e:
        print(str(e))
        return
    except Exception:
        print("INVALID: cannot open/read matching file")
        return

    stable, reason = stability(matches, hospitalPreferences, studentPreferences, n)
    if not stable:
        print(f"UNSTABLE: {reason}")
        return

    print("VALID STABLE")
    end = time.perf_counter()

    print(f"Verifier runtime: {(end - start)*1000:.3f} ms")


if __name__ == '__main__':
    main()