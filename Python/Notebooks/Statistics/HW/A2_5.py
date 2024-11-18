import numpy as np
from scipy.stats import mode


def wait_time_analysis(wait_times):
    mean_wait = np.mean(wait_times)
    median_wait = np.median(wait_times)

    mode_result = mode(wait_times, keepdims=True)  # Use `keepdims=True`
    mode_wait = mode_result.mode[0] if mode_result.count[0] > 0 else "No mode"

    print(f"Average Wait Time (Mean): {mean_wait:.2f} minutes")
    print(f"Typical Wait Time (Median): {median_wait:.2f} minutes")
    print(f"Most Common Wait Time (Mode): {mode_wait} minutes")

wait_times = [5, 10, 15, 10, 20, 5, 10, 30, 5, 5]
wait_time_analysis(wait_times)