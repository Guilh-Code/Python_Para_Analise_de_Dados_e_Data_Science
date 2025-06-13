

# Dicionário de alunos e notas
dict_alunos = {'Bob': 68, 'Michael': 84, 'Zico': 57, 'Ana': 89}

# Criamos um novo dicionário imprimindo os pares de chave:valor
# dict_alunos_status = {k:v for (k, v) in dict_alunos.items()}
# print(dict_alunos_status)



# Criamos um novo com os status: nota maior que 70, aprovado, senão, reprovado
dict_alunos_status = {k: ('Aprovado' if v > 70 else 'Reprovado') for (k, v) in dict_alunos.items()}
print(dict_alunos_status)