import numpy as np

systems = {
    '1':
        {
            'A': np.array([[2, 1, 1, 1, 1], [1, 2, 1, 1, 1], [1, 1,2, 1, 1], [1, 1, 1, 2, 1] ,[1, 1, 1, 1, 2]]),
            'b': np.array([4, 5, 6, 7, 8])
        },
    '2':
        {
            'A': np.array([[0, 3, -6, 6, 4],[3, -7, 8, -5, 8], [3, -9, 12, -9, 6]]),
            'b': np.array([-5, 9, 15])
        },
}


def solve(A, b):
    A_inv = np.linalg.inv(A)
    return np.dot(A_inv, b)

def penrose_solve(A, b):
    A_inv = np.linalg.pinv(A)
    return np.dot(A_inv, b)

def main():
    print(solve(systems['1']['A'], systems['1']['b']))
    print(penrose_solve(systems['2']['A'], systems['2']['b']))

if __name__ == '__main__':
    main()