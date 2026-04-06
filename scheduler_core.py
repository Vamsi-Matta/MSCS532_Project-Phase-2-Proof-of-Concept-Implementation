import heapq
from collections import defaultdict


class TaskScheduler:
    def __init__(self):
        self.tasks = {}
        self.categories = defaultdict(list)
        self.queue = []

    def add_task(self, task_id, text, priority, category):
        if task_id in self.tasks:
            raise ValueError(f"Task '{task_id}' already exists.")

        if priority < 1:
            raise ValueError("Priority must be >= 1")

        self.tasks[task_id] = {
            "text": text,
            "priority": priority,
            "category": category,
            "status": "Pending"
        }

        self.categories[category].append(task_id)
        heapq.heappush(self.queue, (priority, task_id))

    def update_priority(self, task_id, new_priority):
        if task_id not in self.tasks:
            return None

        if new_priority < 1:
            raise ValueError("Priority must be >= 1")

        self.tasks[task_id]["priority"] = new_priority
        heapq.heappush(self.queue, (new_priority, task_id))

    def get_task(self, task_id):
        return self.tasks.get(task_id)

    def get_tasks_by_category(self, category):
        result = []
        for tid in self.categories.get(category, []):
            if tid in self.tasks:
                task_data = {"task_id": tid}
                task_data.update(self.tasks[tid])
                result.append(task_data)
        return result

    # 🔥 PHASE 3 OPTIMIZED METHOD
    def get_next_task(self):
        while self.queue:
            priority, task_id = heapq.heappop(self.queue)

            if task_id not in self.tasks:
                continue

            current = self.tasks[task_id]

            # validate latest priority
            if current["priority"] == priority and current["status"] == "Pending":
                return {
                    "task_id": task_id,
                    "text": current["text"],
                    "priority": priority,
                    "category": current["category"]
                }

        return None

    def mark_completed(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]["status"] = "Completed"

    def remove_task(self, task_id):
        if task_id in self.tasks:
            category = self.tasks[task_id]["category"]
            del self.tasks[task_id]

            if task_id in self.categories[category]:
                self.categories[category].remove(task_id)

    def list_all_tasks(self):
        return [
            {"task_id": tid, **details}
            for tid, details in self.tasks.items()
        ]