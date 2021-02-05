import numpy as np
import matplotlib.pyplot as plt
from common import tool_times
from common import well_construction as wc
from common.sensor_types import sensors
from solvers.solver_cim_py.interface import Solver


tubes = [
    wc.Tube(d=89., th0=6.5, th=6.5, sigma=3e6, mu=80.),
]

sensor = sensors.PULSE_3E_2
times = tool_times.times[sensor]
solver = Solver(sensor, times, tool_averaging=True)


if __name__ == '__main__':
    output = solver.get_curve(tubes)

    plt.figure()
    plt.semilogy(1e3 * times, output, 'o-')
    plt.ylabel('Signal')
    plt.xlabel('time, ms')
    plt.show()


pass
