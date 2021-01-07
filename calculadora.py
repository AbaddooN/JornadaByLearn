while True:
 operacao = input('Escolha uma das operacoes (+,-,*,/) que deseja fazer ou \'q\' para sair: ')
 if operacao == 'q' or operacao == 'Q':
  break
 elif operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':
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
