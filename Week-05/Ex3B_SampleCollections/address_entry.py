
# Create a contact information dictionary
contact_info = {
    "name": "Anna Smith",
    "address": "123 Main Street",
    "city": "Boston",
    "state": "MA",
    "zip": "02108"
}

# Display the original mailing address
print(f"{contact_info['name']}\n{contact_info['address']}\n{contact_info['city']}, {contact_info['state']} {contact_info['zip']}")

# Remove the name key
contact_info.pop("name")

# Create a full_name dictionary
full_name = {
    "first name": "Anna",
    "last name": "Smith"
}

# Add an honorific
full_name.update({"honorific": "Ms."})

# Add full_name information to contact_info
contact_info.update(full_name)

# Display the updated mailing address
print(
    f"{contact_info['honorific']} {contact_info['first name']} {contact_info['last name']}\n"
    f"{contact_info['address']}\n"
    f"{contact_info['city']}, {contact_info['state']} {contact_info['zip']}"
)
