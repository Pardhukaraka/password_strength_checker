#password strength checking tool

import re

def pass_strength_checker(password):
    #mentioning the rules to meet the password

    rules={
        "Password length(8+ characters)":len(password)>=8,
        "Uppercase latter ":bool(re.search(r'[A-Z]',password)),
        "Lowercase latter ":bool(re.search(r'[a-z]',password)),
        "Number           ":bool(re.search(r'[0-9]',password)),
        "Special charecter":bool(re.search(r'[!@#$%^&*(),.|?":<>_]',password))
    }
    # checking password strength score

    strength_score=sum(rules.values())
    total_score=len(rules)

    if strength_score==total_score:
        strength="strong"
    elif strength_score<=total_score-1:
        strength="modarate"
    else:
        strength="weak"

    print("checking the password strength")

    #converting dictionary into tuples
    for criterion,met in rules.items():
        print(f'{criterion}:{'✔️' if met else '❌'}')

    print(f'strength of password : {strength}')

#use input

password=input("enter your password : ")
pass_strength_checker(password)