import json
from scheduler_core import TaskScheduler


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def load_tasks():
    with open("tasks_seed.json", "r") as f:
        return json.load(f)


def main():
    scheduler = TaskScheduler()

    section("LOADING TASKS")
    for t in load_tasks():
        scheduler.add_task(
            t["task_id"],
            t["text"],
            t["priority"],
            t["category"]
        )
        print(f"Loaded {t['task_id']}")

    section("ALL TASKS")
    for t in scheduler.list_all_tasks():
        print(t)

    section("UPDATE PRIORITY")
    scheduler.update_priority("T1", 1)
    print(scheduler.get_task("T1"))

    section("CATEGORY VIEW")
    for t in scheduler.get_tasks_by_category("Work"):
        print(t)

    section("NEXT TASK")
    print(scheduler.get_next_task())

    section("MARK COMPLETE")
    scheduler.mark_completed("T2")
    print(scheduler.get_task("T2"))

    section("FINAL STATE")
    for t in scheduler.list_all_tasks():
        print(t)


if __name__ == "__main__":
    main()