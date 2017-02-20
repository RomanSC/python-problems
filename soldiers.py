"""
"""
import itertools

def permutations(n):
    perms_list = list(itertools.permutations([x for x in range(1, n + 1)]))
    new_perms_list = []

    for i in perms_list:
        new_perms_list.append(list(i))
        perms_list = new_perms_list

    return perms_list

def gen_grid(n_list):
    pass

def main():
    n = 3
    perms_list = permutations(n)
    print(perms_list)

if __name__ == '__main__':
    main()
