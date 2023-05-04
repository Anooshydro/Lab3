
def calculate_bmi (height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = (weight/(height*height))
    print("BMI = " + str(bmi))
    if bmi < 18.5:
        print("Under Weight")
    elif bmi > 25.0:
        print("Over Weight")
    elif 18.5 <= bmi <= 25.0:
        print("Normal Weight")
    else:
        print("Error")




calculate_bmi(weight=65, height=1.75)