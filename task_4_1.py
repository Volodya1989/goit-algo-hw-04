from pathlib import Path


def total_salary(path: str) -> tuple:
    path = Path(path).resolve()
    # checking if file exists
    if not path.exists():
        print(
            f"The file {path} does not exist.\n Please provide valid file or path.")
        return (0, 0)

    salaries = []
    # reading the file and extracting salaries
    with open(path, 'r', encoding='utf-8') as fh:
        for line in fh:
            try:
                # splitting line into name and salary
                _, salary = line.strip().split(',')
                salaries.append(int(salary))
            except ValueError as e:
                print(f'Error occured: {e}')

    if not salaries:
        print(f'No salaries were found')
        return (0, 0)
    else:
        total_salary = sum(salaries)
        average_salary = total_salary//len(salaries)
        print(
            f'Total salary is {total_salary} and avarage salary is {average_salary}.')
        return total_salary, average_salary


print(total_salary('./salary.txt'))
