# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter package weight in kilograms: "))
rate = float(input("Enter the shipping rate in kilograms: "))

## Calculate shipping cost
shipping_cost = weight * rate

##Disply results
print(f"Shipping Cost: {shipping_cost} USD") 
