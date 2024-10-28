class Produto:
    def __init__(self, nome, categoria, quantidade, valor, rastrear):
        self.nome=nome
        self.categoria=categoria
        self.quantidade=quantidade
        self.valor=valor
        self.rastear=rastrear

class Estoque:
    def __init__(self):
        self.produtos={}

    def cadastrar_produtos(self, nome, categoria, quantidade, valor, rastrear):
        produto=Produto(nome, categoria, quantidade, valor, rastrear)
        self.produtos[nome]=produto
        print(f"O produto {nome} foi cadastrado com sucesso! :) ")    

    def atualizar_estoque(self, nome, quantidade):
        if nome in self.produtos:
            self.produtos[nome].quantidade += quantidade
            print(f"Estoque do produto {nome} foi atualizado com sucesso! :) ")
        else:
            print(f"Sinto muito, o produto {nome} não foi encontrado. :( ")    

    def rastrear_localizacao(self, nome):
        if nome in self.produtos:
            print(f"O produto {nome} foi rastreado. Aqui está sua localização{self.produtos[nome].rastrear} :) ")
        else:
            print(f"Sinto muito, o produto {nome} não foi encontrado. :( ")  

    def gerar_relatorio(self):
        print("Relatório do Estoque:")
        for produto in self.produtos.values():
            if produto.quantidade <=5:
                print(f"{produto.nome}: O estoque desse produto está Baixo ({produto.quantidade}) ")
            elif produto.quantidade >=50:
                print(f"{produto.nome}: O estoque desse produto está Em Excesso ({produto.quantidade}) ")
            else:
                print(f"{produto.nome}: O estoque desse produto está Normal ({produto.quantidade}) ") 

def main():
    estoque=Estoque()

    while True:
        print("\nMenu:")    
        print("1. Cadastrar Produto")
        print("2. Atualizar Estoque")
        print("3. Rastrear Localização")
        print("4. Gerar Relatório")
        print("5. Sair")

        escolha=input("Qual ação deseja realizar? (escolha uma das opções numeradas acima)")

        if escolha=="1":
            nome=input("Informe o nome: ")
            categoria=input("Informe a categoria: ")
            quantidade=int(input("Informe a quantidade em estoque: ")) 
            valor=float(input("Informe o valor: "))      
            rastrear=input("Informe a localização: ")
            estoque.cadastrar_produto(nome, categoria, quantidade, valor, rastrear)
        elif escolha=="2":
            nome=input("Informe o nome: ")
            quantidade=input("Informe a quantidade adicional: ")
            estoque.atualizar_estoque(nome, quantidade)
        elif escolha=="3":
            nome=input("Informe o nome: ")
            estoque.rastrear_localizacao(nome)
        elif escolha=="4":
            estoque.gerar_relatorio()
        elif escolha=="5":
            break
        else:
            print("Não encontramos essa opção. Por favor, tente novamente. *o* ")

if __name__=="__main__":
    main()                     