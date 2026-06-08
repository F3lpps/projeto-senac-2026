from conta_bancaria import ContaBancaria

if __name__ == '__main__':
    
    conta = ContaBancaria("João")
    saque = conta.sacar(2)
    assert saque is False

    conta.depositar(10.0)
    assert conta.saldo == 10.0