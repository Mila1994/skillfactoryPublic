def calculate_cost():
    tickets = int(input("количество билетов "))
    list_of_ages = []  # лист возрастов
    for i in range(1, tickets + 1):  # цикл по количеству билетов для ввода возраста и записи его в лист возратсов
        age = int(input("введите возраст посетителя "))
        list_of_ages.append(age)
    cost_of_tickets = 0  # переменная для общей стоимости билетов
    kid = 0  # менее 18 лет
    young = 990  # от 18 до 25 лет
    adult = 1390  # от 25 лет
    for i in list_of_ages:  # цикл определения интервала возраста и общей стоимости билетов
        if i < 18:
            cost_of_tickets = cost_of_tickets + kid
        if 25 > i >= 18:
            cost_of_tickets = cost_of_tickets + young
        if i >= 25:
            cost_of_tickets = cost_of_tickets + adult

    if tickets > 3:  # условие скидки 10%, если количество билетов больше 3
        cost_of_tickets = float(cost_of_tickets)
        cost_of_tickets = cost_of_tickets * 0.9

    print(cost_of_tickets)


if __name__ == '__main__':
    calculate_cost()
