import math


def num_type (nums):
    num_type_dict = {
        'Even': 0,
        'Odd': 0,
        'Prime': 0,
        'Non-Prime': 0,
        'Zero-Count': 0
    }
    for i in nums:
        if i % 2 == 0:
            num_type_dict['Even'] += 1
        else:
            num_type_dict['Odd'] += 1
        prime = 1
        if i == 0:
            num_type_dict['Zero-Count'] += 1
        else:
            r = int(math.sqrt(i))
            for j in range(2, r + 1):
                if i % j == 0:
                    prime = 0
                    break
            if prime == 1:
                num_type_dict['Prime'] += 1
            else:
                num_type_dict['Non-Prime'] += 1
    return num_type_dict


n = int(input("Enter the size of the numbers list: "))
print("Enter " + str(n) + " numbers")
numbers = [int(input()) for i in range(0, n)]
print(numbers)
type_of_numbers = num_type(numbers)
for key, value in type_of_numbers.items():
    print(str(key) + " : " + str(value))
print("There are " + str(type_of_numbers['Zero-Count']) + " zeroes.")
print("They are not included in either PRIMES or NON_PRIMES")
