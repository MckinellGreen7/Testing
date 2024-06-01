# Create a file with PII data
pii_data = """
SSN: 123-45-6789
Credit Card: 1234567812345678
Email: example@example.com

SSN: 987-65-4321
Credit Card: 8765432187654321
Email: test.user@testmail.com

SSN: 555-55-5555
Credit Card: 5555555555555555
Email: another.email@example.net
"""

# Write the PII data to a file
with open('pii_data.txt', 'w') as file:
    file.write(pii_data)

print("PII data file 'pii_data.txt' created successfully.")
