from log_parser import parse_log_line

def read_logs(file_path):
    logs = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            parsed = parse_log_line(line)
            logs.append(parsed)

    return logs
