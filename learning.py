# ab_plus_cd.py
import torch
def ab_plus_cd(a, b, c, d,e):
    return a * b + c * d

if __name__ == "__main__":
    # 方式一：手动修改数值
    a, b, c, d = 2, 3, 4, 5
    print(ab_plus_cd(a, b, c, d))
