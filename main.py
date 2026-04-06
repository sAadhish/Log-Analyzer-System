from reader import read_logs
from analyzer import count_levels, most_common_error,filter_by_level
from summary import summary

logs =read_logs("sample.log")
while True:

    print("\n--- Log Analyzer ---")
    print("1. View Summary")
    print("2. View ERROR logs")
    print("3. View WARNING logs")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        summary(logs)

    elif choice == "2":
        error_logs = filter_by_level(logs, "ERROR")

        print("\n--- ERROR LOGS ---")
        for log in error_logs:
            print(log)

    elif choice == "3":
        warning_logs = filter_by_level(logs, "WARNING")

        print("\n--- WARNING LOGS ---")
        for log in warning_logs:
            print(log)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")



 

