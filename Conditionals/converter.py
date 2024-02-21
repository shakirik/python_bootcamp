kms = input("How many did km did you cycle today? ")
kms = float(kms)
miles = kms / 1.65775
miles = round(miles, 2)
print(f"You cycled {kms} km which is equivalent to {miles} miles")