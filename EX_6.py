##6
print('='*110)
convidados = ['Gisele', 'Lula', 'Brad Pitt', 'Juliette', 'Putin']


for convidado in convidados:
    print(f"Olá {convidado}, gostaria de convidá-lo(a) para um jantar na minha casa.")
print('='*110)

desistentes = ['Gisele', 'Brad Pitt']
for desistente in desistentes:
    print(f"{desistente} não poderá comparecer.")
print('='*110)

print('Valesca e Naldo vão substituir os desistentes.')
print('='*110)

convidados.remove('Gisele')
convidados.remove('Brad Pitt')
convidados.append('Valesca')
convidados.append('Naldo')

for convidado in convidados:
    mensagem = f"Olá {convidado}, gostaria de informar que o jantar foi confirmado e conto com sua presença. Até lá!"
    print(mensagem)
print('='*110)