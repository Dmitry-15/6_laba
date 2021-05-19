#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)
    print("Количество нулевых символов:", A.count(0))
    for i, item in enumerate(A):
        if item == 0:
            print(f"Индекс нулевого символа: {i}")















