
print("----- BLOOD DONOR SCREENING SYSTEM ------")
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight: "))

if donor_age >= 18 and donor_weight >= 50 :
    print("Result: ELigible please proced to the blood doantion room ")
else:
    print("Result: Not eligible. Thank you for your interest ")