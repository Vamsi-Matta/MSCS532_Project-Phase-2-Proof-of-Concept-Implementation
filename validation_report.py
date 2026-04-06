from scheduler_core import TaskScheduler


def check(label, condition):
    print(f"{label}: {'PASS' if condition else 'FAIL'}")


def main():
    scheduler = TaskScheduler()

    scheduler.add_task("T1", "Task A", 2, "Work")
    scheduler.add_task("T2", "Task B", 1, "Work")

    check("Add task", "T1" in scheduler.tasks)

    task = scheduler.get_task("T2")
    check("Fetch task", task is not None and task["text"] == "Task B")

    scheduler.update_priority("T1", 1)
    updated = scheduler.get_task("T1")
    check("Update priority", updated["priority"] == 1)

    next_task = scheduler.get_next_task()
    check("Priority execution", next_task is not None)

    scheduler.mark_completed("T1")
    check("Completion", scheduler.get_task("T1")["status"] == "Completed")

    scheduler.remove_task("T2")
    check("Removal", scheduler.get_task("T2") is None)


if __name__ == "__main__":
    main()