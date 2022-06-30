is_buyer_good = True
price = 1000000

if is_buyer_good:
    down = 0.1 * price
else:
    down = 0.2 * price
print(f"Down payment: P{down}")