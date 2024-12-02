
def is_increasing(numbers: list[int]) -> bool:
    for index in range(len(numbers) - 1):
        if numbers[index] >= numbers[index + 1]:
            return False
    return True

def is_decreasing(numbers: list[int]) -> bool:
    for index in range(len(numbers) - 1):
        if numbers[index] <= numbers[index + 1]:
            return False
    return True


def is_valid_report(report: str) -> bool:
    numbers = list(map(int, report.split()))
    for index in range(len(numbers) - 1):
        diff = abs(numbers[index] - numbers[index + 1])
        if diff not in (1, 2, 3):
            return False

    if is_increasing(numbers) or is_decreasing(numbers):
        return True
    else:
        return False

def main():
    with open("data.txt", "r") as file:
        reports = file.readlines()

    valid_reports = 0
    for report in reports:
        if is_valid_report(report):
            valid_reports += 1
    print(valid_reports)



if __name__ == "__main__":
    main()
