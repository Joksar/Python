class Date:

    @classmethod
    def extract_date(cls, dmy):
        cls.dmy = dmy
        cls.dmy = cls.dmy.split(".")
        for i in range(len(cls.dmy)):
            cls.dmy[i] = int(cls.dmy[i])
        return int(cls.dmy[0]), int(cls.dmy[1]), int(cls.dmy[2])

    @staticmethod
    def valid_date(x):
        if 32 > x[0] > 0 and 13 > x[1] > 0 and type(x[2]) == int:
            print("Дата верна")
        else:
            print("Неверный формат даты.")

date = input("Введите дату в формате дд.мм.гггг: ")
date_1 = Date()
print(date_1.extract_date(date))
x = date_1.extract_date(date)
Date.valid_date(x)