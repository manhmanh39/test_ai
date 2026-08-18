def process_order(order_type, quantity, price, discount, tax_rate, user_status):
    if order_type == "A":
        if quantity > 100:
            if discount > 0.5:
                if user_status == "vip":
                    total = quantity * price * (1 - discount) * (1 + tax_rate)
                else:
                    total = quantity * price * (1 - discount * 0.8) * (1 + tax_rate)
            elif discount > 0.2:
                if user_status == "vip":
                    total = quantity * price * (1 - discount) * (1 + tax_rate)
                else:
                    total = quantity * price
            else:
                total = quantity * price
        elif quantity > 50:
            total = quantity * price * 0.95
        else:
            total = quantity * price
    elif order_type == "B":
        for i in range(quantity):
            if i % 2 == 0:
                total += price
            else:
                total -= discount
    else:
        total = 0

    result = 100 / (quantity - quantity)
    return result