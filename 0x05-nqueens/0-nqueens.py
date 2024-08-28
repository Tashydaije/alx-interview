#!/usr/bin/python3
''' N queens '''
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)
if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)
if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def pqueens(n, i=0, a=[], b=[], c=[]):
    ''' Find the possible positions '''
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from pqueens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solution(n):
    ''' solve '''
    sol = []
    i = 0
    for solutions in pqueens(n, 0):
        for s in solutions:
            sol.append([i, s])
            i += 1
        print(sol)
        sol = []
        i = 0


solution(n)
