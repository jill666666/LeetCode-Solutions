def median_of_those_two(nums1, nums2):

    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    start, end = 0, len(nums1) - 1

    partitionX = int((start + end) / 2)
    partitionY = int((len(nums1) + len(nums2) + 1) / 2 - partitionX)
    print('partitions', partitionX, partitionY)

    while True:
        if nums1[partitionX - 1] < nums2[partitionY] and nums2[partitionY - 1] < nums1[partitionX]:

            print(nums1[partitionX - 1], 'and', nums1[partitionX])
            print(nums2[partitionY - 1], 'and', nums2[partitionY])
            if (len(nums1) + len(nums2)) % 2 == 0:
                return (max(nums1[partitionX - 1], nums2[partitionY - 1]) + min(nums1[partitionX], nums2[partitionY])) / 2
            else:
                return max(nums1[partitionX - 1], nums2[partitionY - 1])
        else:
            start += 1
            partitionX = int((start + end) / 2)
            partitionY = int((len(nums1) + len(nums2) + 1) / 2 - partitionX)
            print('partitions', partitionX, partitionY)
            print(partitionX, nums1[:partitionX], nums1[partitionX:])
            print(partitionY, nums2[:partitionY], nums2[partitionY:])

# nums1 = [1, 3, 8, 9, 15]
# nums2 = [7, 11, 18, 19, 21, 25]

nums1 = [23, 26, 31, 35]
nums2 = [3, 5, 7, 9, 11, 16]

print(median_of_those_two(nums1, nums2))
