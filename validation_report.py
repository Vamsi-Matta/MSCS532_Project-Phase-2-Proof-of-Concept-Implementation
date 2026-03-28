from scheduler_core import SchedulerCore


def check(label, condition):
    result = "PASS" if condition else "FAIL"
    print(f"{label}: {result}")


def main():
    scheduler = SchedulerCore()

    print("VALIDATION REPORT")
    print("-" * 50)

    scheduler.add_new_task("A1", "Draft report", 2, "Academic")
    scheduler.add_new_task("W1", "Client follow-up", 1, "Work")
    scheduler.add_new_task("P1", "Pay electricity bill", 3, "Personal")

    check("Task added successfully", "A1" in scheduler.task_book)

    details = scheduler.fetch_task_details("W1")
    check("Fetch task details works", details is not None and details["title"] == "Client follow-up")

    work_items = scheduler.fetch_by_category("Work")
    check("Category mapping works", len(work_items) == 1)

    top_task = scheduler.next_ready_task()
    check("Priority retrieval works", top_task is not None and top_task["task_id"] == "W1")

    scheduler.revise_priority("A1", 1)
    updated = scheduler.fetch_task_details("A1")
    check("Priority update works", updated["priority"] == 1)

    scheduler.mark_completed("A1")
    updated_after_completion = scheduler.fetch_task_details("A1")
    check("Completion update works", updated_after_completion["status"] == "Completed")

    scheduler.remove_task("P1")
    check("Removal works", scheduler.fetch_task_details("P1") is None)

    print("-" * 50)
    print("Validation finished.")
    

if __name__ == "__main__":
    main()
