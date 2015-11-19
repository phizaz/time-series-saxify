import math
import bisect
import json
import random
import numpy

__author__ = 'phizaz'

X = 6
Y = 3
Z = 4

n = 2 ** X
w = 2 ** Y

def to_file(variable, file):
    with open(file, 'w') as outfile:
        json.dump(variable, outfile)

def generate_series(length, max):
    return numpy.array([random.uniform(0, max) for i in range(length)])

A = generate_series(n, X)
B = generate_series(n, X)

to_file(A.tolist(), 'time_series_A.json')
to_file(B.tolist(), 'time_series_B.json')

print('time_series A:', A)
print('time_series B:', B)

def normalize(time_series):
    mean = numpy.mean(time_series)
    std = numpy.std(time_series)

    return numpy.array([(each - mean) / std for each in time_series])

norm_A = normalize(A)
norm_B = normalize(B)

to_file(norm_A.tolist(), 'normalized_A.json')
to_file(norm_B.tolist(), 'normalized_B.json')

print('normalized A:', norm_A)
print('normalized B:', norm_B)

def saxify(time_series, alphabet_count, word_length):
    breakpoints =          {3 : [-0.43, 0.43],
                            4 : [-0.67, 0, 0.67],
                            5 : [-0.84, -0.25, 0.25, 0.84],
                            6 : [-0.97, -0.43, 0, 0.43, 0.97],
                            7 : [-1.07, -0.57, -0.18, 0.18, 0.57, 1.07],
                            8 : [-1.15, -0.67, -0.32, 0, 0.32, 0.67, 1.15],
                            9 : [-1.22, -0.76, -0.43, -0.14, 0.14, 0.43, 0.76, 1.22],
                            10: [-1.28, -0.84, -0.52, -0.25, 0, 0.25, 0.52, 0.84, 1.28],
                            11: [-1.34, -0.91, -0.6, -0.35, -0.11, 0.11, 0.35, 0.6, 0.91, 1.34],
                            12: [-1.38, -0.97, -0.67, -0.43, -0.21, 0, 0.21, 0.43, 0.67, 0.97, 1.38],
                            13: [-1.43, -1.02, -0.74, -0.5, -0.29, -0.1, 0.1, 0.29, 0.5, 0.74, 1.02, 1.43],
                            14: [-1.47, -1.07, -0.79, -0.57, -0.37, -0.18, 0, 0.18, 0.37, 0.57, 0.79, 1.07, 1.47],
                            15: [-1.5, -1.11, -0.84, -0.62, -0.43, -0.25, -0.08, 0.08, 0.25, 0.43, 0.62, 0.84, 1.11, 1.5],
                            16: [-1.53, -1.15, -0.89, -0.67, -0.49, -0.32, -0.16, 0, 0.16, 0.32, 0.49, 0.67, 0.89, 1.15, 1.53],
                            17: [-1.56, -1.19, -0.93, -0.72, -0.54, -0.38, -0.22, -0.07, 0.07, 0.22, 0.38, 0.54, 0.72, 0.93, 1.19, 1.56],
                            18: [-1.59, -1.22, -0.97, -0.76, -0.59, -0.43, -0.28, -0.14, 0, 0.14, 0.28, 0.43, 0.59, 0.76, 0.97, 1.22, 1.59],
                            19: [-1.62, -1.25, -1, -0.8, -0.63, -0.48, -0.34, -0.2, -0.07, 0.07, 0.2, 0.34, 0.48, 0.63, 0.8, 1, 1.25, 1.62],
                            20: [-1.64, -1.28, -1.04, -0.84, -0.67, -0.52, -0.39, -0.25, -0.13, 0, 0.13, 0.25, 0.39, 0.52, 0.67, 0.84, 1.04, 1.28, 1.64]
                            }

    sax_string = []
    acc = 0
    for i, each in enumerate(time_series):
        acc += each
        if i % word_length == word_length - 1:
            mean = acc / word_length
            pos = bisect.bisect_left(breakpoints[alphabet_count], mean)
            sax_string.append(chr(65 + pos))
            acc = 0

    return sax_string

sax_A = saxify(norm_A, Z, n / w)
sax_B = saxify(norm_B, Z, n / w)

print('sax_A:', sax_A)
print('sax_B:', sax_B)

def mindist(sax_A, sax_B, alphabet_count, word_length):
    breakpoints =          {3 : [-0.43, 0.43],
                            4 : [-0.67, 0, 0.67],
                            5 : [-0.84, -0.25, 0.25, 0.84],
                            6 : [-0.97, -0.43, 0, 0.43, 0.97],
                            7 : [-1.07, -0.57, -0.18, 0.18, 0.57, 1.07],
                            8 : [-1.15, -0.67, -0.32, 0, 0.32, 0.67, 1.15],
                            9 : [-1.22, -0.76, -0.43, -0.14, 0.14, 0.43, 0.76, 1.22],
                            10: [-1.28, -0.84, -0.52, -0.25, 0, 0.25, 0.52, 0.84, 1.28],
                            11: [-1.34, -0.91, -0.6, -0.35, -0.11, 0.11, 0.35, 0.6, 0.91, 1.34],
                            12: [-1.38, -0.97, -0.67, -0.43, -0.21, 0, 0.21, 0.43, 0.67, 0.97, 1.38],
                            13: [-1.43, -1.02, -0.74, -0.5, -0.29, -0.1, 0.1, 0.29, 0.5, 0.74, 1.02, 1.43],
                            14: [-1.47, -1.07, -0.79, -0.57, -0.37, -0.18, 0, 0.18, 0.37, 0.57, 0.79, 1.07, 1.47],
                            15: [-1.5, -1.11, -0.84, -0.62, -0.43, -0.25, -0.08, 0.08, 0.25, 0.43, 0.62, 0.84, 1.11, 1.5],
                            16: [-1.53, -1.15, -0.89, -0.67, -0.49, -0.32, -0.16, 0, 0.16, 0.32, 0.49, 0.67, 0.89, 1.15, 1.53],
                            17: [-1.56, -1.19, -0.93, -0.72, -0.54, -0.38, -0.22, -0.07, 0.07, 0.22, 0.38, 0.54, 0.72, 0.93, 1.19, 1.56],
                            18: [-1.59, -1.22, -0.97, -0.76, -0.59, -0.43, -0.28, -0.14, 0, 0.14, 0.28, 0.43, 0.59, 0.76, 0.97, 1.22, 1.59],
                            19: [-1.62, -1.25, -1, -0.8, -0.63, -0.48, -0.34, -0.2, -0.07, 0.07, 0.2, 0.34, 0.48, 0.63, 0.8, 1, 1.25, 1.62],
                            20: [-1.64, -1.28, -1.04, -0.84, -0.67, -0.52, -0.39, -0.25, -0.13, 0, 0.13, 0.25, 0.39, 0.52, 0.67, 0.84, 1.04, 1.28, 1.64]
                            }

    lookup_table = [[0 for i in range(alphabet_count)] for i in range(alphabet_count)]

    for r in range(alphabet_count):
        for c in range(alphabet_count):
            if abs(r-c) <= 1:
                lookup_table[r][c] = 0
            else:
                lookup_table[r][c] = breakpoints[alphabet_count][max(r, c) - 1] - breakpoints[alphabet_count][min(r, c)]

    sum = 0
    for i in range(len(sax_A)):
        A_i = ord(sax_A[i]) - 65
        B_i = ord(sax_B[i]) - 65
        sum += lookup_table[A_i][B_i] ** 2

    return math.sqrt(word_length) * math.sqrt(sum)

dist = mindist(sax_A, sax_B, Z, n / w)
print('distance between sax_A and sax_B:', dist)

