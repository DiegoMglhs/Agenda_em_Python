
print("********  Agenda de Contatos!  *******")
opcao =''
while opcao != 'sair':
    print("=-=-"*9)
    print(" Escolha uma das opções a Baixo:")
    opcao = input("cadastrar - pesquisar - listar - excluir - editar - sair \n")

    if opcao == 'cadastrar':
        agenda = open('agenda', 'a')
        contato = {
            "Nome": "Não informado",
            "Email": "Não informado",
            "Whats": 0000
        }
        print("informe o Nome")
        contato["Nome"] = input()
        print("informe o whats")
        contato["Whats"] = input()
        print("informe o Email")
        contato["Email"] = input()
        agenda = open('agenda', 'a')
        for x,y in contato.items():
            agenda.write(x)
            agenda.write(" : ")
            agenda.write(y)
            agenda.write(" | ")
        agenda.write("\n")
        agenda.close()
    if opcao == 'listar':
        agenda = open('agenda','r')
        print(agenda.read())
    if opcao == 'excluir':
       print("Digite o nome que deseja excluir")
       removenome = input()
       with open("agenda", "r") as f:
           lines = f.readlines()
       with open("agenda", "w") as f:
           for line in lines:
               if removenome.lower() not in line.lower():
                   f.write(line)
               else:
                   f.write("")
    if opcao == 'pesquisar':
        agenda = open('agenda', 'r')
        print("Digite o nome que deseja procurar")
        pesquisa = input()
        cont = 0
        for x in agenda:
            if (x.find(pesquisa)>=0):
                print(x, end='')
                print("Está na linha ", cont)
            cont = cont + 1
        print('****'*6)
    if opcao == 'editar':
        print("Digite o nome que deseja editar")
        alteranome = input()
        print("Qual o nome correto?")
        n = input()
        print("Qual o email correto?")
        e = input()
        print("Qual o whats correto?")
        w = input()
        with open("agenda", "r") as f:
            lines = f.readlines()
        with open("agenda", "w") as f:
            for line in lines:
                if alteranome.lower() not in line.lower():
                    f.write(line)
                else:
                    f.write("Nome : "+n +" | Email : "+e+" | Whats : "+w+" |\n")