score = input("Enter Score: ")

try:
    score_int=float(score)
except:
    print("Error,enter numeric input!")
    quit()
	
    
if 0.0<=score_int<=1.0:
    if score_int>=0.9:
        print("A")
    elif score_int>=0.8:
        print("B")
    elif score_int>=0.7:
        print("C")
    elif score_int>=0.6:
        print("D")
    elif score_int<0.6:
        print("F")
else:
    print("Prompt for a score between 0.0 and 1.0!")
    