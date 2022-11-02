




















































#L6bs
A=[]
for v in range (1,8):
    A.append(int(input("Enter a number: ")))
print(A)

def bubblesort(A):
    n = len(A)
    for i in range(1,n):
        for j in range(1,n-i+1):
            if A[j]  <A[j-1]:
                A[j], A[j-1] = A[j-1],A[j]
bubblesort(A)
print("Sorted array: ")
print(A)

        











































        
#L7is
A= []
n= 9

for i in range(0,n):
    number = int(input("Enter a number: "))
    if(number>10 and number<20):
        A.append(number)
    else:
        print("Invalid number: ")
    i+i+1

print(A)

def Insertionsort(A):

    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j>=0 and key<A[j]:
            A[j+1]=A[j]
            j=j-1
            A[j+1] = key
            
Insertionsort(A)
print("Sorted Array", A)











































#L8ss
A=[]
for v in range(8):
    A.append(int(input('Enter a number: ')))

print(A)

def selectionSort(A):
    n = len(A)
    for j in range(0,n-1):
        smallest = j
        for i in range(j+1,n):
            if A[i]<A[smallest]:
                smallest = i
            A[j],A[smallest] = A[smallest], A[j]
            
selectionSort(A)
print('Sorted Array: ', A)









































#L8qs
arr=[]
for v in range(7):
    arr.append(input("Enter a number: "))
    print(arr)

def partition(arr,low,high):
    i=(low-1)
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return(i+1)
def quickSort(arr,low,high):
    if low<high:
        q = partition(arr,low,high)
        quickSort(arr,low,q-1)
        quickSort(arr,q+1,high)
quickSort(arr,0,len(arr)-1)
print("Sorted Array: ")
for i in range(len(arr)):
    print(arr[i])















