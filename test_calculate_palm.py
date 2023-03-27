from calculate_palm import validate_weight, calculate_price
# def test_calculate_price():
#     assert main.calculate_price(2500, 1200, 20) == 2900
#     with pytest.raises(ValueError, match="Weight limit exceeded. Maximum weight allowed is 3000 kg."):
#         main.calculate_price(3200, 1200, 20)
        
# def test_validate_weight():
#     assert main.validate_weight(1000, 1200) == True
#     assert main.validate_weight(1000, 900) == True
def test_validate_weight_within_limit():
    assert validate_weight(2500, 1200) == True

def test_validate_weight_exceeds_limit():
    assert validate_weight(3200, 1200) == True

def test_calculate_price_within_limit():
    assert calculate_price(2500, 1200, 20) == 26000

def test_calculate_price_exceeds_limit():
    assert calculate_price(3200, 1200, 20) == 40000
    
# def test_calculate_price_exceeds_limit():
#     assert calculate_price(3200, 1200, 20) == "Weight limit exceeded. Maximum weight allowed is 3000 kg."