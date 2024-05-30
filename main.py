import PySimpleGUI as sg

# calcular a porcentagem de presença
def calcular_presenca(dias_faltados):
    total_aulas_letivas = 200 * 5  # dias multiplicado pelo número de aulas em um dia
    return ((total_aulas_letivas - dias_faltados) / total_aulas_letivas) * 100

# Layout da interface
layout = [
    [sg.Text("Quantos dias você faltou no ano?")],
    [sg.Input(key='dias_faltados')],
    [sg.Button('Calcular Presença'), sg.Button('Cancelar')],
    [sg.Text('', size=(60, 4), key='resultado')]  
]

# Criação da janela
window = sg.Window('Calculadora de Presença Escolar', layout, finalize=True)

# Maximizar a janela
window.maximize()

# Loop principal da interface
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancelar'):
        break

    if event == 'Calcular Presença':
        try:
            dias_faltados = int(values['dias_faltados']) * 5  # Cada dia faltado conta como 5 faltas
            presenca = calcular_presenca(dias_faltados)
            if presenca >= 100:
                resultado = "Parabéns, você tem 100% de presença na escola. Não teve nenhuma falta desde o início das aulas."
            elif presenca >= 85:
                resultado = "Parabéns, você tem 85% de presença na escola."
            elif presenca >= 75:
                resultado = "Você atendeu ao mínimo de 75% de presença na escola."
            else:
                resultado = "Você não atendeu ao mínimo de 75% de presença na escola."

            window['resultado'].update(f'Sua porcentagem de presença é {presenca:.2f}%. {resultado}')
        except ValueError:
            window['resultado'].update('Por favor, insira um número válido.')

window.close()
