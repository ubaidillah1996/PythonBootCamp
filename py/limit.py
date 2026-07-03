limit = int(input("Enter the limit (max 20): "))

# prime number bermaksud : nombor yang susah nak dibahagi. Selain 1 dan dirinya sendiri, tak ada nombor lain yang boleh bahagi habis.


# how its works ?
# 1. loop dari 2 sampai limit
# 2. setiap nombor , cek sama ada boleh dibahagi dengan nombor lain selain 1 dan sendiridirinya 
# 3. kalau boleh bahagi (% == 0) , bukan prime number.
# 4. kalau tak boleh bahagi dengan nombor lain, prime number.


print("Prime numbers up to ", limit, ":")

for num in range(2, limit + 1):
    is_prime = True  # Nombor tu Prime

    for i in range(2, num):
        if num % i == 0:
            is_prime = False  # Nombor tu bukan Prime
            break
    if is_prime:
        print(num)