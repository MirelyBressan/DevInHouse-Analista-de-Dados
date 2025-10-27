#funções relacionadas a datas

from datetime import datetime, date

def data_atual():
    """Retorna a data atual formatada"""
    hoje = date.today()
    return hoje.strftime("%d/%m/%Y")

def diferenca_dias(data1, data2):
    """Calcula a diferença em dias entre duas datas"""
    formato = "%d/%m/%Y"
    d1 = datetime.strptime(data1, formato)
    d2 = datetime.strptime(data2, formato)
    diferenca = abs((d2 - d1).days)
    return diferenca
