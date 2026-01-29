n = int(input("Enter your number : "))

fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0

for i in range(1, n + 1):
    if i % 15 == 0:
        print("FizzBuzz")
        fizzbuzz_count += 1
    elif i % 3 == 0:
        print("Fizz")
        fizz_count += 1
    elif i % 5 == 0:
        print("Buzz")
        buzz_count += 1
    else:
        print(i)

print("\nSummary:")
print(f"Fizz: {fizz_count}")
print(f"Buzz: {buzz_count}")
print(f"FizzBuzz: {fizzbuzz_count}")
