if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    students.sort(key=lambda x: x[1])
    second_lowest_grade = sorted(set(score for name, score in students))[1]
    names_second_lowest = []
    for name, score in students:
        if score == second_lowest_grade:
            names_second_lowest.append(name)
    names_second_lowest.sort()
    for name in names_second_lowest:
        print(name)
