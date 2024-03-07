code_dict = {
    "A": 1, "B": 2, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2,
    "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1,
    "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1,
    "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10
}

def separate_letters_and_numbers(text):
    letters = []
    numbers = []
    for char in text:
        if char.isalpha():
            letters.append(char)
        elif char.isdigit():
            numbers.append(int(char))
    
    print("Letters:", letters)
    print("Numbers:", numbers)

def calculate_sum_of_numbers(numbers):
    total = sum(numbers)
    print("Tổng các số là:", total)

def convert_text_to_numbers(text):
    text = text.upper()
    result = [str(code_dict[char]) if char.isalpha() and char in code_dict else char for char in text]
    result_text = "".join(result)
    print("Chuiyển chuỗi sang số là:", result_text)
input_text = "Gia Dinh University"
separate_letters_and_numbers(input_text)
numbers_list = [code_dict[char] for char in input_text if char.isalpha() and char in code_dict]
calculate_sum_of_numbers(numbers_list)
convert_text_to_numbers(input_text)