def employee_print(employee_info):
    
    if("Name" in employee_info):
        print(f"Name: {employee_info.get('Name')}")
        employee_info.pop("Name")
    else:
        print("Name: N/A")

    if("Salary" in employee_info):
        print(f"Salary: {employee_info.get('Salary')}")
        employee_info.pop("Salary")
    else:
        print("Salary: N/A")

    if("Role" in employee_info):
        print(f"Role: {employee_info.get('Role')}")
        employee_info.pop("Role")
    else:
        print("Role: N/A")

    llaves_restantes = employee_info.keys()

    if(len(llaves_restantes) == 0):
        print("No other info!")    
    else:
        for llave in llaves_restantes:
            print(f"{llave}: {employee_info[llave]}")
 

employee_info = {
    "Name": "Diego",
    "Salary": 5000000,
    "Role": "Janitor",
    "Years at company": 9001,
    "Hours per week": 2
}

employee_print(employee_info) 