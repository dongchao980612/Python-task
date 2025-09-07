
# -*- coding: utf-8 -*-
# Time    : 2025/8/25 9:59
# File    : Testing01.py
# Software: PyCharm

import numpy as np


def conv1d(x, w, p=0, s=1):
    # [::-1]
    w_rot = np.array(w[::-1])# 转置
    x_padded = np.array(x)
    if p > 0:
        zero_pad = np.zeros(shape=p)
        x_padded = np.concatenate([zero_pad, x_padded, zero_pad])# 拼接

    res = []
    for i in range(0, int((len(x_padded) - len(w_rot))) + 1, s):
        # print(x_padded[i:i + w_rot.shape[0]],w_rot)
        res.append(np.sum(x_padded[i:i + w_rot.shape[0]] * w_rot))
    return np.array(res)


if __name__ == '__main__':
    # Testing
    x = [1, 3, 2, 4, 5, 6, 1, 3]
    w = [1, 0, 3, 1, 2]
    print('Conv1d Implementation:', conv1d(x, w, p=2, s=1))
    # Conv1d Implementation: [ 5. 14. 16. 26. 24. 34. 19. 22.]
    print('NumPy Results:', np.convolve(x, w, mode='same'))
    # NumPy Results: [ 5 14 16 26 24 34 19 22]
