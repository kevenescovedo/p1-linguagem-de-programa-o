
"""
###**2.**	Para fazer o cadastro do Facebook o usuário deve preencher vários dados, inclusive um e-mail válido, ou seja, um e-mail deve conter no mínimo um ‘**@**’ e um ’**.**’
### Crie uma função que identifique se um e-mail é válido ou não. Não use nenhum método/função pronto da linguagem Python. Avalie caracter por caracter.
"""


def validacao_email(email):
   qtd_arroba = 0
   qtd_ponto = 0
   for x in range(len(email)):
    
     if '.' == email[x]:
         qtd_ponto = qtd_ponto + 1
     if '@' in email[x]:
         qtd_arroba = qtd_arroba + 1
   print(qtd_arroba)
   print(qtd_ponto)     
   if qtd_arroba == 1 and qtd_ponto >= 1:
    
     print("email valido")
   else:
     print("email invalido")
         
         
     


def main():
  email = input('Informe o seu email para poder se cadastrar no Facebook: ')
  validacao_email(email)

main()
