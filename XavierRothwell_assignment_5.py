print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: "))
step_count = 0
print("Sequence:", end=" ")
while current_number != 1:
    print(current_number, end=" ")
    if current_number % 2 == 0:
        current_number = current_number // 2

    else:
        current_number = current_number * 3 + 1
    step_count += 1
print("1")

print(f"Steps: {step_count}\n")

#Done for Second challenge Commit
print("=== Challenge 2: Prime Number Checker ===")
number = int(input("Enter a number: "))
Number_divisorStart = 2
Number_divisorEnd = number - 1
print(f"Testing divisors from {Number_divisorStart} to {Number_divisorEnd}...")
for divisor in range(Number_divisorStart, Number_divisorEnd + 1):
    if number % divisor == 0:
        print(f"{number} is not prime (divisible by {divisor})")
        break
else:
    print(f"{number} is prime!\n")

#Done for the Final Challenge Commit
print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")
print(" ", end="")

for header in range(1, 11):
    print(f"{header: 4}", end="")
print()

for row in range(1, 11):
    print(f"{row: 2}", end="")
    for column in range(1, 11):
        table_value = row * column
        print(f"{table_value: 4}", end="")
    print()
