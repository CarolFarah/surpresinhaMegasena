from random import *


print(30*"-")
print("     JOGOS DA MEGA SENA")
print(30*"-")

jogos = int(input("\nQuantos jogos deseja sortear: "))

print(f"\n-=-=-= SORTEANDO {jogos} JOGOS =-=-=-")
for i in range(1, jogos+1):
    palpite = sample(range(1, 61), 6)
    print(f'Jogo {i}: {palpite}')

print('-=-=-=-=-= < BOA SORTE! > =-=-=-=-=-')





