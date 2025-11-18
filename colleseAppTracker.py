def display_welcome():
    pass

def get_college_count():
    '''
    Number of colleges the user is applying to 
    
    return
        count (int)
    '''

    count = int(input("How many colleges have you applied for: "))
    return count

def get_application_cost(num_colleges):
    '''
    Calculate total apliction cost

    return
        total_cost (float)
    '''
    total_cost = float(num_colleges * 50)
    return total_cost

def get_sat_score():
    '''
    Get users SAT score

    return
        score (int)
    '''

    score = int(input("What is your SAT score? "))
    return score

def analyze_sat(score):
    '''
    provide feedback on SAT
    >= 1400 - excellent
    >= 1200 - good score
    >= 1000 - soild foundation
    else - consider retaking to inprove college options
    '''

    if score >= 1400:
        feedback = "Excellent"
    elif score >= 1200:
        feedback = "Good score"
    elif score >= 1000:
        feedback = "Soild foundation"
    else:
        feedback = "Consider retaking to improve college options"
    return feedback

def display_summary(colleges, cost, sat_score, sat_feedback):
    print("Number of colleges:", colleges)
    print("Total cost:", cost)
    print("SAT score:", sat_score)
    print("SAT feedback:", sat_feedback)

def main():
    # Welcome the user
    display_welcome()

    #Collect information 
    num_colleges = get_college_count()
    total_cost = get_application_cost(num_colleges)
    sat = get_sat_score()

    # Analyze data
    feedback = analyze_sat(sat)

    # Display results
    display_summary(num_colleges, total_cost, sat, feedback)

# Entry point
if __name__ == "__main__":
    main()