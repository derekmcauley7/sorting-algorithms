# Write a program that counts how many times quickSort is called when sorting the numbers in the file
# 102400.txt.
import time

def store_file_data_in_arrays(number_file):

    text_file = open(number_file, "r")
    number_array = []
    number_of_items_in_array = 0
    for number in text_file:
        number_array.append(number)
        number_of_items_in_array += 1
    text_file.close()

    quick_sort(number_array)
    # using quick_sort_helper as this is the recursive function. Using a wrapper to counter the calls
    print("The number of calls to the function is " + str(quick_sort_helper.calls))

def wrap_counter(item):
    def wrapped(*args, **kwargs):
        wrapped.calls += 1
        return item(*args, **kwargs)
    wrapped.calls = 0
    return wrapped

def quick_sort(number_array):
    quick_sort_helper(number_array, 0, len(number_array) - 1)

@wrap_counter
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



def main():
    store_file_data_in_arrays("102400.txt")

if __name__ =='__main__':
        main()
