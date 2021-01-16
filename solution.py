def solution(x):
    digit1 = 3
    digit2 = 5
    larger = find_larger(x, digit1, digit2)
    return larger

def find_larger(input_number, digit1, digit2):
    while not check_for_two_digits(input_number, digit1, digit2):
        input_number += 1
    return input_number
    
def check_for_two_digits(input_number, digit1, digit2):
    allNumbers = []
    for digit in str(input_number):
        allNumbers.append(int(digit))
    for i in allNumbers:
        if ((i != digit1) and (i != digit2)):
            return False
    return True

if __name__ == "__main__":
    value = input("Please enter an integer:\n")
    value = int(value)
    print(f'You entered {value} and its closest larger number made of 3 and 5 is {solution(value)}')
