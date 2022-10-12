def bubble_Sort(array_of_numbers):
    for i in range(len(array_of_numbers) - 1):
        for j in range(0, len(array_of_numbers) - i - 1):
            if array_of_numbers[j] > array_of_numbers[j+1]:
                array_of_numbers[j], array_of_numbers[j+1] = \
                    array_of_numbers[j+1], array_of_numbers[j]
    return array_of_numbers


array_of_numbers = [1, 0, 4, 20, 5, 639, 7, 3, 9] #Example of an array
print(bubble_Sort(array_of_numbers))