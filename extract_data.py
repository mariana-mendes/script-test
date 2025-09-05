import os
import re
import csv

def extract_iperf_data(log_folder, output_csv):
    pattern = re.compile(
        r"\[\s*\d+\]\s+\S+\s+sec\s+([\d.]+\s+\w+)\s+([\d.]+\s+\w+/sec)\s+(\d*)\s*(sender|receiver)"
    )

    header = ["Filename", "Transfer", "Bitrate", "Retr", "Classification"]

    with open(output_csv, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)

        for fname in os.listdir(log_folder):
            if not fname.lower().endswith(".txt"):
                continue  # process only .txt files

            filepath = os.path.join(log_folder, fname)
            with open(filepath, "r") as file:
                lines = file.readlines()

            results = []
            for line in reversed(lines):
                match = pattern.search(line)
                if match:
                    transfer = match.group(1)
                    bitrate = match.group(2)
                    retr = match.group(3) if match.group(3) else "0"
                    classification = match.group(4)
                    results.append((transfer, bitrate, retr, classification))

            if results:
                for res in reversed(results[:2]):  # sender and receiver lines
                    writer.writerow([fname] + list(res))

if __name__ == "__main__":
    log_folder = "."  # folder with your .txt log files
    output_csv = "iperf_summary.csv"
    extract_iperf_data(log_folder, output_csv)
    print(f"Data extracted to {output_csv}")
