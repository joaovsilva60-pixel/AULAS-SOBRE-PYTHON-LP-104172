import os
os.system("cls")

# ==========================================
# SISTEMA DE FOLHA DE PAGAMENTO
# ==========================================

# Funcionários cadastrados (exemplo)
funcionarios = {
    "1001": "1234",
    "1002": "5678"
}

# Configurações da empresa
PLANO_FIXO = 120.00
PLANO_POR_DEPENDENTE = 35.00


# ==========================================
# 01 - ACESSO
# ==========================================

def login():
    print("\n===== ACESSO AO SISTEMA =====")

    matricula = input("Matrícula: ")
    senha = input("Senha: ")

    if matricula in funcionarios:
        if funcionarios[matricula] == senha:
            print("\nAcesso autorizado!")
            return True

    print("\nAcesso negado! Verifique seus dados.")
    return False


# ==========================================
# 02 - DADOS DO FUNCIONÁRIO
# ==========================================

def coletar_dados():

    print("\n===== DADOS DO FUNCIONÁRIO =====")

    salario = float(input("Salário base: R$ "))

    if salario <= 0:
        raise ValueError("O salário deve ser maior que zero.")

    transporte = input(
        "Deseja vale-transporte? (S/N): "
    ).strip().upper()

    if transporte not in ("S", "N"):
        raise ValueError("Informe S ou N para o transporte.")

    if transporte == "S":
        custo_transporte = float(
            input("Custo mensal do transporte: R$ ")
        )
    else:
        custo_transporte = 0

    vale_refeicao = float(
        input("Valor do desconto do VR: R$ ")
    )

    dependentes = int(
        input("Quantidade de dependentes: ")
    )

    if custo_transporte < 0 or vale_refeicao < 0 or dependentes < 0:
        raise ValueError("Os valores não podem ser negativos.")

    return salario, transporte, custo_transporte, vale_refeicao, dependentes


# ==========================================
# 03 - FUNÇÕES DE CÁLCULO
# ==========================================

# Cálculo do INSS
def calcular_inss(salario):

    faixas = [
        (1621.00, 0.075),
        (2902.84, 0.09),
        (4354.27, 0.12),
        (8475.55, 0.14)
    ]

    desconto = 0
    limite_anterior = 0

    for limite, aliquota in faixas:

        valor = min(salario, limite) - limite_anterior

        if valor > 0:
            desconto += valor * aliquota

        limite_anterior = limite

        if salario <= limite:
            break

    return round(desconto, 2)


# Cálculo do IRRF
def calcular_irrf(salario, inss, dependentes):

    tabela = [
        (2428.80, 0, 0),
        (2826.65, 0.075, 182.16),
        (3751.05, 0.15, 394.16),
        (4664.68, 0.225, 675.49),
        (float("inf"), 0.275, 908.73)
    ]

    deducao = max(
        inss + dependentes * 189.59,
        607.20
    )

    base = max(0, salario - deducao)

    irrf = 0

    for limite, aliquota, parcela in tabela:
        if base <= limite:
            irrf = base * aliquota - parcela
            break

    if salario <= 5000:
        reducao = 312.89
    elif salario <= 7350:
        reducao = 978.62 - (0.133145 * salario)
    else:
        reducao = 0

    return round(max(0, irrf - reducao), 2)


# Cálculo do vale-transporte
def calcular_vale_transporte(salario, transporte, custo):

    if transporte == "S":
        return round(min(custo, salario * 0.06), 2)

    return 0.00


# Cálculo do vale-refeição
def calcular_vale_refeicao(valor):

    return round(valor, 2)


# Cálculo do plano de saúde
def calcular_plano_saude(dependentes):

    return round(
        PLANO_FIXO + dependentes * PLANO_POR_DEPENDENTE,
        2
    )


# ==========================================
# 04 - CONTRACHEQUE
# ==========================================

def gerar_contracheque(
    salario,
    transporte,
    custo_transporte,
    vale_refeicao,
    dependentes
):

    inss = calcular_inss(salario)

    irrf = calcular_irrf(
        salario,
        inss,
        dependentes
    )

    vt = calcular_vale_transporte(
        salario,
        transporte,
        custo_transporte
    )

    vr = calcular_vale_refeicao(vale_refeicao)

    plano = calcular_plano_saude(dependentes)

    total = inss + irrf + vt + vr + plano

    liquido = salario - total

    print("\n================================")
    print("       CONTRACHEQUE")
    print("================================")

    print(f"Salário base:       R$ {salario:10.2f}")
    print("--------------------------------")
    print(f"INSS:               R$ {inss:10.2f}")
    print(f"IRRF:               R$ {irrf:10.2f}")
    print(f"Vale-transporte:    R$ {vt:10.2f}")
    print(f"Vale-refeição:      R$ {vr:10.2f}")
    print(f"Plano de saúde:     R$ {plano:10.2f}")

    print("--------------------------------")
    print(f"Total de descontos: R$ {total:10.2f}")
    print("--------------------------------")
    print(f"SALÁRIO LÍQUIDO:    R$ {liquido:10.2f}")
    print("================================")


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def main():

    if not login():
        return

    try:
        dados = coletar_dados()

        gerar_contracheque(*dados)

    except ValueError as erro:
        print("\nErro:", erro)


# Iniciar sistema
if __name__ == "__main__":
    main()
