case1 = [1,2,3,1]
case2 = [1,2,3,4]
case3 = [1,1,1,3,3,4,3,2,4,2]

# simplified solution
def containsDuplicate1(nums:list[int]) -> bool:
    nums.sort()

    # finding the duplicate
    for i in range(len(nums)):
        if i != len(nums)-1:
            if nums[i] == nums[i+1]:
                return True

    return False


# solution without built in sort function
def containsDuplicate2(nums:list[int]) -> bool:

    # sorting a list using loops
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] >= nums[j]:
                # swap the values
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

    # finding the dublicate
    for i in range(len(nums)):
        if i != len(nums)-1:
            if nums[i] == nums[i+1]:
                return True

    return False


# printing the results
print(containsDuplicate1(case3))
print(containsDuplicate2(case3))


