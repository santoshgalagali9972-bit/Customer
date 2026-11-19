from customer import customer_purchases

def test_total_bill():
    assert customer_purchases(1500, 30000, 10000) == 41500

def test_any_bill():
    assert customer_purchases(2000, 60000, 0) == 62000
    