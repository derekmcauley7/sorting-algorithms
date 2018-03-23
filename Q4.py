# Write a program that reads in the file 102400.txt and stores it in an array of integers. The program
# should use this array to create smaller sub-arrays of size 6400, 12800, 25600, 51200, 102400 and find
# the average time for both quickSort and mergeSort to sort each i.e. each algorithm should run five
# times on each sub-array (loops should be used).
import time

def store_file_data_in_arrays(number_file):

    text_file = open(number_file, "r")
    number_array = []
    number_of_items_in_array = 0
    for number in text_file:
        number_array.append(number)
        number_of_items_in_array += 1
    text_file.close()
    print("Main Array created with " + str(number_of_items_in_array) + " integers.")
    number_array6400 = []
    number_array12800 = []
    number_array25600 = []
    number_array51200 = []
    number_array102400 = []

    for i in range(len(number_array)):
        if(i < 6400):
            number_array6400.append(number_array[i])
            number_array12800.append(number_array[i])
            number_array25600.append(number_array[i])
            number_array51200.append(number_array[i])
            number_array102400.append(number_array[i])
        elif(i < 12800):
            number_array12800.append(number_array[i])
            number_array25600.append(number_array[i])
            number_array51200.append(number_array[i])
            number_array102400.append(number_array[i])
        elif(i < 25600):
            number_array25600.append(number_array[i])
            number_array51200.append(number_array[i])
            number_array102400.append(number_array[i])
        elif(i < 51200):
            number_array51200.append(number_array[i])
            number_array102400.append(number_array[i])
        else:
            number_array102400.append(number_array[i])
    startQuick = time.time()
    run_5_times(quick_sort(number_array6400))
    run_5_times(quick_sort(number_array25600))
    run_5_times(quick_sort(number_array12800))
    run_5_times(quick_sort(number_array51200))
    run_5_times(quick_sort(number_array102400))
    endQuick = time.time()
    totalTimeQuickSort = ((endQuick - startQuick) / 5) / 5
    print("The average time for quick sort is " + str(totalTimeQuickSort))

    startMerge = time.time()
    run_5_times(merge_sort(number_array6400))
    run_5_times(merge_sort(number_array25600))
    run_5_times(merge_sort(number_array12800))
    run_5_times(merge_sort(number_array51200))
    run_5_times(merge_sort(number_array102400))
    endMerge = time.time()
    totalTimeMergeSort = ((endMerge - startMerge) / 5) / 5
    print("The average time for merge sort is " + str(totalTimeMergeSort))


def run_5_times(array):
    i = 0
    while i < 5:
        array
        i += 1


def quick_sort(number_array):
    quick_sort_helper(number_array, 0, len(number_array) - 1)

def quick_sort_helper(number_array, first, last):
   if first < last:
       splitpoint = split_array(number_array, first, last)
       quick_sort_helper(number_array, first, splitpoint - 1)
       quick_sort_helper(number_array, splitpoint + 1, last)


def split_array(number_array, first, last):
   pivotvalue = number_array[first]
   leftNumber = first+1
   rightNumber = last
   done = False
   while not done:
       while leftNumber <= rightNumber and number_array[leftNumber] <= pivotvalue:
           leftNumber = leftNumber + 1

       while number_array[rightNumber] >= pivotvalue and rightNumber >= leftNumber:
           rightNumber = rightNumber -1

       if rightNumber < leftNumber:
           done = True
       else:
           temp = number_array[leftNumber]
           number_array[leftNumber] = number_array[rightNumber]
           number_array[rightNumber] = temp

   temp = number_array[first]
   number_array[first] = number_array[rightNumber]
   number_array[rightNumber] = temp
   return rightNumber



def merge_sort(array):
    if len(array) <=1:
        return array
    midpoint = int(len(array) / 2)
    left, right = merge_sort(array[:midpoint]), merge_sort(array[midpoint:])

    return merge(left, right)

def merge(left, right):

    result = []

    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):

        if left[left_pointer] < right[right_pointer]:

            result.append(left[left_pointer])
            left_pointer+=1

        else:
            result.append(right[right_pointer])
            right_pointer +=1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result


def main():
    store_file_data_in_arrays("102400.txt")

if __name__ =='__main__':
        main()
