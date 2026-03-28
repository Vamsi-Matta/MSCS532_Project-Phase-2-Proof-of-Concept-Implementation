from dataclasses import dataclass
from collections import defaultdict
import heapq
import itertools


@dataclass
class Task:
    task_id: str
    title: str
    priority: int
    category: str
    status: str = "Pending"


class SchedulerCore:
    def __init__(self):
        self.task_book = {}
        self.category_map = defaultdict(list)
        self.heap = []
        self._sequence = itertools.count()

    def add_new_task(self, task_id, title, priority, category):
        if task_id in self.task_book:
            raise ValueError(f"Task ID '{task_id}' already exists.")

        if priority < 1:
            raise ValueError("Priority must be greater than 0.")

        task = Task(task_id, title, priority, category)
        self.task_book[task_id] = task
        self.category_map[category].append(task_id)

        entry = (priority, next(self._sequence), task_id)
        heapq.heappush(self.heap, entry)

    def revise_priority(self, task_id, new_priority):
        if task_id not in self.task_book:
            raise KeyError(f"Task ID '{task_id}' not found.")

        if new_priority < 1:
            raise ValueError("Priority must be greater than 0.")

        self.task_book[task_id].priority = new_priority
        entry = (new_priority, next(self._sequence), task_id)
        heapq.heappush(self.heap, entry)

    def fetch_task_details(self, task_id):
        task = self.task_book.get(task_id)
        if task is None:
            return None

        return {
            "task_id": task.task_id,
            "title": task.title,
            "priority": task.priority,
            "category": task.category,
            "status": task.status
        }

    def fetch_by_category(self, category):
        ids = self.category_map.get(category, [])
        return [self.fetch_task_details(task_id) for task_id in ids if task_id in self.task_book]

    def mark_completed(self, task_id):
        if task_id not in self.task_book:
            raise KeyError(f"Task ID '{task_id}' not found.")

        self.task_book[task_id].status = "Completed"

    def next_ready_task(self):
        while self.heap:
            priority, _, task_id = heapq.heappop(self.heap)

            if task_id not in self.task_book:
                continue

            task = self.task_book[task_id]

            if task.status == "Completed":
                continue

            if task.priority != priority:
                continue

            return {
                "task_id": task.task_id,
                "title": task.title,
                "priority": task.priority,
                "category": task.category,
                "status": task.status
            }

        return None

    def remove_task(self, task_id):
        if task_id not in self.task_book:
            raise KeyError(f"Task ID '{task_id}' not found.")

        category = self.task_book[task_id].category
        del self.task_book[task_id]

        if task_id in self.category_map[category]:
            self.category_map[category].remove(task_id)

        if not self.category_map[category]:
            del self.category_map[category]

    def summary(self):
        output = []
        for task in self.task_book.values():
            output.append({
                "task_id": task.task_id,
                "title": task.title,
                "priority": task.priority,
                "category": task.category,
                "status": task.status
            })
        return output
