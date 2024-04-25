# "Given two strings s and t, return true if t is an anagram of s, and false otherwise. 
# "An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase
# "typically using all the original letters exactly once." - LeetCode

# case 1
s = "anagram"
t = "nagaram"

# case 2
# s = "rat"
# t = "car"

# solution with built in sort function
def isAnagram(s: str, t: str) -> bool:

    if (len(s) != len(t)):
        return False
    else:
        s = sorted(s)
        t = sorted(t)

    if s == t:
        return True
    else:
        return False
    
# solution without built in sorted function --> using bubble sort
def isAnagram2(s: str, t: str) -> bool:

    def sort(string: str):
        arr = list(string)
        length = len(string)
        
        for i in range(length):
            for j in range(i+1, length):
                if arr[i] >= arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp

        return ''.join(arr)


    if (len(s) != len(t)):
        return False
    else:
        s = sort(s)
        t = sort(t)

    if s == t:
        return True
    else:
        return False