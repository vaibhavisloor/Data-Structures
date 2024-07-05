def linearSearch(arr,key):

    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1    

if __name__ == "__main__":

    array = [2,5,3,8,6,9,1]

    find = linearSearch(array,1)

    if find == -1:
        print("Number wasnt found")
    else:
        print(f"Number was found at index {find}")

