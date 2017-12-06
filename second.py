score = raw_input("Enter Score Grade:")

if score > 90:
    print "Grade A"
elif score >= 80:
    print "grade B"
elif score >= 70:
    print "grade C"
elif score >= 60:
    print "grade D"
else:
    print "Your grade is an F"
    
    
    '''
    Accept a numeric score (0-100) as input. Convert this input into a letter grade.
    
    A = 100-90
    B = 89-80
    C = 79-70
    D = 69-60
    F = anything else 
    
    '''
