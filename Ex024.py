# Desafio 024? analisando o nome de uma cidade. Ver se a cidade começa com a palavra santo.
cidade = str(input('Qual cidade vc nasceu? ')).strip()
cid = cidade.lower()
'''print(cid)
print(cid[0:5] == "santo")'''
# também pode ser feito assim:
print(f'A cidade: {cidade}, começa com a palavra Santo? ')
print(cidade[0:5].lower() == "santo")

