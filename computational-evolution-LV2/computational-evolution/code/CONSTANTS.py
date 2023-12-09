"""Constants Module"""

# agent related constants / default values
INIT_SPEED = 100
INIT_ENERGY = 10000
PREY_MAX_ENERGY = 16000
PREDATOR_MAX_ENERGY = 20000
EAT_ENERGY = 4000
CORRELATION_FACTOR = 0.7
REP_THRESHOLD = 0.8  # reproduction threshold, e.g. 0.8 -> 80% energy required to reproduce
PROB_MUTATE = 0  # probability of a mutation occurring in offspring
MAX_SIGHT = 1000
MIN_SIZE = 50
PREY_REP_RATE = 0.002

# environment related constants
ENV_SIZE = 24000
TIME_STEP = 0.1
DATA_INTERVAL = 1  # number of steps between data collection
CONTINUATION = False

# food related constants
FOOD_SIZE = 50
FOOD_SPAWN_RATE = 0

BASE_LOSS = TIME_STEP*10
