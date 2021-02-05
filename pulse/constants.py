from numpy import inf

debug = False

# timeout for karat getting decay
DECAY_ANSWER_TIMEOUT_MINUTES = 10

# cross_plots generation step in mm and count of decays between 2 "raw" decays after interpolation
CROSS_PLOTS_INTERPOLATION_COUNT = 50

# how to divide data responses while getting thickness by cross_plots
GRID_OPTIMIZER_DATA_PARTS = 6
GRID_OPTIMIZER_DATA_SIZE_THRESHOLD = inf
