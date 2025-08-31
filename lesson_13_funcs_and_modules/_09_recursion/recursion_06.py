# from
# collections import Counter
def count_tasks(tasks_tree):
    if not tasks_tree.get('subtasks'):
        return 1
    return 1 + sum(count_tasks(subtask) for subtask in tasks_tree['subtasks'])


if __name__ == '__main__':
    task_tree = {
        "name": "Main Task",
        "subtasks": [
            {"name": "Subtask 1", "subtasks": []},
            {"name": "Subtask 2", "subtasks": [
                {"name": "Sub-subtask 1", "subtasks": []},
                {"name": "Sub-subtask 2", "subtasks": []}
            ]}
        ]
    }
    print(count_tasks(task_tree))
