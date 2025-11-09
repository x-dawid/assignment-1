from ex2 import email_addresses
first = ["Jack" , "Bellatrix"]
last = ["Sparrow" , "Lestrange"]
expected_result = ["j.sparrow@exeter.ac.uk" , "b.lestrange@exeter.ac.uk"]
assert email_addresses(first, last) == expected_result
print("Test Passed!")
