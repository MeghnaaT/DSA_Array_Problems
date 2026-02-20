# Find the Leader Elements: An element is a leader if it is greater than all elements to its right.

def leader_element(self, arr):
    max_right = float('-inf')
    result = []
    for num in reversed(arr):
        if num > max_right:
            result.append(num)
            max_right = num
    return result[::-1]