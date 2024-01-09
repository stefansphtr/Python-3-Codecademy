"""Reading in the Passwords"""

# Task 1
# Import module
import csv
import json

# Task 2
compromised_users = []

# Task 3
with open("passwords.csv") as password_file:
    # Task 4
    password_csv = csv.DictReader(password_file)
    # Task 5
    for password_row in password_csv:
        # Task 6
        # print(password_row["Username"])
        # Task 7
        compromised_users.append(password_row["Username"])

# print(compromised_users)

# Task 8
with open("compromised_user.txt", "w") as compromised_user_file:
    # Task 9
    for compromised_user in compromised_users:
        # Task 10 - 11
        compromised_user_file.write(compromised_user)

"""Notifying the Boss"""

# Task 12 -13
with open("boss_message.json", "w") as boss_message:
    # Task 14
    boss_message_dict = {"recipent": "The Boss", "message": "Mission Success"}
    # Tas 15
    json.dump(boss_message_dict, boss_message)

"""Scrambling the Password"""

# Task 16
with open("new_passord.csv", "w") as new_passwords_obj:
    # Task 17
    slash_null_sig = """  _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/ """
    # Task 18 - 19
    new_passwords_obj.write(slash_null_sig)
