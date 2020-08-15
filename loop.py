#测试一下拉取
odd_sum = 0
for number in range(1,1000):
    if number % 2 == 1:
        odd_sum += number
print(odd_sum)

even_sum = 0
for number in range(1,1000):
    if number % 2 == 0:
        even_sum += number
print(even_sum)



composite_number_sum = 0
for number in range(2,1000):
    for _ in range(2,number):
        if number % _ == 0:
            composite_number_sum += number
            break
print(composite_number_sum)



prime_number_sum = 0
for number in range(2, 1000):
    for k in range(2,number+1):
        if number % k != 0:
           continue
        elif number % k == 0 and number == k:
            prime_number_sum += number
            print(number)
        else:
            break
print(prime_number_sum)



