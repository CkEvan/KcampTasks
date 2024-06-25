import os
import subprocess

base_directory = "/vagrant"
company_directory = "Kodecamp-Stores"


employees = {
    "Andrew": "System-Administrator",
    "Julius": "Legal",
    "Chizi": "HR",
    "Jeniffer": "Sales-Manager",
    "Adeola": "Business-Strategist",
    "Bach": "CEO",
    "Gozie": "IT-Intern",
    "Ogochukwu": "Finance-Manager"
}

command = ["sudo", "useradd", "-m", "-G"]  # legal Julius

# Creating Users and assigning them to a group
# fun // function


def create_employee(employee_name, group):
    try:
        subprocess.run(["sudo", "useradd", "-m", "-G", group, employee_name], )
        print(
            f"Created employee {employee_name} successfully and added to group {group}")

    except subprocess.CalledProcessError as e:
        print(f"Could not create employee {employee_name}: {e}")

# Create groups


def create_group(group_name):
    try:
        subprocess.run(['sudo', 'groupadd', group_name], check=True)
        print(f"Group '{group_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create group '{group_name}'. Error: {e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


# Company directories
company_directories = {
    "Finance-Budgets": "Finance-Manager",
    "Contract-Documents": "Legal",
    "Business-Projections": "Business-Strategist",
    "Business-Models": "Sales-Manager",
    "Employee-Data": "HR",
    "Company-Vision and Mission Statement": "CEO",
    "Server-Configuration Script": "System-Administrator"
}

# Check if directory exist


def check_dir():
    dirs = os.listdir("./")
    # print(f"dirs in check_dir(): {dirs}")
    # print(f"dir in dirs: {dir}")
    if company_directory in dirs:
        exist = "Directory exists"
    else:
        exist = "Directory does not exist"
    return exist


# Get current working directory
cwd = os.getcwd()


# Create directory
def create_directory(directory_name):
    if cwd == base_directory:
        directory_exist = check_dir()
        # print(f"directory exist value: {directory_exist}")
        if directory_exist == "Directory does not exist":
            try:
                os.mkdir(f"{company_directory}/")
                create_directories(directory_name)
                print(
                    f"Directory /{company_directory}/{directory_name} created")

            except OSError as e:
                print(f"Error creating directory: {e}")
        else:
            create_directories(directory_name)
    else:
        os.chdir(base_directory)
        os.mkdir(f"{company_directory}/")
        create_directories(directory_name)
        print(f"Directory /{company_directory}/{directory_name} created")


def create_directories(directory_name):
    try:
        os.makedirs(f"/{company_directory}/{directory_name}", exist_ok=True)
        print(f"Directory /{company_directory}/{directory_name} created")
    except OSError as e:
        print(
            f"Error creating directory /{company_directory}/{directory_name}: {e}")


# Set Permissions
def set_permissions(directory_name, employee_name, group):
    try:
        subprocess.run(["sudo", "chown", f"{employee_name}:{group}",
                       f"/{company_directory}/{directory_name}"], check=True)
        subprocess.run(
            ["sudo", "chmod", "770", f"/{company_directory}/{directory_name}"], check=True)
        print(f"Permissions set for /{company_directory}/{directory_name}")
    except subprocess.CalledProcessError as e:
        print(
            f"Error setting permissions for /{company_directory}/{directory_name}: {e}")


def create_file():
    filename = input("Enter the name of the file: ")
    directory_name = input("Enter the directory to create the file in: ")

    if directory_name in company_directories.keys():
        file_path = f"/{company_directory}/{directory_name}/{filename}"
        try:
            with open(file_path, "w") as file:
                file.write("This is a new file.\n")
            print(
                f"File {filename} created in /{company_directory}/{directory_name}")
        except IOError as e:
            print(f"Error creating file {filename}: {e}")
    else:
        print(
            f"Directory /{company_directory}/{directory_name} does not exist. File not created.")


def main():
    # Create users/Employees and directories
    for employee_name, group in employees.items():
        create_group(group)
        create_employee(employee_name, group)

    for directory_name, group in company_directories.items():
        create_directory(directory_name)

        employee = [employee_name for employee_name,
                    emp_group in employees.items() if emp_group == group]
        if employee:
            set_permissions(directory_name, employee[0], group)

    create_file()


main()
