from datetime import date, datetime

class Transacao:
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)

class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Conta:
    def __init__(self, cliente, numero: int):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    def saldo_conta(self):
        return self.saldo

    def sacar(self, valor: float) -> bool:
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.historico.adicionar_transacao(Saque(valor))
            print(f"\n[Saque] R${valor:.2f} realizado com sucesso.")
            return True
        print("\n[Saque] Saque não autorizado.")
        return False

    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao(Deposito(valor))
            print(f"\n[Depósito] R${valor:.2f} realizado com sucesso.")
            return True
        print("\n[Depósito] Valor inválido.")
        return False

    @classmethod
    def nova(cls, cliente, numero: int):
        return cls(cliente, numero)

class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome: str, cpf: str, data_nascimento: date, endereco: str):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


clientes = []
contas = []
proximo_numero_conta = 1


def encontrar_cliente_por_cpf(cpf: str):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None


def criar_cliente():
    print("\n--- Cadastro de Cliente ---")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    nascimento_str = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço: ")

    try:
        nascimento = datetime.strptime(nascimento_str, "%d/%m/%Y").date()
    except ValueError:
        print("Data inválida.")
        return

    if encontrar_cliente_por_cpf(cpf):
        print("CPF já cadastrado!")
        return

    cliente = PessoaFisica(nome, cpf, nascimento, endereco)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")


def criar_conta():
    global proximo_numero_conta
    print("\n--- Criar Conta ---")
    cpf = input("Informe o CPF do cliente: ")

    cliente = encontrar_cliente_por_cpf(cpf)
    if not cliente:
        print("Cliente não encontrado.")
        return

    conta = Conta.nova(cliente, proximo_numero_conta)
    cliente.adicionar_conta(conta)
    contas.append(conta)
    proximo_numero_conta += 1

    print(f"Conta criada com sucesso! Número: {conta.numero}")


def acessar_conta():
    print("\n--- Acessar Conta ---")
    cpf = input("Informe seu CPF: ")
    cliente = encontrar_cliente_por_cpf(cpf)
    if not cliente:
        print("Cliente não encontrado.")
        return

    if not cliente.contas:
        print("Cliente não possui contas.")
        return

    print("\nContas disponíveis:")
    for i, conta in enumerate(cliente.contas):
        print(f"{i + 1} - Conta {conta.numero} | Saldo: R${conta.saldo_conta():.2f}")

    opcao = input("Escolha o número da conta: ")
    try:
        index = int(opcao) - 1
        conta = cliente.contas[index]
    except:
        print("Opção inválida.")
        return

    menu_operacoes(cliente, conta)


def menu_operacoes(cliente, conta):
    while True:
        print(f"\n--- Conta {conta.numero} ---")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver saldo")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            valor = float(input("Valor do depósito: "))
            cliente.realizar_transacao(conta, Deposito(valor))

        elif op == "2":
            valor = float(input("Valor do saque: "))
            cliente.realizar_transacao(conta, Saque(valor))

        elif op == "3":
            print(f"Saldo atual: R${conta.saldo_conta():.2f}")

        elif op == "0":
            break
        else:
            print("Opção inválida.")


def menu_principal():
    while True:
        print("\n~~BANCO DA SOPHIA~~")
        print("1 - Cadastrar cliente")
        print("2 - Criar conta")
        print("3 - Acessar conta")
        print("0 - Sair")

        escolha = input("Escolha: ")

        if escolha == "1":
            criar_cliente()
        elif escolha == "2":
            criar_conta()
        elif escolha == "3":
            acessar_conta()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_principal()
