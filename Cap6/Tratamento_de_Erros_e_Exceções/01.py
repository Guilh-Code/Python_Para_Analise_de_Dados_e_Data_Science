# Tratamento de exceções permite que seu programa lide com erros de forma controlada, sem travar. Em vez de encerrar a execução, você pode capturar e reagir a erros específicos.

# Erro (leia a mensagem de erro)
#print('Hello)

# Erro (leia a mensagem de erro)
#s + 's'

# Criando uma função
# def numDiv(num1, num2):
#    resultado = num1 / num2
#    print(resultado)

# Execução não gera erro
#numDiv(4, 2)

# Execução gerando erro (leia a mensagem de erro)
#numDiv(4, 0)


# ---------------------------------------------

# Utilizando try e except
try:
    s + 's'
except NameError:
    print('Operação não permitida')


# Utilizando try, except e else
try:
    f = open('arquivos/testandoerros.txt', 'w')
    f.write('Gravando no arquivo')
except IOError:
    print('Erro: arquivo não encontrado ou não pode ser salvo.')
else:
    print('Conteúdo gravado com sucesso!')
    f.close()


# Utilizando try, except e else
try:
    f = open('arquivos/testandoerros', 'r')
except IOError:
    print('Erro: arquivo não encontrado ou não pode ser lido.')
else:
    print('Conteúdo gravado com sucesso!')
    f.close()


# Utilizando try, except, else e finally
try:
    f = open('arquivos/testandoerros.txt', 'w')
    f.write('Gravando no arquivo')
except IOError:
    print('Erro: arquivo não encontrado ou não pode ser salvo.')
else:
    print('Conteúdo gravado com sucesso!')
    f.close()
finally:
    print('Comandos no bloco finally são sempre executados!')
