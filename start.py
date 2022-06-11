input("Learn_python" + " " + "Press Enter to continue...")


#   этот код полностью написан с помощью github copilot!!!
# write a program that asks for two numbers and prints the bigger one (without using if)
def bigger_number(a, b):
    if a > b:
        return a
    else:
        return b
    
# write a function that takes a list of numbers and returns the sum of the biggest and the smallest number
def sum_biggest_and_smallest(numbers):
    for number in numbers:
        if number > numbers[0]:
            numbers[0] = number
    print(numbers[0])
    
    for number in numbers:
        if number < numbers[1]:
            numbers[1] = number
    print(numbers[1])
    
    return numbers[0] + numbers[1]


print(sum_biggest_and_smallest(numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))