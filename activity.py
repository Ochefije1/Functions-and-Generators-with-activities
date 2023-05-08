def calculate_tax(name, department, position, **salary):
    # Find the salary value
        salary_value = float(salary['salary'])
    
    # Calculate the tax
    tax_rate = 0.2  # 20% tax rate
    tax_amount = salary_value * tax_rate
    
    # Return a string describing the tax amount
    return f"{name} in {department} as {position} will pay {tax_amount:} in tax."

