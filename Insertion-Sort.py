def insertion_Sort(array_of_numbers):
    for j in range(0, len(array_of_numbers)):
        key = array_of_numbers[j]
        i = j - 1
        while i > 0 and array_of_numbers[i] > key:
            array_of_numbers[i+1] = array_of_numbers[i]
            i = i - 1
        array_of_numbers[i+1] = key
    return array_of_numbers


array_of_numbers = [1, 4, 20, 5, 7, 3, 9] #Example of an array
print(insertion_Sort(array_of_numbers))
