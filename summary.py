from reader import read_logs
from analyzer import count_levels, most_common_error
def summary(logs):

    #logs =read_logs("sample.log")
    total_logs = len(logs)

    level_count = count_levels(logs)
    most_common = most_common_error(logs)


    print("----- LOG ANALYSIS REPORT -----")

    print(f"\nTotal Logs : {total_logs}")

    print(f"\nLog Levels : ")
    for level , count in level_count.items():
        print(f"{level} : {count}")

    print("\nMost Common Error:")

    if most_common:
        print(most_common)
    else:
        print("No errors found")