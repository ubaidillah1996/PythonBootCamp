#Exercise 1 : write function check is prime or not

def get_primes(limit):
    primes = []

    for num in range(2, limit + 1):
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes

print(get_primes(77))

# Exercise 2 : Build a temperatur converter function (cel to fah)

# Formula : F = (C × 9/5) + 32

def celcius_to_fahrenheit(celcius):
    return(celcius * 9/5) + 32

temp = float(input("Enter Temp to celcius: "))
print("Fahrenheit:", celcius_to_fahrenheit(temp))