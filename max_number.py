def find_max(numbers):
    max=numbers[0]
    for num in numbers:
        if max <= num:
            max =num
    print(f"the ma x number in the list is = {max}")