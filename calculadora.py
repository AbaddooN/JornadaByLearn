while True:
 operacao = input('Qual operacao (+,-,*,/) deseja fazer ?: ')
 if operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':
  num1 = int(input('Digite o primeiro numero: '))
  num2 = int(input('Digite o segundo numero: '))
 else:
   print('Operacao Invalida')
 if operacao == '+':
   total = num1 + num2
   print(total)
 elif operacao == '*':
   total = num1 * num2
   print(total)
 elif operacao == '/':
   total = num1 / num2
   print(total)
 elif operacao == '-':
   total = num1 - num2
   print:(total)
