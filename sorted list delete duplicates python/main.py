# Удалить дубликаты из отсортированного массива



# Входные данные: nums = [1,1,2]
#  Выходные данные: 2, nums = [1,2,_]
#  Объяснение: Ваша функция должна возвращать k = 2, причем первые два элемента nums равны 1 и 2 соответственно.
# Не имеет значения, что вы оставите после возвращенного k (следовательно, они являются подчеркиванием).

class RemoveDuplicatesFromSortedArray:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Length of the update array
        count = 0
        # Loop for all the elements in the array
        for i in range(len(nums)):
            # If the current element is equal to the next element, we skip
            if i < len(nums) - 2 and nums[i] == nums[i + 1]:
                continue
            # We will update the array in place
            nums[count] = nums[i]
            count += 1
        return count

        