def minmax(arr):
    # converting items in array to integers as they inputted as strings
    for i in range(len(arr)):
        arr[i] = int(arr[i])
# initialising max and min as the first value in the array
    min = arr[0]
    max = arr[0]
# looping through every value in array to see if they can replace max or min
    for num in arr:
        if num < min:
            min = num
        if num > max:
            max = num
    return [min, max]


# user inputs a list of numbers which gets cleaned and put into an array
list = input("Enter a list of numbers separated by a comma: ")
array = list.replace(" ", "").split(",")
print(minmax(array))
