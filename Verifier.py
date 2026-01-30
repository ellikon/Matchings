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


