import re

def arithmetic_arranger(problems, show_answers=False):
  
    if len(problems)> 5:
      return "Error: Too many problems."

    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = ""

    for problem in problems:
      if(re.search("[^\s0-9.+-]", problem)):
        if(re.search("[/]", problem) or re.search("[*]", problem)):
          return "Error: Operator must be '+' or '-'."
        return "Error: Numbers must only contain digits."
      

      firstNumber = problem.split(" ")[0]
      operator = problem.split(" ")[1]
      secondNumber = problem.split(" ")[2]

      if(len(firstNumber) >= 5 or len(secondNumber) >= 5):
        return "Error: Numbers cannot be more than four digits."

      sum = ""
      if (operator == '+'):
        sum = str(int(firstNumber) + int(secondNumber))
      elif (operator == '-'):
        sum = str(int(firstNumber) - int(secondNumber))

      length = max(len(firstNumber), len(secondNumber))
      top = str(firstNumber).rjust(length  + 2)
      bottom = operator + str(secondNumber).rjust(length +1)
      line =""
      res= str(sum).rjust(length +2)
      for s in range(length + 2):
        line += "-"

      first += top + '    '
      second += bottom + '    '
      lines += line + '    '
      sumx += res + '    '

    if show_answers:
      string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
      string = first + "\n" + second + "\n" + lines
    return string

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')