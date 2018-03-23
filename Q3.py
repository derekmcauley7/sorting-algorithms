# Write a program that reads in the file 102400.txt, stores it in an array of integers and repeatedly (5
# times) generates a timing for how long it takes insertionSort to sort it - a loop should be used for this.
# The program should print the number of integers sorted (input size) and average time it takes to sort
# the file
import time

def store_file_data_in_array(number_file, counter):

    text_file = open(number_file, "r")
    number_array = []
    number_of_items_in_array = 0
    for number in text_file:
        number_array.append(number)
        number_of_items_in_array += 1
    text_file.close()
    print("The number of integers stored is " + str(number_of_items_in_array))
    sort_array_and_output(number_array, counter)


def sort_array_and_output(number_array, counter):
    start = time.time()
    for index in range(0,len(number_array)):
     currentnumber = number_array[index]
     position = index
     while position>0 and number_array[position-1]>currentnumber:
         number_array[position]=number_array[position-1]
         position = position-1
     number_array[position]=currentnumber
    end = time.time()
    print("For run number " + str(counter) + " the running time for this is " +  str(end - start))

def main():
    counter = 1
    start = time.time()
    while counter < 6:
        print("Running insertionSort number " + str(counter) + ", this may take some time...")
        store_file_data_in_array("102400.txt", counter)
        counter +=1

    end = time.time()
    average_time = (end - start) / 5

if __name__ =='__main__':
        main()
