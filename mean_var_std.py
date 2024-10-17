import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(list).reshape(3, 3)

    mean = [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr.mean().tolist()]
    variance = [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr.var().tolist()]
    std_dev = [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), arr.std().tolist()]
    max_val = [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr.max().tolist()]
    min_val = [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr.min().tolist()]
    sum_val = [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr.sum().tolist()]
    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }
    return calculations