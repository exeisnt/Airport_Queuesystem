# --- Performance Analysis ---
def performance_analysis(function, *args):
    """Analyzes runtime and memory usage of a function."""
    start_time = time.time()
    start_memory = memory_profiler.memory_usage()[0]
    result = function(*args)
    end_memory = memory_profiler.memory_usage()[0]
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds")
    print(f"Memory Usage: {end_memory - start_memory:.2f} MB")
    return result
