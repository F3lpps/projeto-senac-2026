from aluno import Aluno

if __name__ == '__main__':
    
    aluno = Aluno("João", [2,2,2,2,2])
    resultado = aluno.verificar_situacao()
    assert resultado == 'Reprovado'

    aluno2 = Aluno("João", [9,9,9,9,9])
    resultado2 = aluno2.verificar_situacao()
    assert resultado2 == 'Aprovado'

    aluno3 = Aluno("João", [6,6,6,6,6])
    resultado3 = aluno3.verificar_situacao()
    assert resultado3 == 'Recuperação'