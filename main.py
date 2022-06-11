while True:
  try:
    part1 = int(input('correct scores in part1 out of 10?\n'))
    part2 = int(input('correct scores in part2 out of 10?\n'))
    part3 = int(input('correct scores in part3 out of 10?\n'))
    part4 = int(input('correct scores in part4 out of 10?\n'))
    break
  except ValueError as err:
    print(err)
    continue
total = part1 + part2 + part3 + part4
incorrect = 40 - total
percentage1 = part1 / 10 *100
percentage2 = part2 / 10 *100
percentage3 = part3 / 10 *100
percentage4 = part4 / 10 *100
print(f'{round(percentage1)}%in part1\n{round(percentage2)}%in part2\n{round(percentage3)}%in part3\n{round(percentage4)}%in part4\n')
print(f'total incorrect answers are {incorrect},correct answers are {total}')
#----------------------part1
while True:
  try:
    score = int(input('your total score\n'))
    break
  except ValueError as err:
    print(err)
if score ==0 or score <=5:
  print('Band 2.5 out of 9')
elif score ==6 or score <=8:
  print('Band 3.0 out of 9')
elif score ==9 or score <=10:
  print('Band 3.5 out of 9')
elif score ==11 or score <=12:
  print('Band 4 out of 9')
elif score ==13 or score <=15:
  print('Band 4.5 out of 9')
elif score ==16 or score <=17:
  print('Band 5 out of 9')
elif score ==18 or score <=22:
  print('Band 5.5 out of 9')
elif score ==23 or score <=25:
  print('Band 6 out of 9')
elif score ==26 or score <=29:
  print('Band 6.5 out of 9')
elif score ==30 or score <=31:
  print('Band 7 out of 9')
elif score ==32 or score <=34:
  print('Band 7.5 out of 9')
elif score ==35 or score <=36:
  print('Band 8 out of 9')
elif score ==37 or score <=38:
  print('Band 8.5 out of 9')
elif score ==39 or score <=40:
  print('Band 9 out of 9')
else:
  print('sorry')
#-------------part2
while True:
  try:
    choose = int(input('Total Choose The Best Answers? - Question - 1\n'))
    chsans = int(input('Correct Answers? - Question - 2\n'))
    fill = int(input('Total Fill In The Best Answers? - Question - 3\n'))
    fillans = int(input('Correct Answers? - Question - 4\n'))
    break
  except ValueError as err:
    print(f'you should not type any letter(s)-{err}')
    continue
if chsans < fillans:
  print(f'Total Incorrect Answer(s) {choose - chsans}-in choose the best answer section')
  print('focus on the choose the best answers')
elif chsans > fillans:
  print(f'Total Incorrect Answer(s){fill - fillans}-in fill in the blank section')
  print('focus on fill in the blank section')
else:
  print('Congrats - You have been achieved 40 out of 40')
#-----------part3----
