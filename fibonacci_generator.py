import csv

n = int(input("Enter the number you want to generate fibonacci series : "))

fibonacci_cache = {}

def fibonacci(n):
    # If we have cached the value, tehn return it 
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # Cache the value and return it 
    fibonacci_cache[n] = value
    return value

for i in range (1,n+1):
    print(i,":", fibonacci(i))


# Output is sotred in json file

with open("fibonacci_output.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Position", "Fibonacci Number"])
    for i in range(1,n+1):
        fib = fibonacci(i)
        print(f"{i} : {fib}")
        writer.writerow([i,fib])

print("Fibonacci Series saved to 'fibonacci_output.csv'")

