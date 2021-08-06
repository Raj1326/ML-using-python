#Qn 1
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y
    
# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
flag  = True
while flag:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print
    else:
        flag = False

#Qn 2 Even Numbers  Variable-length argument function

def even(*t):
    lst =[]
    for i in t:
        if i%2== 0:
            lst .append(i)
    print("Even numbers:")
    for i in lst :
        print(str(i))
    
    
even(3,45,67,87,17,91,54)

#Qn 3 Even Odd Count Variable-length argument function
def count_even_odd(*t):
    count_even = 0
    count_odd = 0
    for i in t:
        if i%2== 0:
            count_even +=1
        else:
            count_odd +=1
    print("Even numbers:" +str(count_even) + "\nOdd numbers:" +str(count_odd))
    
    
count_even_odd(3,45,67,87,17,91,54)

#Qn 4 Factorial  Variable-length argument function
def factorial(*t):
    for i in t:
        fact = 1
        print("Factorial of " + str(i))
        while i :
            fact *= i
            i -=1
        print(" is " + str(fact))

factorial(3,45,67,87,17,91,54)

#Qn 5 Prime Numbers  Variable-length argument function
def prime(*t):
    lst  = []
    for i in t:
        flag = False
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    flag =True
                    break
        if (flag == False) :
            lst.append(i)
    return lst

prime_list = prime(3,45,67,87,17,91,54)
print(prime_list)

#Q6. Write a Python program to get the largest number from a list.
lst = [23,4,5,67,87,56,34,25]
print(max(lst))

#Q7. Write a Python program to remove duplicates from a list
lst = [23,4,5,67,87,23,67,56,34,23,25]
res = []
for i in lst:
    if i not in res:
        res.append(i)
print(res)
#another 7
res = list(dict.fromkeys(lst))
print(res)
#ALternate 7
print(lst)
lst = list(set(lst))
print(lst)
#Q8. Write a Python program to find the list of words that are longer than n from a given list of words
words = ["facebook", "mirosoft", "uber", "google", "netflix", "amazon"]
n = int(input("Enter n: "))
for i in words :
    if len(i) > n:
        print(i)

#Q9. Write a Python program to sum all the items in a dictionary.
dict = {'a':120,'b':300,'c':210}
def sum(dict):
    sum=0
    for i in dict :
        sum +=dict[i]
    return sum
print(sum(dict))

#Q10. Write a Python program to get the maximum and minimum value in a dictionary.
dict = {'a':120,'b':300,'c':210}
maximum = max(dict.values())
minimum = min(dict.values())
print("MAXIMUM : " + str(maximum) + "\nMINIMUM : " + str(minimum))

#Q11. Write a Python program to find the highest 3 values in a dictionary.
dict = {'a':120,'b':300,'c':210}
arr = dict.values()
print(arr)
arr.sort()
arr = arr[-1:-4:-1]
print(arr)
