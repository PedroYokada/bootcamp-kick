import random

def escolha_computador():
    opcoes = ["pedra", "papel", "tesoura"]
    return random.choice(opcoes)

def escolha_jogador():
    escolha = input("Escolha pedra, papel ou tesoura: ").lower()
    while escolha not in ["pedra", "papel", "tesoura"]:
        escolha = input("Escolha inválida. Escolha pedra, papel ou tesoura: ").lower()
    return escolha

def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "empate"
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        return "jogador"
    else:
        return "computador"

def jogar():
    vitorias = 0
    derrotas = 0
    empates = 0

    while True:
        jogador = escolha_jogador()
        computador = escolha_computador()

        print(f"Você escolheu: {jogador}")
        print(f"O computador escolheu: {computador}")

        resultado = determinar_vencedor(jogador, computador)

        if resultado == "empate":
            print("Empate!")
            empates += 1
        elif resultado == "jogador":
            print("Você venceu!")
            vitorias += 1
        else:
            print("Você perdeu!")
            derrotas += 1

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            break

    print("\nEstatísticas do Jogo:")
    print(f"Vitórias: {vitorias}")
    print(f"Derrotas: {derrotas}")
    print(f"Empates: {empates}")

# Iniciar o jogo
jogar()
