# hands = ["""
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# ""","""
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# ""","""
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """]

# candidate_hand = input('chose - hammer,paper,seaser')
# print('your hand')
# if candidate_hand == 'hammer':
#     print("""
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """)
# elif candidate_hand == 'paper':
#     print("""
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """)
# else :
#     print("""
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """)
# import random
# a= random.randint(0,2)
# print('by computer')
# print(hands[a])


# =========================================




# hands = {'hammer' : """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """,'paper' : """
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """,'seaser' : """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """}

# candidate_hand = input('chose - hammer,paper,seaser')
# print('your hand')
# print(hands[candidate_hand])
# import random
# b=['hammer','paper','seaser']
# a= random.choice(b)
# print('by computer')
# print(hands[a])






# # =====================================================







hands = {'hammer' : """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",'paper' : """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",'seaser' : """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""}

candidate_hand = input('chose - hammer,paper,seaser')
print('your hand')
print(hands[candidate_hand])
import random
b=['hammer','paper','seaser']
a= random.choice(b)
print('by computer')
print(hands[a])
if candidate_hand == a:
    print('your match is drra')
elif candidate_hand == 'hammer' & a == 'paper':
    print('you lose')
elif candidate_hand == 'paper' & a == 'seaser':
    print('you lose')
elif candidate_hand== 'seaser' & a == 'hammer':
    print('you lose')
else :
    print('you win')