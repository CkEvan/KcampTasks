import os

# User roles
# Created users and assigning roles to each user
users = {
    'Andrew': 'System Administrator',
    'Julius': 'Legal',
    'Chizi': 'Human Resource Manager',
    'Jeniffer': 'Sales Manager',
    'Adeola': 'Business Strategist',
    'Bach': 'CEO',
    'Gozie': 'IT intern',
    'Ogochukwu': 'Finance Manager'
}

# Assign users to groups
groups = {
    'System Administrator': 'Employees',
    'Legal': 'Employees',
    'Human Resource Manager': 'Employees',
    'Sales Manager': 'Employees',
    'Business Strategist': 'Employees',
    'CEO': 'Employees',
    'IT intern': 'Employees',
    'Finance Manager': 'Employees'
}

# Print user assignments
for user, role in users.items():
    print(f"{user} is assigned to the {groups[role]} group.")



# List of company directories
company_directories = [
    'Finance Budgets',
    'Contract Documents',
    'Business Projections',
    'Business Models',
    'Employee Data',
    'Company Vision and Mission Statement',
    'Server Configuration Script'
]

# Get user input for file creation
file_name = input("Enter the name of the file: ")
directory_name = input("Enter the directory to create the file: ")

# Check if the directory exists in the company directories
if directory_name in company_directories:
    # Create the directory if it doesn't exist
    os.makedirs(directory_name, exist_ok=True)
    print(f"Directory '{directory_name}' created successfully.")
    
    # Create the file
    file_path = os.path.join(directory_name, file_name)
    with open(file_path, 'w') as file:
        print(f"File '{file_name}' created in '{directory_name}'.")
else:
    print(f"Directory '{directory_name}' is not one of the company directories.")
