#Aula 09 - Exercício 02
#Aluna: Juliana Silva Soares

#Criação do dicionário e listas

abreviacoes = {"bk":['black',0, 1, "-"], "br":['brown',1, 10, "1"], "rd":['red',2, 1e2, "2"],
           "or":['orange',3, 1e3, "-"], "yl":['yellow',4, 1e4,"5"],"gr":['green',5,1e5,"0.5"],
           "bl":['blue',6, 1e6, "0.25"],"vi": ['violet',7, 1e7, "0.1"],"gy":['gray',8, 1e8, "0.05"],
           "wh":['white',9, 1e9, "-"], "au":['gold','', 1, "5"], "ag":['silver','', 1, "10"],
           "--":["none",'', 1, "20"]}

corAbreviacoes = list(abreviacoes.keys())
corNomes = list(abreviacoes.values())

#Interação com o usuário

print("Verifique as abreviações das cores na tabela abaixo: \n")

print(f"{'-' * 20: ^20}")
print(f"{'Cor':<10} {'':^2} {'Código':>6}")
print(f"{'-' * 20: ^20}")
for i in range(len(corAbreviacoes)):
    print(f"{corNomes[i][0]:<10} {'':^2} {corAbreviacoes[i]:>6}")
print(f"{'-'* 20: ^20}\n")

cores = input("\nQuais as cores do resistor?\nIndique os códigos separados por espaço: ").split()

valor = abreviacoes[cores[0]][1]*10 + abreviacoes[cores[1]][1]

print(f"\nResistência: {valor * abreviacoes[cores[2]][2]} \u03A9 \u00B1 {abreviacoes[cores[3]][3]}%")