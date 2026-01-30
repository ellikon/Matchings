import random

def generate(n, filename):
    with open(f"../data/{filename}", 'w') as file:
        file.write(str(n) + "\n")
        #hospitals
        for _ in range(n):
            arr = list(range(1,n+1))
            random.shuffle(arr)
            file.write(" ".join(map(str, arr)) + "\n")
        #students
        for _ in range(n):
            arr = list(range(1,n+1))
            random.shuffle(arr)
            file.write(" ".join(map(str, arr)) + "\n")


if __name__ == '__main__':
    checks = [1,2,4,8,16,32,64,128,256,512]
    for n in checks:
        generate(n, f"test_{n}.in")