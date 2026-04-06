import time
from scheduler_core import TaskScheduler


def run_test():
    sizes = [100, 500, 1000, 3000]

    for size in sizes:
        scheduler = TaskScheduler()

        start_insert = time.time()
        for i in range(size):
            scheduler.add_task(
                f"T{i}",
                f"Task {i}",
                (i % 5) + 1,
                f"Cat{i % 3}"
            )
        end_insert = time.time()

        start_lookup = time.time()
        for i in range(size):
            scheduler.get_task(f"T{i}")
        end_lookup = time.time()

        start_next = time.time()
        for _ in range(50):
            scheduler.get_next_task()
        end_next = time.time()

        print(f"\nSize: {size}")
        print(f"Insert: {end_insert - start_insert:.6f}")
        print(f"Lookup: {end_lookup - start_lookup:.6f}")
        print(f"Next Task: {end_next - start_next:.6f}")


if __name__ == "__main__":
    run_test()