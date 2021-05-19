#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = list(map(float, input("Введите список:").split()))
    k =0
    for i in enumerate(a, 0):
        if i[1] < 0:
            n = i[0]
            k += 1
            if k == 1:
                j = n
            if k == 2:
                b = a[j+1:n]
    c = sum(b)
    print("Сумма элементов между 1 и 2 отрицательными элементами:", c)
    f = str(sorted(a, key=lambda x: abs(x)))
    print("Преобразованный список:", f)













