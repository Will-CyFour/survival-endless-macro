import time

start_time = time.perf_counter_ns()

time.sleep(100)

end_time = time.perf_counter_ns()

duration_ns = end_time - start_time
duration_ms = duration_ns // 1_000_000

print(f"The code took {duration_ms} milliseconds to run.")
