import sys
from collections import Counter
from colorama import Fore

header_of_table = "Рівень логування | Кількість"
separator = "-----------------|----------"

def parse_log_line(line: str) -> dict:
  dateList = line.split()
  return {
    'date': dateList[0],
    'time': dateList[1],
    'level': dateList[2],
    'message': ' '.join(dateList[3:])
  }

def load_logs(file_path: str) -> list[dict]:
  try:
   with open(file_path, 'r', encoding='utf-8') as file:
    return [parse_log_line(line) for line in file]
  except FileNotFoundError :
    print(f"File {log_file} not found")
  except Exception as e:
    print(f"Error: {e}")


def filter_logs_by_level(logs: list, level: str) -> list:
  return [log for log in logs if log['level'] == level]


def count_logs_by_level(logs: list, error_level: str) -> dict:
  return Counter(log['level'] for log in logs)


def display_log_counts(counts: dict, error_level="ALL"):
  print(header_of_table)
  print(separator)
  for level, count in counts.items():
    if(error_level == "ALL"):
      print(f"{level:<16} | {count:<10}")
    else:
      if(level == error_level):
        print(f"{Fore.BLUE}{level:<16}{Fore.RESET} | {count:<10}")
      else:
        print(f"{level:<16} | {count:<10}")

def display_ditails_logs(filtered_logs: list, error_level: str):
  print("\n")
  print(f"Деталі логів для рівня '{error_level}':")
  for log in filtered_logs:
    print(f"{log['date']} {log['time']} {log['level']} {log['message']}")


def parse_log(log_file: str, error_level="all") -> dict:
  logs = load_logs(log_file)
  count = count_logs_by_level(logs, error_level.upper())
  if(error_level == "all"):
    display_log_counts(count)
  else:
    display_log_counts(count, error_level.upper())
    filtered_logs = filter_logs_by_level(logs, error_level.upper())
    display_ditails_logs(filtered_logs, error_level.upper())




def main():
  path = sys.argv[1]
  error_level = sys.argv[2]
  parse_log(path, error_level)



if __name__ == "__main__":
  main()