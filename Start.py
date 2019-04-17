sat_critical_reading= int(input("What is your critical reading SAT score? : "))
sat_mathematics = int(input("What is your mathematics SAT score? : "))
sat_writing = int(input("What is your writing SAT score? : "))
class_rank = int(input("What was your high school rank? : "))
class_size = int(input("What was the number of students in your graduating class? : "))

if (sat_mathematics or sat_writing or sat_critical_reading or class_rank < 0 or class_size < 0) > 800:
    print("Reject")
else:
    print("Accept")