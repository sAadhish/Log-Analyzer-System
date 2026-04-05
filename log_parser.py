def parse_log_line(line):   
  parts = line.split()
  timestamp = parts[0] + "  " + parts[1]
  level = parts[2]
  message = " ".join(parts[3:]) # used to join those words that are splited  
  return{
        "timestamp": timestamp,
        "level": level,
        "message":message
    }
       




