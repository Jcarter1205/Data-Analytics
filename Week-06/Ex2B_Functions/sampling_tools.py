import random
products = [
    'Laptop',
    'Monitor',
    'Keyboard',
    'Mouse',
    'Webcam',
    'Headset',
    'Docking Station',
    'USB Hub',
    'Desk Lamp',
    'Surge Protector'
]
# Select one random product
product_of_the_day = random.choice(products)

print(f"Product of the Day: {product_of_the_day}")
# Select three products without repetition
survey_products = random.sample(products, 3)

print(f"Products selected for survey: {survey_products}")
# Shuffle the product list
random.shuffle(products)

print(f"Shuffled products: {products}")
# Generate a random daily transaction count
daily_transactions = random.randint(50, 300)

print(f"Daily transaction count: {daily_transactions}")