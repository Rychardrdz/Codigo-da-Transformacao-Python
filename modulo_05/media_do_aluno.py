'''
Atividade 2
'''

def calcular_media(notas):
    media = sum(notas) / len(notas)
    
    print(f"Média: {media:.1f}")
    
    if media >= 7:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado.")

# Exemplo de uso
calcular_media([7.5, 8.0, 6.5])