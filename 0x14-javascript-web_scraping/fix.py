import requests
import sys

def count_completed_tasks(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Failed to fetch data from the API.")
        return

    tasks = response.json()
    completed_tasks = {}

    for task in tasks:
        if task['completed']:
            user_id = task['userId']
            if user_id in completed_tasks:
                completed_tasks[user_id] += 1
            else:
                completed_tasks[user_id] = 1

    return completed_tasks

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <API_URL>")
    else:
        api_url = sys.argv[1]
        completed_tasks = count_completed_tasks(api_url)
        print(completed_tasks)
