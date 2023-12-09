import matplotlib.pyplot as plt
from analysis import import_data
import numpy as np
import pickle
from tqdm import tqdm
from scipy.stats import pearsonr
import pandas as pd

plt.style.use("ben")

LV_data = import_data("/Users/benstevens/PycharmProjects/computational-evolution-LV/computational-evolution/data/LV_data1")

# use when cahnging data
# pickle_file_path = 'data_frame.pkl'
# with open(pickle_file_path, 'wb') as pickle_file:
#     pickle.dump(LV_data, pickle_file)

with open('data_frame.pkl', 'rb') as pickle_file:
    LV_data = pickle.load(pickle_file)

pop_data = LV_data["pop_data_1"]

t = pop_data["Time Elapsed/s"]
ag_pop = pop_data["Agent Population"]
pred_pop = pop_data["Predator Population"]
food_pop = pop_data["Food Population"]

# plt.figure(figsize=(12, 6))
# plt.xlabel("Step")
# plt.xlim(5000, 25000)
# plt.title("Predator-Prey Population")
#
# plt.plot(t, ag_pop, color='blue', label="Prey Population")
# plt.plot(t, pred_pop, color='red', label="Predator Population")
# plt.plot(t, food_pop, color='green', label="Food")
#
# plt.legend()
# plt.show()


def get_alpha(step, interval, data):
    """Return alpha, the prey growth rate"""

    prey_pop = list(data['Agent Population'])[step-interval:step]
    mean_prey_pop = np.average(prey_pop)
    prey_births = list(data['Prey Births'])
    prey_births = prey_births[step] - prey_births[step-interval]

    alpha = prey_births / mean_prey_pop
    return alpha / interval


def get_beta(step, interval, data):
    """Return beta, the prey death rate per predator"""

    prey_pop = list(data['Agent Population'])[step - interval:step]
    pred_pop = list(data['Predator Population'])[step - interval:step]
    mean_prey_pop = np.average(prey_pop)
    mean_pred_pop = np.average(pred_pop)
    prey_deaths = list(data['Prey Deaths'])
    prey_deaths = prey_deaths[step] - prey_deaths[step - interval]

    beta = prey_deaths / (mean_prey_pop * mean_pred_pop)
    return beta / interval


def get_delta(step, interval, data):
    """Return delta, the predator birth rate per prey"""

    prey_pop = list(data['Agent Population'])[step - interval:step]
    pred_pop = list(data['Predator Population'])[step - interval:step]
    mean_prey_pop = np.average(prey_pop)
    mean_pred_pop = np.average(pred_pop)
    pred_births = list(data['Predator Births'])
    pred_births = pred_births[step] - pred_births[step - interval]

    delta = pred_births / (mean_prey_pop * mean_pred_pop)
    return delta / interval


def get_gamma(step, interval, data):
    """Return gamma, the predator death rate"""

    pred_pop = list(data['Predator Population'])[step-interval:step]
    mean_pred_pop = np.average(pred_pop)
    pred_deaths = list(data['Predator Deaths'])
    pred_deaths = pred_deaths[step] - pred_deaths[step - interval]

    gamma = pred_deaths / mean_pred_pop
    return gamma / interval


def dX_dt(X, step):
    """Return dX_dt where X = [num_prey, num_predators]
    """
    prey = X[0]
    pred = X[1]
    dX_dt = np.array([a*prey - b*prey*pred, d*pred*prey - g*pred])
    return dX_dt


def next(X, dX_dt):
    """find next step X_new from X"""
    X_new = np.array([X[0]+dX_dt[0], X[1]+dX_dt[1]])
    return X_new


def solve(X_0, step):
    """find X for the next 5000 steps"""
    X = X_0
    X_vals = []
    dt = 1
    t_vals = np.arange(step, step+5000, dt)
    for i in tqdm(range(len(t_vals))):
        X_new = next(X, dX_dt(X, step)*dt)
        X_vals.append(X_new)
        X = X_new

    return X_vals, t_vals


# finding param vals every 100 steps
a_vals = []
b_vals = []
d_vals = []
g_vals = []
step_vals = []

for i in tqdm(range(1, 200)):
    step = (i * 100)
    interval = 100
    step_vals.append(step)
    a_vals.append(get_alpha(step, interval, pop_data))
    b_vals.append(get_beta(step, interval, pop_data))
    d_vals.append(get_delta(step, interval, pop_data))
    g_vals.append(get_gamma(step, interval, pop_data))

step_vals = [i+5000 for i in step_vals]

a_pearsonr = pearsonr(step_vals, a_vals)[0]
b_pearsonr = pearsonr(step_vals, b_vals)[0]
d_pearsonr = pearsonr(step_vals, d_vals)[0]
g_pearsonr = pearsonr(step_vals, g_vals)[0]

plt.figure(figsize=(8,6))

plt.ylabel(r"$\alpha$")
plt.xlabel("Step")

plt.plot(step_vals, a_vals, 'ro', label="Pearson r = "+str(np.round(a_pearsonr, 3)))

print("alpha std",np.std(a_vals))
print("alpha mean", np.mean(a_vals))

plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,6))

plt.ylabel(r"$\beta$")
plt.xlabel("Step")

plt.plot(step_vals, b_vals, 'bo', label="Pearson r = "+str(np.round(b_pearsonr, 3)))

print("beta std", np.std(b_vals))
print("beta mean", np.mean(b_vals))

plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,6))
plt.ylabel(r"$\delta$")
plt.xlabel("Step")

plt.plot(step_vals, d_vals, marker='o', linestyle='None', color='mediumorchid',
         label="Pearson r = "+str(np.round(d_pearsonr, 3)))

print("delta std", np.std(d_vals))
print("delta mean", np.mean(d_vals))

plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,6))
plt.ylabel(r"$\gamma$")
plt.xlabel("Step")

plt.plot(step_vals, g_vals, marker='o', color='royalblue', linestyle='None',
         label="Pearson r = "+str(np.round(g_pearsonr, 3)))

print("gamma std", np.std(g_vals))
print("gamma mean", np.mean(g_vals))

plt.legend()
plt.tight_layout()
plt.show()

a = get_alpha(19000, 18000, pop_data)
b = get_beta(19000, 18000, pop_data)
d = get_delta(19000, 18000, pop_data)
g = get_gamma(19000, 18000, pop_data)

X_vals, t_vals = solve(X_0=[ag_pop[0], pred_pop[0]], step=5000)

LV_prey = [X[0] for X in X_vals]
LV_pred = [X[1] for X in X_vals]

plt.figure(figsize=(12, 6))
plt.xlabel("Step")
plt.xlim(5000, 14000)
plt.title("Predator-Prey Population")

plt.plot(t, ag_pop, color='blue', label="Prey Population")
plt.plot(t, pred_pop, color='red', label="Predator Population")
# plt.plot(t, food_pop, color='green', label="Food")
plt.plot(t_vals, LV_prey, color='royalblue', label="LV Prey")
plt.plot(t_vals, LV_pred, color='coral', label="LV Pred")


plt.legend()
plt.show()




