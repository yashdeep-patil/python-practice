class AgeError(Exception):
    
    pass

def check_voting_eligibility(age):
    
    if age < 0:
        raise AgeError("Age cannot be negative.")
    
    elif age < 18:
        raise AgeError("Not eligible to vote.")
    else:
        return "Eligible to vote."   
try:
    print(check_voting_eligibility(20))
    print(check_voting_eligibility(15))  
    print(check_voting_eligibility(-5))   

except AgeError as e:
    print(e)

finally:
    print("Voting eligibility check completed.")