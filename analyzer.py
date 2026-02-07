from collections import Counter

LOG_FILE = "app.log"


def read_logs():
    with open(LOG_FILE, "r") as f:
        return f.readlines()
    

def count_levels(lines):
    counter = {
        "INFO": 0,
        "DEBUG": 0,
        "ERROR": 0,
        "WARNING": 0
    }

    for line in lines:
        low = line.lower()

        if "info" in low:
            counter["INFO"] += 1
        elif "debug" in low:
            counter["DEBUG"] += 1
        elif "error" in low:
            counter["ERROR"] += 1
        elif "warning" in low:
            counter["WARNING"] += 1

    return counter


def show_errors(lines):
    print("\nError logs:\n")
    for line in lines:
        if "ERROR" in line:
            print(line.strip())


def save_report(counter):
    with open("report.txt", "w") as f:
        for key, value in counter.items():
            f.write(f"{key}: {value}\n")


def main():
    lines = read_logs()

    print("Total logs:", len(lines))

    counter = count_levels(lines)
    print("\nLog Summary:")
    print("INFO:", counter["INFO"])
    print("DEBUG:", counter["DEBUG"])
    print("ERROR:", counter["ERROR"])
    print("WARNING:", counter["WARNING"])

    print("\n")
    show_errors(lines)
    
    save_report(counter)

    print("\nReport saved to report.txt")


if __name__ == "__main__":
    main()