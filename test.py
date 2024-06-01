# Create a file with PII data
user_data = [{
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "555-123-4567",
        "ssn": "123-45-6789",
        "credit_card": "4111 1111 1111 1111",
        "ip_address": "192.168.1.1"
    }, {
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "phone": "555-987-6543",
        "ssn": "987-65-4321",
        "credit_card": "5500 0000 0000 0004",
        "ip_address": "10.0.0.2"
    }]

# Write the PII data to a file
with open('pii_data.txt', 'w') as file:
    file.write(pii_data)

print("PII data file 'pii_data.txt' created successfully.")
