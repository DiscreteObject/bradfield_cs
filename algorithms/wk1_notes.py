# -*- coding: utf-8 -*-
import time


def get_sum(n):
    start = time.time()

    total_sum = 0
    for x in xrange(1, n + 1):
        total_sum += x

    end = time.time()
    return total_sum, end - start

def get_sum_2(n):
    start = time.time()
    total = n * (n + 1) / 2
    end = time.time()

    return total, end - start


def main():
    output_template = '{}({}) = {:15d} ({:8.7f} seconds)'
    num_times = 5

    for _ in range(num_times):
        print(output_template.format('get_sum', 1000000, *get_sum(1000000)))

    print("---------")

    for i in range(1, 10):
        print(output_template.format('get_sum', i * 1000000, *get_sum(i * 1000000)))

    print("---------")

    for i in range(1, 10):
        print(output_template.format('get_sum_2', i * 1000000, *get_sum_2(i * 1000000)))

if __name__ == '__main__':
    main()
