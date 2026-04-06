🧪 Log Analyzer System

A Python-based CLI tool to parse, analyze, and extract insights from system log files. This project simulates real-world log monitoring used in backend systems and DevOps workflows.

⸻

🚀 Features
	•	📂 Read and process log files
	•	🧩 Parse unstructured logs into structured data
	•	📊 Count log levels (INFO, WARNING, ERROR)
	•	🔍 Identify most frequent error messages
	•	🎯 Filter logs by level (ERROR, WARNING)
	•	💻 Interactive CLI interface

⸻

🧠 How It Works

Log File → Parser → Analyzer → CLI Output

	•	Parser: Converts raw log lines into structured dictionaries
	•	Analyzer: Performs counting, filtering, and insights
	•	CLI: Allows user interaction and displays results

📁 Project Structure

log_analyzer/
│
├── main.py          # CLI interface
├── log_parser.py    # Parses each log line
├── reader.py        # Reads log file
├── analyzer.py      # Analysis logic
├── sample.log       # Sample log data

🛠️ Technologies Used
	•	Python 3
	•	File Handling
	•	OOP Concepts
	•	CLI (Command Line Interface)

⸻

▶️ How to Run
	1.	Clone the repository

    git clone https://github.com/sAadhish/Log-Analyzer-System.git 
    cd log_analyzer

    2.	Run the program

    python main.py

🧪 Sample Log Format

2026-04-01 10:00:00 INFO User logged in
2026-04-01 10:05:00 ERROR Database connection failed
2026-04-01 10:06:00 WARNING Disk space low

📊 Example Output

----- LOG ANALYSIS REPORT -----

Total Logs: 3

Log Levels:
INFO: 1
WARNING: 1
ERROR: 1

Most Common Error:
Database connection failed

💡 Key Learnings
	•	Data parsing and transformation
	•	File processing in Python
	•	Dictionary-based counting logic
	•	Modular project structure
	•	CLI-based application design

⸻

🔮 Future Enhancements
	•	Save reports to file
	•	Add graphical visualization
	•	Integrate AI for log explanation
	•	Real-time log monitoring

