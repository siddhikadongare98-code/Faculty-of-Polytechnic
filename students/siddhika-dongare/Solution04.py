#problem1
def countdown(n):
    while n >= 1:
        print(n)
        n = n - 1
    print("Liftoff!")

# Example
countdown(5)

#problem2
def first_multiple(n, start):
    x = start

    while True:
        if x % n == 0:
            break
        x = x + 1

    return x

# Example
print(first_multiple(5, 12))


#problem3
def print_triangle(height):
    row = 1
    while row <= height:
        print("*" * row)
        row += 1

# Example
print_triangle(5)

#problem4
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

#problem5

secret = 7

def play_game(i):   
    while True:     
        if i == secret:
            print("correct")
            break
        else:
            print("incorrect")
            break 
play_game(7)
#problem8
total = 0

def add_item(price):
    global total
    total += price
    return total

def apply_tax():
    return total * 1.05

def main():
    add_item(40)
    add_item(25)
    add_item(15)

    print(f"Items added. Cart total: {total}")
    print(f"With 5% tax: {apply_tax():.2f}")

if __name__ == "__main__":
    main()
