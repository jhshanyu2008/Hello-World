import numpy as np
import matplotlib.pyplot as plt

iteration = 10000
target_dir = {'A': 2.0,
              'B': 2.0,
              'C': 2.5,
              'D': 2.5,
              'E': 5,
              'F': 5
              }
term_set = [0, 500, 50]
Finished = False
target_depart = {}
target_get = {}
analy_dir = {}
term_depart = {}
total_num = 0

for i in range(term_set[0], term_set[1], term_set[2]):
    term_depart[(i, i + term_set[2])] = 0
term_depart[(term_set[1], float('Inf'))] = 0

for name, num in target_dir.items():
    target_get[name] = 0
    target_depart[name] = (total_num, total_num + num)
    total_num += num

details = {}
for i in range(iteration):
    for name in target_get:
        target_get[name] = 0
    Finished = False
    terms = 0
    while not Finished:
        get = 100 * np.random.rand()
        terms += 1
        for name, depart in target_depart.items():
            if depart[0] < get <= depart[1]:
                target_get[name] += 1
        for name, status in target_get.items():
            if status == 0:
                Finished = False
                break
            else:
                Finished = True
    try:
        analy_dir[terms]
    except:
        analy_dir[terms] = 0
    analy_dir[terms] += 1
    for term_range in term_depart:
        if term_range[0] < terms <= term_range[1]:
            term_depart[term_range] += 1
    details[i] = {terms: target_get}

raw_x = []
raw_y = []
for x, y in analy_dir.items():
    raw_x.append(x)
    raw_y.append(y)
plt.figure()
ax_1 = plt.subplot(211)
ax_1.bar(raw_x, raw_y, facecolor="#9999ff", edgecolor="white")
plt.draw()

con_x = []
con_y = []
for x, y in term_depart.items():
    con_x.append(x[0] + term_set[2] / 2)
    con_y.append(y)
ax_2 = plt.subplot(212)
ax_2.bar(con_x, con_y, width=0.8 * term_set[2], facecolor="#9999ff", edgecolor="white")
plt.draw()
plt.show()
