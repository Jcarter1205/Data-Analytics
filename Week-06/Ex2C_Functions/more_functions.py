
# Exercise 2.C Creating and Calling Functions
# Lab 2: More Custom Functions

# Function 1: Display a mailing label
def display_mailing_label(name, address, city, state, zip):
    print(name)
    print(address)
    print(f"{city}, {state} {zip}")


# Test mailing label with two different people
display_mailing_label("Jada Carter", "123 Main Street", "Philadelphia", "PA", "19103")

print()

display_mailing_label("Anna Smith", "456 Oak Avenue", "Boston", "MA", "02108")


# Function 2: Add any number of numbers
def add_numbers(*args):
    total = sum(args)
    numbers = " + ".join(str(number) for number in args)
    print(f"{numbers} = {total}")


# Test adding numbers three times
print()
add_numbers(10)
add_numbers(10, 20)
add_numbers(10, 20, 30, 40)


# Function 3: Display a receipt
def display_receipt(total_due, amount_paid):
    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")

    if amount_paid > total_due:
        change = amount_paid - total_due
        print(f"Change Due: ${change:.2f}")

    elif amount_paid == total_due:
        print("Change Due: $0.00")

    else:
        balance = total_due - amount_paid
        print(f"Remaining Balance: ${balance:.2f}")


# Test receipt 1: Customer overpays
print()
display_receipt(45.50, 50.00)

# Test receipt 2: Customer pays the exact amount
print()
display_receipt(45.50, 45.50)

# Test receipt 3: Customer underpays
print()
display_receipt(45.50, 40.00)
