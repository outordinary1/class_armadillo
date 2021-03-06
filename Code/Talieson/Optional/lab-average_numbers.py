
# This lab allows the user to find the average of a set of numbers.
# Version 2 allows the user to input the list of numbers, rather then
# taking flat values.
# Version 3 adds median functionality.
# Version 4 adds mode functionality.


# This function finds the mean by taking the sum of a list of numbers
# and dividing by the amount of numbers in that list.
def mean(nums):
    return sum(nums) / len(nums)


# This function finds the median of a list of numbers
def median(nums):
    # here we define the amount of numbers in the list and sort ascending
    nums = sorted(nums)
    size = len(nums)
    # this defintes the middle index if the list is an odd number.
    # if it's not it takes the left of the middle two index.
    index = (size - 1) // 2
    # if the list is odd, just return the middle number
    if size % 2:
        return nums[index]
    # else, average the number at index, and the number to it's right
    else:
        return nums[index] + nums[index + 1] / 2


# This function finds the mode of a list of numbers
def mode(nums):
    # establish an empty library
    output = {}
    # iterate through the numbers.
    for num in nums:
        # if the number isn't in the library key, add it with value 1
        if num not in output:
            output[num] = 1
        # if the key is in the library, add 1 to it's value
        else:
            output[num] += 1
    # return the value of the key of output with the highest value
    return max(output, key=output.get)


# definte global variables
run = True
list_finished = False
operation = False
nums_list = []

# main run loop
while run:
    # check if the user has input done, if not keep taking numbers.
    while not list_finished:
        # check that we've got the operation from the user.
        while operation not in ("mean", "median", "mode"):
            operation = input(
                "Do you want to find a mean, median or mode? "
                ).lower().strip()

        # take input from user
        num = input("Enter a num to add to list, enter done to proceed. ")
        # if that input is a number
        if num.isdigit():
            # make it an integer, put it in our list, and show what we've got
            num = int(num)
            nums_list.append(num)
            print(nums_list)
        # if the user enters done, lets move on
        elif num == "done":
            list_finished = True
        else:
            print("that is not a valid response.")

    # call the correction function depending on which operator they've picked
    if operation == "mean":
        print(mean(nums_list))
    elif operation == "mode":
        print(mode(nums_list))
    elif operation == "median":
        print(median(nums_list))

    run = False
    nums_list = []
    checkin = input("Do you want to operate on another list? (Y/N) ")
    if checkin == "Y":
        run = True
        list_finished = False
        operation = False
