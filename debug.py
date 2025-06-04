from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")
carol = Customer("Carol")

# Create coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")
cappuccino = Coffee("Cappuccino")

# Create orders
alice.create_order(latte, 3.5)
alice.create_order(latte, 4.0)
bob.create_order(latte, 2.5)
bob.create_order(espresso, 2.0)
carol.create_order(cappuccino, 5.0)

# Customer orders
print(f"Alice's orders: {alice.orders()}")
print(f"Bob's orders: {bob.orders()}")

# Unique coffees each customer ordered
print(f"Alice's coffees: {[coffee.name for coffee in alice.coffees()]}")
print(f"Bob's coffees: {[coffee.name for coffee in bob.coffees()]}")

# Coffee's total orders
print(f"Latte num_orders: {latte.num_orders()}")
print(f"Espresso num_orders: {espresso.num_orders()}")

# Average price per coffee
print(f"Latte average_price: {latte.average_price()}")
print(f"Cappuccino average_price: {cappuccino.average_price()}")

# Coffee's customers
print(f"Latte customers: {[customer.name for customer in latte.customers()]}")
print(f"Espresso customers: {[customer.name for customer in espresso.customers()]}")

# Bonus: Who spent the most on Latte?
most_spent = Customer.most_aficionado(latte)
print(f"Most aficionado for Latte: {most_spent.name if most_spent else 'None'}")