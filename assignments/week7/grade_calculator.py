from sys import argv
import csv
import random

WEEKS = [f"Week {i}" for i in range(1, 14) if i != 6]
MAX_SCORE = 3
students = []

# Step 1
def read_csv(filename):
    # load csv to variables in your program
    # handle file exceptions here
    try:
        with open(filename) as f:
            for line in f:
                print(line)
    except FileNotFoundError:
        print("CVS file was not found.")
    except PermissionError:
        print("No permission to access the file.")

# Step 2
def populate_scores(filename):
    global students
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        students = [row for row in reader]

    for student in students:
        for week in WEEKS:
            value = student.get(week, "").strip().lower()
            if value in ('', 'nan', '-', None):
                # 10% chance of no submission
                student[week] = '' if random.random() < 0.1 else str(random.randint(0, MAX_SCORE))
            else:
                try:
                    # Convert float strings like '3.0' to int
                    score = float(value)
                    student[week] = str(int(score))
                except ValueError:
                    student[week] = ''  # Set invalid values to empty
# read csv and add randomized numbers (0-3)

# Step 3
def calculate_all():
    for student in students:
        scores = []
        for week in WEEKS:
            value = student.get(week, '').strip()
            if value.isdigit():
                scores.append(int(value))
        student["Total Points"] = calculate_total(scores)
        student["Average Points"] = calculate_average(scores)
    # loop through all the students and calculate grades

def calculate_total(scores):
    # Best 10 scores, capped at 30
    return min(sum(sorted(scores, reverse=True)[:10]), 30)

def calculate_average(scores):
    return round(sum(scores) / len(scores), 2) if scores else 0.0

# After the update let's save the data as a new csv file

def write_csv(new_filename):
    if not students:
        print("No data to write.")
        return
    fieldnames = list(students[0].keys())
    with open(new_filename, mode='w', newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
    print("Updated CSV saved as:", new_filename)

# Bonus

def print_analysis():
    # print average scores for stream A, B and every week
    pass

if __name__ == "__main__":
    script, filename = argv

    print("Opening file:", filename)

    read_csv(filename)

    populate_scores(filename)
    calculate_all()

    user_name = input("What's your user name?")

    newname = filename.split(".")[0] + "_calculated_by_" + user_name + ".csv"
    write_csv(newname)
    print("New file written:", newname)

    print_analysis()

# Run the file with `python grade_calculator.py sheet.csv`