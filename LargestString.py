def largestWord(strings):
    # Sort the words in increasing
    # order of their lengths
    strings = sorted(strings, key=len)
    # Print last word
    return (strings[-1])
print(largestWord(list(input().split(" "))))