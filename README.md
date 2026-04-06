# Smart Task Scheduler - Phase 2 Prototype

## Overview
This project presents a working prototype of a task scheduling system built with Python. The purpose of the system is to organize tasks by urgency and category while supporting common scheduling operations in a clean and structured way.

## Main Idea
The scheduler keeps task information in memory and uses a priority-driven mechanism to determine which task should be handled first. It also groups tasks by category so that related activities can be reviewed together.

## Included Files
- `scheduler_core.py` - core scheduler logic
- `simulate_day.py` - sample execution flow
- `validation_report.py` - validation checks for important operations
- `tasks_seed.json` - initial task data used by the simulation
- `README.md` - project overview

## Features Demonstrated
- task creation
- task lookup
- category-based retrieval
- priority revision
- next-task selection
- completion tracking
- task removal

## How to Run
Run the main simulation:

```bash
python simulate_day.py
python scheduler_core.py

## Phase 3 Enhancements

In Phase 3, the system was improved to address limitations identified in the proof-of-concept version.

The main improvement focuses on handling outdated entries in the restock priority queue. When product quantities are updated multiple times, older values may still exist in the queue. To improve accuracy, the retrieval logic now validates entries before returning them.

Additional enhancements include:
- Improved input validation for product operations
- Better handling of edge cases
- Performance testing with larger datasets

These changes make the system more reliable and closer to real-world usage.