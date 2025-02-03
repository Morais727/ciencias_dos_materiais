def calcular_raio_critico(T_Celsius, Tm_Celsius, delta_Hf, gamma):
    """
    Calcula o raio crítico para nucleação homogênea.

    Parâmetros:
    T_Celsius (float): Temperatura atual (em Celsius).
    Tm_Celsius (float): Temperatura de fusão (em Celsius).
    delta_Hf (float): Calor latente de fusão (em J/kg).
    gamma (float): Energia superficial (em J/m²).

    Retorna:
    r_star (float): Raio crítico (em metros).
    """
    # Conversão de Celsius para Kelvin
    T = T_Celsius + 273.15
    Tm = Tm_Celsius + 273.15

    # Cálculo do super-resfriamento (ΔT)
    delta_T = Tm - T

    # Cálculo da variação da energia livre (ΔG_v)
    delta_Gv = (delta_Hf * delta_T) / Tm

    # Cálculo do raio crítico (r*)
    r_star = (2 * gamma) / delta_Gv

    return r_star

# Entrada de dados pelo usuário
T_Celsius = float(input("Digite a temperatura atual (em Celsius): "))
Tm_Celsius = float(input("Digite a temperatura de fusão (em Celsius): "))
delta_Hf = float(input("Digite o calor latente de fusão (em J/kg): "))
gamma = float(input("Digite a energia superficial (em J/m²): "))

# Cálculo do raio crítico
raio_critico_metros = calcular_raio_critico(T_Celsius, Tm_Celsius, delta_Hf, gamma)

# Conversão para nanômetros (1 m = 10^9 nm)
raio_critico_nm = raio_critico_metros * 1e9

# Exibição do resultado
print(f"O raio crítico para nucleação homogênea é: {raio_critico_nm:.2f} nm")