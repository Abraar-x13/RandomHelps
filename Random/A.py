"""
    Hey Raisa, you were on the right track to solve the problem. I completed half of the work for you.
    Changed the code to show all of the errors, and showed the first one. Output the rest.
    If you can't, here's a repo to follow : https://github.com/ShreyasSubhedar/fcc-arithmetic-arranger
    
"""

def arithmetic_arranger(problems, show = False) -> None:
    
    num1, num2, oprt = [], [], []
    line1 = line2 = line3 = line4 = ""
    
    if len(problems) > 5: return "Error: Too many problems"
    
    for i in problems:
        
        if "+" in i:
            oprt.append("+")
            operand1, operand2 = i.split("+")
            if len(operand1) > 4 or len(operand2) > 4:
                return "Error: Numbers cannot be more than four digits."
            try:
                num1.append(int(operand1))
                num2.append(int(operand2))
            except ValueError:
                return "Error: Numbers must only contain digits."
            
        elif "-" in i:
            oprt.append("-")
            operand1, operand2 = i.split("-")
            if len(operand1) > 4 or len(operand2) > 4:
                return "Error: Numbers cannot be more than four digits."
            try:
                num1.append(int(operand1))
                num2.append(int(operand2))
            except:
                return "Error: Numbers must only contain digits."
        else:
            return "invalid operator"
        
    if show is True:
        line1 += str(num1[0]).rjust(6)
        line2 += oprt[0] + ' ' + str(num2[0]).rjust(4)
        line3 += '-' * (6)
        if oprt[0] == "+":
            # print(f"{num1[0]} + {num2[0]} = {num1[0] + num2[0]}")
            line4 += "    " + str(num1[0] + num2[0]).rjust(2)
        else:
            # print(f"{num1[0]} - {num2[0]} = {num1[0] - num2[0]}")
            line4 += "    " + str(num1[0] - num2[0]).rjust(2)
              
        print(line1)
        print(line2)
        print(line3)
        print(line4)                


if __name__ == "__main__":
    
    problems_lst=["25+4","345-25","250+53","77-7","13+4"]
    arithmetic_arranger(problems_lst, True)

