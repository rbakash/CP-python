class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = [(index,num) for index,num in enumerate(nums) if num !=0]
        # for index, num in enumerate(nums):
        #     if num != 0:
        #         self.vector.append((index, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        result = 0
        iteratorForV1, iteratorForV2 = 0, 0
        while iteratorForV1 < len(self.vector) and iteratorForV2 < len(vec.vector):
            if self.vector[iteratorForV1][0] < vec.vector[iteratorForV2][0]:
                iteratorForV1 += 1
            elif self.vector[iteratorForV1][0] > vec.vector[iteratorForV2][0]:
                iteratorForV2 += 1
            else:
                result += self.vector[iteratorForV1][1] * vec.vector[iteratorForV2][1]
                iteratorForV1 += 1
                iteratorForV2 += 1

        return result


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
