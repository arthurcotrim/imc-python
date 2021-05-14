def exponentiation(number):
  exponentiation = number ** 2
  return exponentiation

def imc(weight, height):
  double_height = exponentiation(height)

  imc = weight / double_height

  return imc

def classification(imc):
  if imc < 18.5:
     print('Thinness', imc)
  elif imc >=18.5 and imc <25:
    print('Normal', imc)
  elif imc >=25 and imc <30:
    print('Overweight', imc)
  elif imc >=30 and imc <40:
    print('Obesity', imc)
  else:
    print('Severe obesity', imc)

weight = float(input('Inform yout weight: '))
height = float(input('Inform your height: '))

my_imc = imc(weight, height)

classification(my_imc)
