from builtins import len

import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')

    arr = np.array(list)
    mtx = arr.reshape(3, 3)

    calculations = {
        'mean': [np.mean(mtx, axis=0).tolist(), np.mean(mtx, axis=1).tolist(), np.mean(arr)],
        'variance': [np.var(mtx, axis=0).tolist(), np.var(mtx, axis=1).tolist(), np.var(arr)],
        'standard deviation': [np.std(mtx, axis=0).tolist(), np.std(mtx, axis=1).tolist(), np.std(arr)],
        'max': [np.max(mtx, axis=0).tolist(), np.max(mtx, axis=1).tolist(), np.max(arr)],
        'min': [np.min(mtx, axis=0).tolist(), np.min(mtx, axis=1).tolist(), np.min(arr)],
        'sum': [np.sum(mtx, axis=0).tolist(), np.sum(mtx, axis=1).tolist(), np.sum(arr)]}
    return calculations

# if __name__ == '__main__':
#     print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
