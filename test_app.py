def test_basic():
    assert 1 + 1 == 2

def test_prediction():
    from app import predict
    result = predict("This is a test")
    assert len(result) > 0
