import json
from scheduler_core import SchedulerCore


def section(name):
    print("-" * 60)
    print(name)
    print("-" * 60)


def load_seed_tasks(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    scheduler = SchedulerCore()
    seed_tasks = load_seed_tasks("tasks_seed.json")

    section("* LOADING INITIAL TASKS *")
    for item in seed_tasks:
        scheduler.add_new_task(
            item["task_id"],
            item["title"],
            item["priority"],
            item["category"]
        )
        print(f"Loaded {item['task_id']} - {item['title']}")

    section("* CURRENT TASK SUMMARY *")
    for task in scheduler.summary():
        print(task)

    section("* VIEWING ONE TASK *")
    print(scheduler.fetch_task_details("TS101"))

    section("* UPDATING PRIORITY *")
    scheduler.revise_priority("TS101", 1)
    print("Priority updated for TS101")
    print(scheduler.fetch_task_details("TS101"))

    section("* TASKS UNDER ACADEMIC CATEGORY *")
    for task in scheduler.fetch_by_category("Academic"):
        print(task)

    section("* NEXT READY TASK *")
    print(scheduler.next_ready_task())

    section("* MARKING TASK AS COMPLETED *")
    scheduler.mark_completed("TS102")
    print(scheduler.fetch_task_details("TS102"))

    section("* REMOVING A TASK *")
    scheduler.remove_task("TS103")
    for task in scheduler.summary():
        print(task)

    section("* PROCESSING REMAINING TASKS *")
    while True:
        item = scheduler.next_ready_task()
        if item is None:
            break
        print(item)


if __name__ == "__main__":
    main()
