import re
import sys

def convert_to_seconds(duration_str):
    # Extract numeric value from the string and convert to float
    seconds = float(re.search(r'\d+', duration_str).group())
    return seconds

def main():
    # Check if a file name is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            content = file.read()

            # Find all matches for Duration, OnDuration, and OffDuration
            durations = re.findall(r'Duration="([^"]+)"', content)
            on_durations = re.findall(r'OnDuration="([^"]+)"', content)
            off_durations = re.findall(r'OffDuration="([^"]+)"', content)

            # Convert and sum the durations
            total_seconds = sum(map(convert_to_seconds, durations + on_durations + off_durations))

            # Convert total seconds to hours, minutes, seconds
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            print(f"Total Time: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
