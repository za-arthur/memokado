import argparse
import csv
import random

def get_dictionary_randomly(file_name, num_items):
    rows = []

    if num_items == 0:
        return rows

    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_data = list(csv_reader)

        sample = random.sample(range(0, len(csv_data)), num_items)
        for idx in sample:
            rows.append(csv_data[idx])

    return rows

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Memory cards")
    parser.add_argument("-f", "--file_name", default="vocabulary.csv")
    parser.add_argument("-n", "--num_items", type=int, default=20)
    args = parser.parse_args()

    rows = get_dictionary_randomly(args.file_name, args.num_items)

    for row in rows:
        sample = [r for r in row if r]
        if len(sample) == 0:
            continue
        term_to_check = random.choice(sample)

        print("")
        print(term_to_check, end=":\n")
        answer = input().lower()

        print(", ".join(r for r in sample if r != term_to_check), end="")

        if answer != term_to_check.lower() and answer in (s.lower() for s in sample):
            print(" - CORRECT", end="")
        print("")
