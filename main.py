from reader import read_logs


logs = read_logs("sample.log")

for log in logs:
    print(log)