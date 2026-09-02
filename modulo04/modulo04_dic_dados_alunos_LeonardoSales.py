import time
aluno = {
    "nome": "João da Silva",
    "idade": 17,
    "notas": [8.5, 7.0, 9.5] 
}
print('\n','=' * 48,'\n')
print("====Ficha do Aluno====\n")
time.sleep(3)
print(f"\nNome: {aluno['nome']}")
time.sleep(1)
print(f"\nIdade: {aluno['idade']} anos")
time.sleep(1)
media_das_notas = sum(aluno['notas']) / len(aluno['notas'])
print(f"\nMédia das notas: {media_das_notas:.2f}")
time.sleep(1)
print(f"\nNotas: {aluno['notas']}")
time.sleep(1)
print('\n','=' * 48,'\n')
print("====Todos os Dados====\n")
time.sleep(3)
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")
    time.sleep(1)
print('\n','=' * 48,'\n')
