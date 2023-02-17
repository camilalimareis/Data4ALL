

#Alunos: Camila Bianca dos Reis Lima, Delson Cardoso de Souza , Kleiton Rocha de Oliveira, Luíza Caroline Santos Jeremias


users = [
    [1,"Ciclano Sauro",2345678,"Rua Boa",True],
    [2,"Fulano Silva",3478358235,"Rua Top",True],
    [3,"John Doe",3853385267,"MAIOBÃO",True],
    [4,"João Roberto",23554432,"Rua ruim",True],
    [5,"Silva Sauro",34526853,"Rua ok",True]
]

def teste_id(id_teste):
  for info in users:
    id_user, nome, telefone, endereco, status = info  
    if id_teste == id_user:
      return True
    else:
      pass
  return False

def arrumar_telefone(telefone:str)-> int:
  '''Retira todos os caracteres exceto numéricos do telefone'''
  telefone_temp = []
  for letra in telefone:
    if letra.isnumeric():
      telefone_temp.append(letra)
  return ''.join(telefone_temp) 

def print_telefone(telefone:int)-> str:
  '''Print Telefone com o formato (xx)xxxxx-xxxx'''
  return f'({telefone[0:2]}) {telefone[2:7]}-{telefone[7:]}'

resposta = ''
nome = ''
telefone = ''
endereco = ''

menu_str = """
O que deseja fazer:\n
1 - Inserir usuário
2 - Excluir usuário
3 - Atualizar usuário
4 - Informações de um usuário
5 - Informações de todos os usuários
6 - Sair\n
"""

sub_menu = """
\nQual informação deseja alterar?
1 - Nome
2 - Tefone
3 - Endereço
\n
"""

print('\nBoas vindas ao nosso sistema:')

while resposta != '6':
  print(menu_str)
  resposta = input()

  if resposta == '1':
    print('Inserir novo usuário','\n','-'*50,'\n')

    nome = input('Qual o nome do usuário: \n')
    telefone = input('Qual o telefone do usuário: (xx)xxxxx-xxxx\n')  
    endereco = input('Qual o endereço do usuário: \n')

    telefone = arrumar_telefone(telefone)

    sucesso_inserir = f'''
***********************
Usuário inserido com sucesso
***********************
Nome: {nome}
Telefone: {print_telefone(telefone)}
Endereço: {endereco}
    ''' 
    
    users.append([max(users)[0]+1,nome,telefone,endereco,True])
    print(sucesso_inserir)
    continue
    
  elif resposta == '2':
    id_desativado = int(input('\nDigite o id do usuário que deseja excluir: '))
    testando_id = teste_id(id_desativado)
    while testando_id == False:
      print('\nInsira um id valído!\n')  
      id_desativado = int(input('\nDigite o id do usuário que deseja excluir: '))
      testando_id = teste_id(id_desativado)

    i=0   #contador
    for info in users:
      id_user, nome, telefone, endereco, status = info
      if id_desativado == id_user:
        if status == False: 
          print('\nUsuário não encontrado\n') 
        elif status == True:
          users[i][4] = False 
          print(f'\n\nUsuário {id_desativado} excluído com sucesso!\n\n') 
        else:
          print('Erro!')
      i=i+1
   
   
  elif resposta == '3':
    cliente_desejado = input('\nInsira o ID do usuário: ')

    while not cliente_desejado.isnumeric():
      print('\nID inválido! Digite somente números')
      cliente_desejado = input('\nInsira o ID do usuário: ')

    cliente_desejado = int(cliente_desejado)

    encontrado = False

    for info in users:
        id_user, nome, telefone, endereco, status = info
        
        if id_user == cliente_desejado:
            encontrado = True
            
            info_alteracao = int(input('\nQual informação deseja alterar? \n1 - Nome \n2 - Telefone \n3 - Endereço\n'))
                
            if info_alteracao!=1 and info_alteracao!=2 and info_alteracao!=3:
                
                while info_alteracao!=1 and info_alteracao!=2 and info_alteracao!=3:
                    print('\nOpção inválida!')
                    info_alteracao = int(input('\nQual informação deseja alterar? \n1 - Nome \n2 - Telefone \n3 - Endereço\n'))
            
            elif info_alteracao==1:
                
                nome_atualizado = (input('\nInsira o novo nome : '))
                users[cliente_desejado-1][info_alteracao] = nome_atualizado
                print('\nAtualizado.')  
            
            elif info_alteracao==2:
                
                telefone_atualizado = input('\nInsira o novo telefone : ')
                telefone_atualizado = arrumar_telefone(telefone_atualizado)
                users[cliente_desejado-1][info_alteracao] = telefone_atualizado
                print('\nAtualizado.')
            
            elif info_alteracao==3:
                
                endereco_atualizado = input('\nInsira o novo endereço: ')
                users[cliente_desejado-1][info_alteracao] = endereco_atualizado
                print('\nAtualizado.')
            
            break

    if not encontrado:
        print("\nId não encontrado.")

  elif resposta == '4':

    id_exibir = int(input('\nDigite o id do usuário que deseja exibir: '))
    testando_id_exibir = teste_id(id_exibir)
    while testando_id_exibir == False:
      print('Insira um ID válido!\n\n')  
      id_exibir = int(input('Digite o id do usuário que deseja exibir: '))
      testando_id_exibir = teste_id(id_exibir)
    contador=0
    for info in users:
      id_user, nome, telefone, endereco, status = info
      if id_exibir == id_user:
        if status == False: 
          print('Usuário não encontrado') 
        elif status == True: 
          print(f'\nNome:{users[contador][1]}\nTelefone:{users[contador][2]}\nEndereço:{users[contador][3]}') 
        else:
          print('Erro!')
      contador=contador+1
  
  elif resposta == '5':
    for info in users:
      id_user, nome, telefone, endereco, status = info
      if status == True:
        telefone = str(telefone)
        print(f'''ID: {id_user}
            Nome:{nome}
            telefone:({telefone[0:2]}){telefone[2:7]}-{telefone[7:]}
            Endereço: {endereco}''')
      else:
        pass
     
  elif resposta == '6':
    print('Processo finalizado pelo usuário.\nObrigado')
  else:
    print('Valor digitado incorreto, favor verificar')