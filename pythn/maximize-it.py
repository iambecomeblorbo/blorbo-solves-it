# Enter your code here. Read input from STDIN. Print output to STDOUT

def take_first_line():
    K, M = list(map(int, input().split()))
    return K, M

def take_second_line():
    parts = list(map(int, input().split()))
    N_i, integers = parts[0], parts[1:]
    return N_i, integers


def calculate_S_max():
    K, M = take_first_line()
    squares_map = make_map(K)

    possible_S_vals = {0}
    num_lists = len(squares_map)
    for k in range(num_lists):
        new_set = set()
        vals = squares_map[k]

        # prev := S_vals from previous list
        for prev in possible_S_vals:
            for v in vals:
                new_set.add((prev + v) % M)

        possible_S_vals = new_set
        print(possible_S_vals)
    return max(possible_S_vals)


def make_map(K):
    k = 0
    map = {}
    while k < K:
        N_i, integers = take_second_line()
        if len(integers) == N_i:
            map[k] = [(i*i) for i in integers]
        else:
            print("does not match")
        k += 1
    return map


print(calculate_S_max())

'''
Sample Input

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 

Sample Output

206

python3 maximize-it.py < inputs/maximize-it.txt | cat
'''