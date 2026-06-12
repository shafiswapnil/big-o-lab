import matplotlib.pyplot as plt
from benchmark import run_benchmarks, run_fib_benchmarks


def create_chart():
    """Generate a comparison chart of algorithm growth curves."""
    sizes, results = run_benchmarks()

    plt.figure(figsize=(10, 6))

    for name, times in results.items():
        # Filter out None values for plotting
        plot_sizes = [sizes[i] for i in range(len(times)) if times[i] is not None]
        plot_times = [t for t in times if t is not None]
        plt.plot(plot_sizes, plot_times, marker="o", linewidth=2, label=name)

        plt.xlabel("Input Size (n)")
        plt.ylabel("Time (seconds)")
        plt.title("Big O in Action: Algorithm Speed vs. Input Size")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig("big_o_comparison.png", dpi=150)
        print("Chart saved as big_o_comparison.png")


def create_fib_chart():
    """Generate a chart comparing naive vs. memoized Fibonacci."""
    fib_sizes, fib_results = run_fib_benchmarks()

    plt.figure(figsize=(10, 6))

    for name, times in fib_results.items():
        plt.plot(fib_sizes, times, marker="o", linewidth=2, label=name)

    plt.xlabel("Fibonacci Number (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Exponential vs. Linear: Naive vs. Memoized Fibonacci")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("fib_comparison.png", dpi=150)
    print("Chart saved as fib_comparison.png")


if __name__ == "__main__":
    create_chart()
    create_fib_chart()
