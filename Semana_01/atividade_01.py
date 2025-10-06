#Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
#O usuário deve escolher a unidade de entrada e a unidade de saída. 
#Use float() para garantir precisão.

#Entrada de dados
print("=== Conversor de Temperaturas ===")

temp = float(input("Digite a temperatura: "))
entrada = input("Converter a temperatura de Celsius, Fahrenheit ou Kelvin: ").lower()
saida = input("Para Celsius, Fahrenheit ou Kelvin: ").lower()

# Converção de Celsius
if entrada == "celsius":
    c = temp
elif entrada == "fahrenheit":
    c = (temp - 32) * 5/9
elif entrada == "kelvin":
    c = temp - 273.15
else:
    print("Unidade de entrada inválida!")
    exit()

# Converção de Celsius para a unidade desejada
if saida == "celsius":
    resultado = c
elif saida == "fahrenheit":
    resultado = (c * 9/5) + 32
elif saida == "kelvin":
    resultado = c + 273.15
else:
    print("Unidade de saída inválida!")
    exit()

print(f"\nResultado: {resultado:.2f} {saida.capitalize()}")
print("Conversão concluída com sucesso! ✅")