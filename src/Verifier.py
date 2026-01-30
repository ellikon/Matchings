def read_intstance(path):
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
            if line == "":
                raise ValueError(f"INVALID INPUT: missing hospital preference in line {i+n+2}")
            studentPreferences.append(list(map(int, line.split())))

        #Remainder
        rest = file.read().strip()
        if rest != "":
            raise ValueError("INVALID INPUT: extra data after hospital and student preferences")

