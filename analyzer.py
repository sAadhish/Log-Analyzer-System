from reader import read_logs 
from log_parser import parse_log_line

def count_levels(logs):
    counts = {}
    for log in logs:
        level = log["level"]
        if level in counts:
            counts[level] +=1

        else :
            counts[level]=1

    return counts

# Find which ERROR message appears the most
def most_common_error(logs):
    error_count = {}

    for log in logs:

        if log["level"] == "ERROR":
            msg=log["message"]

            if msg in error_count:
                error_count[msg] += 1
            else:
                error_count[msg] = 1

    if not error_count:
        return None

    most_common_error_message = max(error_count, key=error_count.get)
    return most_common_error_message

#Giving only ERROR logs
def filter_by_level(logs, level):
    filtered = []

    for log in logs:
        if log["level"] == level:
            filtered.append(log)

    return filtered