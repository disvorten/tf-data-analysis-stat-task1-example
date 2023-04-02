import pandas as pd
import numpy as np

chat_id = 1109095907  # Ваш chat ID, не меняйте название переменной

np.random.seed(40)


# 0.5942192924577453
def solution(x: np.array) -> float:
    t = 58
    beta = x.mean()
    disp = 0
    for i in range(x.shape[0]):
        disp += (x[i] - beta) ** 2
    disp /= x.shape[0] - 1
    alpha_1 = np.sqrt(2 / disp)
    acc_1 = 2 * alpha_1 / t ** 2
    av_2 = 0
    for i in range(x.shape[0]):
        av_2 += x[i] ** 2
    av_2 /= x.shape[0]
    alpha = np.sqrt(2 / (av_2 - beta ** 2))
    acc_2 = 2 * alpha / t ** 2
    return acc_2


# if __name__ == '__main__':
    # loc = 0
    # scale = 10
    # sample_size = 1000
    # var = np.random.laplace(loc, scale, sample_size)
    # print(solution(np.array(var)))
