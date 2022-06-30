
def print_hi():
    # Исходные данные
    per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
    # Ввод пользователем суммы вклада
    money = input("введите сумму вклада ")
    # Функция для расчета накоплений за год по ставке rate на сумму money
    def count_deposit(rate):
        return int(int(money) * rate / 100)
    # Из словаря исходных данных берем список значений
    rates = per_cent.values()
    # Вычисляем по ставкам rates для каждого банка накопления за год и записывает результат в list
    deposit = list(map(count_deposit, rates))
    print(deposit)
    print("Максимальная сумма, которую вы можете заработать-", max(deposit))

if __name__ == '__main__':
    print_hi()
