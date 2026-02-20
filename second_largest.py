def second_largest(self, arr):
    first = second= float('-inf')
    for num in arr:
        if num> first:
            second = first
            first = num
        elif first>num>second:
            second = num
    return second
