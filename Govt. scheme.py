scheme_eligibilty=int(input("Enter Your Age "))
if scheme_eligibilty<20:
    print("You're not eligible for the scheme")
elif scheme_eligibilty<30:
    print("You're eligible for INR 10000")
elif scheme_eligibilty<45:
    print("You're elegible for upto INR 15000")
elif scheme_eligibilty<=70:
    print("You're Eligible for upto INR 5000")