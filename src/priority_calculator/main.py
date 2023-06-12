from math import floor


def main():
    subjects = []
    total_work = input("Total hours to work in the following 7 days: ").strip()
    if not total_work.isdigit() or int(total_work) > 7 * 24:
        print("\nTotal work hours invalid")
    total_work = int(total_work)

    while True:
        subject_name = input("\nEnter a subject to spend time (c to cancel): ").strip()
        if subject_name == "c":
            break

        subject_priority = input(
            f"\nEnter a priority to ({subject_name}):\n[1-5]\n>>> "
        ).strip()
        if not subject_priority.isdigit() or 1 > int(subject_priority) > 7:
            print(f"\nError add subject {subject_name}\nPriority invalid")
            continue

        subject_priority = int(subject_priority)
        subjects.append((subject_name, subject_priority))

        ops = ["yes", "no"]
        _continue = ""
        message_error = False
        while _continue.lower() not in ops:
            if message_error:
                print("\nOption error")
            _continue = input("\nDo you want to add more subjects? [yes | no]: ")
            message_error = True
        if _continue.lower() == ops[1]:
            break

    sum_priorities = total_work / sum([each[1] for each in subjects])
    print("\n\n\n")
    for each in subjects:
        subject_hours = floor(each[1] * sum_priorities)
        print(f"You should spend {subject_hours}h in {each[0]}")


if __name__ == "__main__":
    main()
