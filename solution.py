import pandas as pd
import numpy as np

chat_id = 1109095907  # Ваш chat ID, не меняйте название переменной


def solution(x: np.array) -> float:
    t = 58
    x_av = x.mean()
    all = [x[i] ** 2 for i in range(x.shape[0])]
    qv = sum(all) / x.shape[0]
    res = (x_av * 2) / t ** 2
    res = (np.sqrt(qv - 2) * 2) / t ** 2
    return res


