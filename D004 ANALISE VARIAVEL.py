t = input('\033[;31mDigite algo: \033[m')
print('\033[0;34mO tipo primitivo deste valor é \033[m', type(t))
print('\033[32mSó tem espaços?\033[m', t.isspace())
print('\033[33mÉ numérico? \033[m', t.isnumeric())
print('\033[35mÉ Alphabético? \033[m', t.isalpha())
print('\033[36mÉ Alphanumérico? \033[m', t.isalnum())
print('\033[37mEstá em maiúsculas? \033[m', t.isupper())
print('\033[31mEstá em minúsculas?\033[m', t.islower())
print('\033[34mEstá capitalizado? \033[m', t.istitle())
