print("===== Placement Eligibility Validator =====")

name = input("Enter candidate name: ")
graduation_score = float(input("Enter graduation score (%): "))
active_backlogs = int(input("Enter number of active academic backlogs: "))

print("\n===== Eligibility Result =====")
print("Candidate:", name)

if graduation_score >= 70 and active_backlogs == 0:
    print("Status: ELIGIBLE")
    print("Reason: Candidate has 70% or above and no active academic backlogs.")
else:
    print("Status: NOT ELIGIBLE")

    if graduation_score < 70:
        print("Reason: Graduation score is below 70%.")

    if active_backlogs > 0:
        print("Reason: Candidate has active academic backlogs.")
