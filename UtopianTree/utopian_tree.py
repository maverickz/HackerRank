# Enter your code here. Read input from STDIN. Print output to STDOUT
def solution():
    num_test_cases  = input()
    output = []
    for _ in xrange(num_test_cases):
        N = input()
        h = 1
        for i in xrange(N):
            if i%2 == 0:
                h = h * 2
            else:
                h = h + 1
        output.append(h)
    for elem in output:
        print elem

if __name__ == "__main__":
    solution()