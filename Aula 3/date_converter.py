from datetime import datetime

def decimal_para_data(timestamp):
    data_final = datetime.fromtimestamp(timestamp)
    return data_final

numero_decimal = int(input("Digite um número decimal para converter em data: "))

data_convertida = decimal_para_data(numero_decimal)
print(data_convertida)