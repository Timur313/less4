def input_year_digit():
    res = None
    year_born = input("Введите год рождения А.С.Пушкина: ")
    if year_born.isdigit():
        res = year_born
    else:
        print(f"{year_born} - не является числом")
    return res

if __name__ == '__main__':

    #  Александр Сергеевич Пушкин родился в 1799г
    real_year_born = 1799
    year_born = None

    while year_born != real_year_born:
        
        year_born = input_year_digit()
        if not year_born is None:
            if int(year_born) == real_year_born:
                print("Верно")
                break
            else:
                print("Неверно")

