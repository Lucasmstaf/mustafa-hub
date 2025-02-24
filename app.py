import os

restaurantes = [{'nome':'McDonalds', 'categoria':'Alimentos', 'ativo':True}, 
{'nome':'BurguerKing','categoria':'Alimentos' ,'ativo':False}, 
{'nome':'Centauro','categoria':'Esportes', 'ativo':True}, 
{'nome':'Americanas', 'categoria':'Diversos' ,'ativo':True}]

def exibir_titulo_do_programa():
    '''Essa função exibe o título do programa'''
    
    print ('''
███╗░░░███╗██╗░░░██╗░██████╗████████╗░█████╗░███████╗░█████╗░  ██╗░░██╗██╗░░░██╗██████╗░
████╗░████║██║░░░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗  ██║░░██║██║░░░██║██╔══██╗
██╔████╔██║██║░░░██║╚█████╗░░░░██║░░░███████║█████╗░░███████║  ███████║██║░░░██║██████╦╝
██║╚██╔╝██║██║░░░██║░╚═══██╗░░░██║░░░██╔══██║██╔══╝░░██╔══██║  ██╔══██║██║░░░██║██╔══██╗
██║░╚═╝░██║╚██████╔╝██████╔╝░░░██║░░░██║░░██║██║░░░░░██║░░██║  ██║░░██║╚██████╔╝██████╦╝
╚═╝░░░░░╚═╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝  ╚═╝░░╚═╝░╚═════╝░╚═════╝░ 
''')  

def exibir_menu_do_programa():
    '''Essa função exibe o menu do programa''' 
    
    print ('1. Cadastrar Restaurante')
    print ('2. Listar Restaurantes')
    print ('3. Alternar Estado Do Restaurante')
    print ('4. Sair\n')

def saindo_do_programa():
    '''Essa função exibe uma mensagem de saída do programa'''
    
    exibir_subtitulo('Saindo do programa')
   
def opcao_invalida():
    '''Essa função exibe uma mensagem de opção inválida'''
    
    print('Opção inválida\n')
    input('Aperte qualquer tecla para voltar para o menu principal')
    main()

def voltar_pro_menu_principal():
    '''Essa função volta para o menu principal'''
    
    input('\nAperte qualquer tecla para voltar para o menu principal ')
    main()

def exibir_subtitulo(subtitulo):
    '''Essa função exibe um subtitulo'''
    
    os.system('cls')
    linha = '-' * len(subtitulo)
    print(linha)
    print(subtitulo)
    print(linha)
    print()

def cadastrar_restaurante():
    '''Essa função cadastra um restaurante'''
    
    exibir_subtitulo('Cadastro de Restaurante')

    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso\n')
    
    voltar_pro_menu_principal()

def listando_restaurantes():
    '''Essa função lista os restaurantes cadastrados'''
    
    exibir_subtitulo('Listagem de Restaurantes')

    print('Nome do Restaurante'.ljust(22), '| Categoria'.ljust(22), '| Status')
    print('-' * 60)
    for restaurante in restaurantes:
        nome_do_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_do_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')  
    
    voltar_pro_menu_principal()

def alterar_status_do_restaurante():
    '''Essa função altera o status do restaurante'''
    
    exibir_subtitulo('Alterar status do restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'] == nome_do_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'O restaurante {nome_do_restaurante} foi {mensagem} com sucesso\n')

    if not restaurante_encontrado:
        print(f'O restaurante {nome_do_restaurante} não foi encontrado\n')

    voltar_pro_menu_principal()

def escolher_opcao():
    '''Essa função escolhe a opção do menu'''
    
    try:
        opcao_escolhida = int(input('Digite a opção desejada: '))
        
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listando_restaurantes()
            case 3:
                alterar_status_do_restaurante()
            case 4:
                saindo_do_programa()
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    '''Essa função é a principal do programa'''
    
    os.system('cls')
    exibir_titulo_do_programa()
    exibir_menu_do_programa()
    escolher_opcao()

if __name__ == '__main__':
    main()