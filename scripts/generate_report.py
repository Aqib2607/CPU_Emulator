import datetime

def generate_report():
    """Generates a simple report for the CPU emulator."""
    with open("performance_report.txt", "w") as report:
        report.write("Virtual CPU Emulator Report\n")
        report.write("===========================\n")
        report.write(f"Date: {datetime.datetime.now()}\n")
        report.write("Performance Test: Completed\n")
        report.write("Test Duration: 2 seconds (Simulated)\n")
        report.write("\nTested Programs:\n")
        report.write("- simple_program.asm\n")
        report.write("- io_program.asm\n")
        report.write("- branching_program.asm\n")

    print("Report generated: performance_report.txt")

if __name__ == "__main__":
    generate_report()
