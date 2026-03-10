spo2 = int(input("Enter SpO2 value (%): "))

if spo2 >= 95:
    print("Oxygen level is Normal")
elif spo2 >= 90:
    print("Oxygen level is Low. Monitor closely.")
else:
    print("Critical oxygen level. Seek medical help.")