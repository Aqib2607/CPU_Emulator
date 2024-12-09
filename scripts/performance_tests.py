import time

def run_performance_test():
    """Simple performance test for the Virtual CPU Emulator."""
    start_time = time.time()

    # Simulate running a sample program
    print("Running performance test...")
    # (You would replace the following with the actual CPU emulator running the program)
    time.sleep(2)  # Simulating program execution time

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Test completed in {execution_time:.4f} seconds.")

if __name__ == "__main__":
    run_performance_test()
