from numb3rs import validate

def test_valid_ips():
    assert validate("192.168.1.1") == True, "Failed on valid IP '192.168.1.1'"
    assert validate("0.0.0.0") == True, "Failed on valid IP '0.0.0.0'"
    assert validate("255.255.255.255") == True, "Failed on valid IP '255.255.255.255'"
    assert validate("127.0.0.1") == True, "Failed on valid IP '127.0.0.1'"

def test_invalid_ips():
    assert validate("256.256.256.256") == False, "Failed on invalid IP '256.256.256.256'"
    assert validate("192.168.1") == False, "Failed on invalid IP '192.168.1'"
    assert validate("192.168.1.999") == False, "Failed on invalid IP '192.168.1.999'"
    assert validate("192.168.1.-1") == False, "Failed on invalid IP '192.168.1.-1'"
    assert validate("192.168.1.1.1") == False, "Failed on invalid IP '192.168.1.1.1'"
    assert validate("abc.def.ghi.jkl") == False, "Failed on invalid IP 'abc.def.ghi.jkl'"
    assert validate("1234.123.123.123") == False, "Failed on invalid IP '1234.123.123.123'"

def test_edge_cases():
    assert validate("192.168.01.1") == True, "Failed on edge case '192.168.01.1'"
    assert validate("192.168.1.01") == True, "Failed on edge case '192.168.1.01'"
    assert validate("0.0.0.0") == True, "Failed on edge case '0.0.0.0'"
    assert validate("255.255.255.255") == True, "Failed on edge case '255.255.255.255'"

if __name__ == "__main__":
    test_valid_ips()
    test_invalid_ips()
    test_edge_cases()
    print("All tests passed!")
