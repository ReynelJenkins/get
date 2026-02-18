import numpy as np
import time

def get_wave_amplitude(freq, time):
    period = 1.0 / freq
    phase = (time % period) / period
    
    if phase < 0.5:
        return 2.0 * phase
    
    else:
        return 2.0 - 2.0 * phase
    
def wait_for_sampling_period(sampling_frequency):
    period = 1.0 / sampling_frequency
    time.sleep(period)
