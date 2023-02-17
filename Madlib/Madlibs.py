# String concatenation (how to put a strings together)

ans = "Yes it is working"

#1. Way
print("Is it working ? -",ans)

#2. Way 
print("Is it working ? - " + ans)

#3. Way
print(f"Is it working ? - {ans}")

#4. Way
print("Is it working ? - {}".format(ans))

#5. Way
print("Is it working ? - %s"%(ans))

#>>>
# Is it working ? - Yes it is working
# Is it working ? - Yes it is working
# Is it working ? - Yes it is working
# Is it working ? - Yes it is working
# Is it working ? - Yes it is working


from sample_madlib import code_1, code_2, code_3, code_4
import random


if __name__ == "__main__":
    select_code = random.choice([code_1, code_2, code_3, code_4])
    select_code.madlib()
