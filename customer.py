import sys

def customer_purchases(smartwatch, laptop, smartphone):
    return smartphone + laptop + smartwatch

if __name__ == "__main__":
    smartwatch = int(sys.argv[1])
    laptop = int(sys.argv[2])
    smartphone = int(sys.argv[3])

    print("Customer_purchases_bill:", customer_purchases(smartwatch, laptop, smartphone))
