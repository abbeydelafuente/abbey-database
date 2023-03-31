# 1 Savings
def savings(gross_pay, tax_rate, expenses):
    after_tax = int(gross_pay * (1 - tax_rate))
    remaining_pay = after_tax_pay - expenses
    return remaining_pay
# test
# gross_pay = [input value here]
# tax_rate = [input value here]
# expenses = [input value here] 
# remaining_pay = savings(gross_pay, tax_rate, expenses)
# print("Remaining pay: ", remaining_pay)

# 2 Material Waste
def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_consumption = num_jobs * job_consumption
    remaining_material = total_material - total_consumption
    formatted_remaining_material = str(remaining_material) + material_units
    return formatted_remaining_material
# test  
# remaining_material = material_waste([input value here], [input units here], [input value here], [input value here])
# print("Remaining material: ", remaining_material)

# 3 Interest
def interest(principal, rate, periods):
    interest_earned = principal * rate * periods
    final_amount = principal + interest_earned
    return int(final_amount)
# test
# result = interest([input value here], [input value here], [input value here])
# print(result) 

# 4 Body Mass Index
def body_mass_index(weight, height):
    weight_kg = weight * 0.45359237
    height_m = (height[0] * 0.3048) + (height[1] * 0.0254)
    bmi = weight_kg / (height_m ** 2)
    return bmi
# test
weight = [input value here]
height = [[input value here], [input value here]]
print(body_mass_index(weight, height))
