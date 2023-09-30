import sys
import re

def convert_to_seconds(time_str):
    # Convert time string to seconds
    hours, minutes, seconds = map(int, time_str.split(":"))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            content = file.read()

            # Use regular expressions to find and extract durations
            durations = re.findall(r'Duration="(\d+:\d+:\d+)"', content)

            # Convert durations to seconds and sum them
            total_seconds = sum(map(convert_to_seconds, durations))

            # Convert total seconds to hours, minutes, seconds
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            print(f"Total Time: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
