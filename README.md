# ☕ Coffee Shop Challenge

This is a Python object-oriented programming (OOP) project modeling a coffee shop system with three main classes: Customer, Coffee, and Order. It covers object relationships, properties, type validation, aggregation, and more.

## 📁 Project Structure


## 📌 Requirements

### 1. Models

#### Customer
- Initializes with a name (str, 1–15 characters).
- Property name with type and length validation.
- Methods:
  - orders() → list of their Order instances.
  - coffees() → unique Coffee instances ordered.
  - create_order(coffee, price) → creates an Order.
  - most_aficionado(coffee) (classmethod) → customer who spent the most on a given coffee.

#### Coffee
- Initializes with a name (str, ≥3 characters).
- Property name (immutable).
- Methods:
  - orders() → list of `Order`s for this coffee.
  - customers() → unique list of customers who ordered it.
  - num_orders() → count of orders.
  - average_price() → mean price of orders.

#### Order
- Initializes with:
  - customer (Customer instance)
  - coffee (Coffee instance)
  - price (float, between 1.0 and 10.0)
- Properties:
  - customer and coffee are type-checked.
  - price is immutable with type/range enforcement.

---

## 🔧 How to Use

1. Clone or download the project.

2. Ensure you're using Python 3.6+.

3. Run the debug/test file:

```bash
python debug.py