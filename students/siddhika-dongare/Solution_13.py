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
