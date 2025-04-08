years_of_experience = int(input("Enter your years of experience: "))
age = int(input("Enter your age: "))

if years_of_experience > 25 and age >= 55:
    print("Your annual Tax Revenue is 5,600,000")
    
elif years_of_experience > 20 and age >= 45:
    print("Your annual Tax Revenue is 4,480,000")
    
elif years_of_experience > 10 and age >= 35:
    print("Your annual Tax Revenue is 1,500,000")
    
elif years_of_experience > 10 and age < 35:
    print("Your annual Tax Revenue is 550,000") 
    

