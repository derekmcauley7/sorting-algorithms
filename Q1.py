# Write a program that reads in a file of integers, (file format: one integer per line), stores it in an array
# and times how long it takes insertionSort to sort the numbers in ascending order. The program should
# output the number of integers sorted (input size) and running time.
# Use this program to generate timings for sorting the numbers in the six files contained in folder Q1.
import time

def store_file_data_in_array(number_file):

    text_file = open(number_file, "r")
    number_array = []
    number_of_items_in_array = 0
    for number in text_file:
        number_array.append(number)
        number_of_items_in_array += 1
    text_file.close()
    print("The number of integers stored is " + str(number_of_items_in_array))
    sort_array_and_output(number_array)

def sort_array_and_output(number_array):
    start = time.time()
    for index in range(0,len(number_array)):
     currentnumber = number_array[index]
     position = index
     while position>0 and number_array[position-1]>currentnumber:
         number_array[position]=number_array[position-1]
         position = position-1
     number_array[position]=currentnumber
    end = time.time()
    print("Sorted Array : " + str(number_array))
    print("The running time for this is " +  str(end - start))

def main():
    store_file_data_in_array("1600.txt")
    store_file_data_in_array("3200.txt")
    store_file_data_in_array("6400.txt")
    store_file_data_in_array("12800.txt")
    store_file_data_in_array("25600.txt")
    store_file_data_in_array("51200.txt")

if __name__ =='__main__':
        main()
