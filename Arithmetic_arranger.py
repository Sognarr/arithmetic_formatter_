import re

def arithmetic_arranger(problems, show_answers=False):
  
    if len(problems)> 5:
      return "Error: Too many problems."

    first =""
    second =""
    lines =""
    sumx =""
    string =""

    for problem in problems:
      if(re.search("[^\s0-9.+-]", problem)):
        if(re.search("[/]", problem) or re.search("[*]", problem)):
          return "Error: Operator must be '+' or '-'."
        return "Error: Numbers must only contain digits."
      

      firstNumber, operator, secondNumber = problem.split()
      if(len(firstNumber) > 4 or len(secondNumber) > 4):
        return "Error: Numbers cannot be more than four digits."

      sum_result = ""
      if operator == '+':
        sum_result = str(int(firstNumber) + int(secondNumber))
      elif (operator == '-'):
        sum_result = str(int(firstNumber) - int(secondNumber))

      length = max(len(firstNumber), len(secondNumber)) +2
      top = str(firstNumber).rjust(length)
      bottom = operator + str(secondNumber).rjust(length - 1 )
      line ="-" * length
      res= str(sum_result).rjust(length)
      

      first += top + '    '
      second += bottom + '    '
      lines += line + '    '
      sumx += res + '    '

    if show_answers:
      arranged_problems = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
      arranged_problems = first + "\n" + second + "\n" + lines
    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')