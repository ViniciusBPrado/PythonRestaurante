import os

# Dicionário com os dados da variável restaurantes #
restaurantes = [{'nome':'Outback','categoria':'Churrasco','ativo':False},
                {'nome':'BK','categoria':'Lanches','ativo':True},
                {'nome':'Pizzaroia','categoria':'Pizza','ativo':False}]

# Função exibir_nome_do_programa, onde vai printar na tela o nome do programa que foi estilizado ( """ essas 3 aspas server para manter a formatação do texto)#
def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

# Função exibir_opções onde temos o menu do nosso programa, com o print de cada opção para ser escolhida#
def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Ativar Restaurante")
    print("4. Sair\n")

# Função para encerrar o app opção 4 do menu one ele usa a outra função exibir_subtitulo dentro dela, que vai limpar a tela e encerrar#
def finalizar_app():
    exibir_subtitulo("Finalizando a Aplicação")

# Função  para voltar ao menu principal que fica na main() que também é uma função que puxa o menu principal#
def voltar_ao_menu():
    input("Digite uma tecla para voltar ao menu principal\n")
    main()

# Função que serve para quando for digitado uma opção que não é valida para o programa, ativando a função voltar_ao_menu, indo para o menu de opções#
def opcao_invalida():
    print("Opção Inválida! \n")
    voltar_ao_menu()

# Função exibir_subtitulo, ela recebe um parâmetro que será passado na forma de text(string), limpa o console, printa o texto que foi passado pulando uma linha#
def exibir_subtitulo(texto):
    os.system("cls")
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

# Função cadastrar_restaurante  - primeiramente ele exibe a função do subtitulo, depois o nome_do_restaurante solicita um input que ai a pessoa coloca o nome que quer para o restaurante
# a ser cadastrado, em seguida ele salva esse nome no dicionario rastaurantes, depois printa na tela que foi cadastrado com sucesso e o nome do restaurante e pra finalizar retorna ao menu#
# Com a nova atualização - adicionado a variavel categoria pra receber um input da pessoa com categoria do restaurante, e alterado, adicionando dados_do_restaurante recebendo os dados
# passados pela pessoa, e colocando nessa biblioteca de dados. ao ir em listar vai aparecer esse novo restaurante com todos dados adicionados#
def cadastrar_restaurante():
    exibir_subtitulo("Cadastro de novos Restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante para cadastrar: ")
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f"\nO Restaurante {nome_do_restaurante} foi cadastrado com sucesso! \n ")
    voltar_ao_menu()

# Função listar_restaurande, primeiramente exibe o subititulo, depois cria um lança onde enquanto o restaurante estiver dentro de restaurantes ele vai pegar o que foi criado na biblioteca
# como o nome, categoria e ativo e trazer no print essas informações de todos os que estiverem dentro da biblioteca#
def listar_restaurantes():
    exibir_subtitulo("Lista de todos os restaurantes cadastrados")

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status \n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        print()
    voltar_ao_menu()

# alterando estado do restaurante
def alternar_estado_restaurante():
    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
            
    voltar_ao_menu()

# Função de escolher opção do menu. o try serve para validar se a opção escolhida é um inteiro válido caso contrário cai no except e da opção invalida. ai teremos uma estrutura de if
# onde o primero verifica se a opção escolhida é = ao numero 1, se for ai abre a função cadastrar, se for 2, listar, se for 3 , ativar e 4 encerrar o app#
def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Ativar Restaurante")
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

# Função main, do menu principal onde ele limpa o display, exibe o nome do programa, menu de opções e pede pra escolher uma opção      
def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

# Seta a main no sistema
if __name__ == '__main__':
    main()


