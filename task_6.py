# task 6
a = int(input("Введите кол-во километров первого дня: "))
b = int(input("Введите кол-во желаемого результата: "))

days = 1
while a < b:
    a = a + (a * 0.1)
    days = days + 1

print(f"На {days}-й день спортсмен достигнет результата - не менее {b} км")
