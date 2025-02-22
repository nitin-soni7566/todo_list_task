# The following function is inefficient. Optimize it for better performance.


# def find_duplicates(nums):
#     duplicates = []
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] == nums[j] and nums[i] not in duplicates:
#                 duplicates.append(nums[i])
#     return duplicates


def find_duplicates(nums: list) -> list:
    """
    This function takes a list of numbers and returns a list of duplicate numbers.
    """
    seen_number = set()
    duplicate = set()
    for num in nums:

        if num in seen_number:
            duplicate.add(num)
        else:
            seen_number.add(num)

    return list(duplicate)


duplicate = find_duplicates([8, 9, 8, 7, 6, 24, 3, 2, 9])

print(duplicate)
