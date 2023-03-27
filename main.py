from calculate_palm import validate_weight
from calculate_palm import calculate_price
def main():
#ฟังก์ชั่นหลักที่แจ้งให้ผู้ใช้ป้อนน้ำหนักของน้ำมันปาล์มกับรถและน้ำหนักของรถเปล่าคำนวณน้ำหนักรวมและราคาตามอินพุตและราคาต่อกก. แล้วพิมพ์ผลลัพธ์
   
    weight_with_palm_oil = float(input("Enter the weight of the palm oil with the vehicle in kg: "))
    weight_empty = float(input("Enter the weight of the empty vehicle in kg: "))
    price_per_kg = float(input("Enter the price per kg of the palm oil: "))
    
    if validate_weight(weight_with_palm_oil, weight_empty):
        price = calculate_price(weight_with_palm_oil, weight_empty, price_per_kg)
        print(f"The total weight of the palm oil is {weight_with_palm_oil - weight_empty} kg and the price is {price} baht.")
    else:
        print("Weight limit exceeded. Maximum weight allowed is 3000 kg.")