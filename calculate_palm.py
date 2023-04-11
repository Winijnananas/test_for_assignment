def calculate_price(weight_with_palm_oil, weight_empty, price_per_kg):
    # คำนวณราคาน้ำมันปาล์มตามน้ำหนัก น้ำหนักรถ และราคาต่อกก.
    total_weight = weight_with_palm_oil - weight_empty
    if not validate_weight(weight_with_palm_oil, weight_empty):
        return "น้ำหนักเกินกำหนด น้ำหนักสูงสุดที่อนุญาตคือ 3000 กก."
    else:
        total_price = total_weight * price_per_kg
        if total_price < 0:
            return "ราคาติดลบ"
        elif total_price == 0:
            return "ไม่มีมูลค่า"
        else:
            return f"{int(total_price)} baht"


def validate_weight(weight_with_palm_oil, weight_empty):
    # ตรวจสอบน้ำหนักของน้ำมันปาล์มกับรถเพื่อให้แน่ใจว่าไม่เกินน้ำหนักที่กำหนด
    total_weight = weight_with_palm_oil - weight_empty
    if total_weight > 3000:
        return False
    elif total_weight <= 0:
        return "น้ำหนักรวมน้อยกว่า0"
    else:
        return True
    # if total_weight > 3000:
    #     return False
    # elif total_weight <=0:
    #     return "น้ำหนักติดลบ"
    # else:
    #     return "น้ำหนักติดลบ"
def display_price(weight_with_palm_oil, weight_empty, price_per_kg):
    # คำนวณราคาน้ำมันปาล์มตามน้ำหนัก น้ำหนักรถ และราคาต่อกก.
    total_weight = weight_with_palm_oil - weight_empty
    if not validate_weight(weight_with_palm_oil, weight_empty):
        return False
    else:
        total_price = calculate_price(weight_with_palm_oil, weight_empty, price_per_kg)
        return f"น้ำหนักรวมของน้ำมันปาล์มคือ {total_weight} กก.และมีราคา {total_price} บาท."

# def calculate_palm(weight_with_palm_oil, weight_empty, price_per_kg):
#     # คำนวณราคาน้ำมันปาล์มตามน้ำหนัก น้ำหนักรถ และราคาต่อกก.
#     if weight_with_palm_oil < 0 or weight_empty < 0:
#         return "Weight cannot be negative."
#     elif not validate_weight(weight_with_palm_oil, weight_empty):
#         return "Weight limit exceeded. Maximum weight allowed is 3000 kg."
#     else:
#         total_weight = weight_with_palm_oil - weight_empty
#         total_price = total_weight * price_per_kg
#         return f"The total weight of the palm oil is {total_weight} kg and the price is {total_price} baht."

# def validate_weight(weight_with_palm_oil, weight_empty):
#     # ตรวจสอบน้ำหนักของน้ำมันปาล์มกับรถเพื่อให้แน่ใจว่าไม่เกินน้ำหนักที่กำหนด
#     total_weight = weight_with_palm_oil - weight_empty
#     if total_weight > 3000:
#         return False
#     else:
#         return True