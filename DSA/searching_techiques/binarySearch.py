#Python implementation of binarysearch


# def binary_search(numbers_list, number_to_find):
#     left_index = 0
#     right_index = len(numbers_list) - 1
#     mid_index = 0

#     while left_index <= right_index:
#         mid_index = (left_index + right_index) // 2
#         mid_number = numbers_list[mid_index]

#         if mid_number == number_to_find:
#             return mid_index

#         if mid_number < number_to_find:
#             left_index = mid_index + 1
#         else:
#             right_index = mid_index - 1

#     return -1

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

if __name__ == '__main__':
    numbers_list = [40 , 58 , 70 , 65 , 23 , 90 , 69]
    number_to_find = 65

    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    print(f"Number found at index {index} using binary search")