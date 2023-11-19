"""Constants Module"""

# agent related constants / default values
INIT_SPEED = 100
INIT_ENERGY = 8000
MAX_ENERGY = 16000
EAT_ENERGY = 4000
CORRELATION_FACTOR = 0.8
REP_THRESHOLD = 0.8  # reproduction threshold, e.g. 0.8 -> 80% energy required to reproduce
PROB_MUTATE = 0.5  # probability of a mutation occurring in offspring

# environment related constants
ENV_SIZE = 4000
TIME_STEP = 0.1
DATA_INTERVAL = 1  # number of steps between data collection
CONTINUATION = False

# food related constants
FOOD_SIZE = 50
FOOD_SPAWN_RATE = 0.04

BASE_LOSS = TIME_STEP*10
