import random
import time

# Computador "pensa" em um número entre 0 e 5
numero_computador = random.randint(0, 5)

print("-=" * 30)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=" * 30)

# Pequena pausa para efeito dramático
print("PROCESSANDO...")
time.sleep(2)

# Usuário tenta adivinhar
numero_usuario = int(input("Em que número eu pensei? "))

# Verifica se o usuário acertou
if numero_usuario == numero_computador:
    print(f"PARABÉNS! Você acertou! Eu pensei no número {numero_computador}.")
else:
    print(f"QUE PENA! Você errou! Eu pensei no número {numero_computador} e você disse {numero_usuario}.")