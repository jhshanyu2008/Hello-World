import matplotlib.pyplot as plt
from random import shuffle

iteration = 10000
pool_size = 200
top_rewards = ["A"]
next_rewards = ["a", "b", "c", "d", "e"]

reward_pool = ["0" for i in range(pool_size - len(top_rewards) - len(next_rewards))]
reward_pool += top_rewards + next_rewards

details = {}
top_iter = {}
total_iter = {}
for i in range(iteration):
    shuffle(reward_pool)
    details[i] = [0, 0]
    flag = 0
    for j in range(pool_size):
        if reward_pool[j] in top_rewards:
            flag += 1
            details[i][0] = j+1
            details[i][1] = j+1
        elif reward_pool[j] in next_rewards:
            flag += 1
            details[i][1] = j+1
        else:
            continue
        if flag == len(top_rewards) + len(next_rewards):
            try:
                top_iter[details[i][0]]
                total_iter[details[i][1]]
            except:
                top_iter[details[i][0]] = 0
                total_iter[details[i][1]] = 0
            top_iter[details[i][0]] += 1
            total_iter[details[i][1]] += 1
            break

_x = []
_y = []
for x, y in top_iter.items():
    _x.append(x)
    _y.append(y)
plt.figure()
ax_1 = plt.subplot(211)
ax_1.bar(_x, _y, facecolor="#9999ff", edgecolor="white")
plt.draw()

t_x = []
t_y = []
for x, y in total_iter.items():
    t_x.append(x)
    t_y.append(y)
ax_2 = plt.subplot(212)
ax_2.bar(t_x, t_y, facecolor="#9999ff", edgecolor="white")
plt.draw()
plt.show()
