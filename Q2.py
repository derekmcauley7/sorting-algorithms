# Write a program that reads in the 3 files in folder Q2 and generates timings for sorting them using
# insertionSort.
import time

def store_file_data_in_arrays(array_of_files):
    unsortedArray = []
    for currentFileNumber in range(0, len(array_of_files)):
        text_file = open(array_of_files[currentFileNumber], "r")
        number_of_items_in_array = 0
        for number in text_file:
            unsortedArray.append(number)
            number_of_items_in_array += 1
        text_file.close()
        print("The number of integers stored in Array " + str(currentFileNumber + 1) + " is : " + str(number_of_items_in_array))
        sort_time_and_print_array(unsortedArray)

def sort_time_and_print_array(number_array):

    start = time.time()

    for index in range(0, len(number_array)):
     currentnumber = number_array[index]
     position = index
     while position > 0 and number_array[position-1] > currentnumber:
         number_array[position] = number_array[position-1]
         position = position-1
     number_array[position] = currentnumber

    end = time.time()
    print("Sorted Array : " + str(number_array))
    print("The running time for this is " +  str(end - start))

def main():
    fileNames = ["Q2a.txt", "Q2b.txt", "Q2c.txt"]
    store_file_data_in_arrays(fileNames)

if __name__ =='__main__':
        main()
