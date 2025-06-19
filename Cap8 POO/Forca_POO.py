import random

RESET = "\033[0m"
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AZUL = "\033[94m"
AMARELO = "\033[93m"
CIANO = "\033[96m"


class JogoDaForca:

    def __init__(self):
        self.palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
        self.palavra_secreta = random.choice(self.palavras)
        self.tabuleiro = ['_'] * len(self.palavra_secreta)
        self.chances = 6
        self.letras_tentadas = []

    def iniciar_jogo(self):
        print(f"\n{VERDE}Bem-vindo(a) ao Jogo da Forca!{RESET}")
        print(f"Adivinhe a palavra {AMARELO}SECRETA!{RESET}\n")

        while self.chances > 0 and '_' in self.tabuleiro:
            self.mostrar_tabuleiro()
            tentativa = input(f"{CIANO}Digite uma letra:{RESET} ").lower()

            if not tentativa.isalpha() or len(tentativa) != 1:
                print("Digite apenas uma letra válida.\n")
                continue

            self.verificador_letra(tentativa)

        # Fim de Jogo
        if "_" not in self.tabuleiro:
            print(f"{RESET}Palavra:{VERDE}", " ".join(self.tabuleiro))
            print(f"\n{VERDE}Parabéns! Você venceu! A palavra era: {self.palavra_secreta}\n")
        else:
            self.mostrar_forca()
            print(f"\n{VERMELHO}Você perdeu. A palavra era: {self.palavra_secreta}\n")


    def mostrar_tabuleiro(self):
        self.mostrar_forca()
        print(f"\n{AZUL}Chances restantes:{RESET} {self.chances}")
        print(f"{CIANO}Letras já tentadas:{AMARELO}", ", ".join(self.letras_tentadas))
        print(f"\n{VERDE}Palavra:", " ".join(self.tabuleiro), RESET)
        print()

    def verificador_letra(self, letra):

        if letra in self.letras_tentadas:
            return print(f"{VERMELHO}Você já tentou essa letra.{RESET}")
            
        self.letras_tentadas.append(letra)

        if letra in self.palavra_secreta:
            print(f"\n{VERDE}Boa! Você acertou essa letra.{RESET}")
            for i in range(len(self.palavra_secreta)):
                if self.palavra_secreta[i] == letra:
                    self.tabuleiro[i] = letra

        else:
            print(f"\n{VERMELHO}Ops! Letra incorreta{RESET}")
            self.chances -= 1

    def mostrar_forca(self):
        estagios = [
            """
               --------
               |      |
               |      
               |      
               |      
               |      
               -
            """,  # 0 erros
            """
               --------
               |      |
               |      O
               |      
               |      
               |      
               -
            """,  # 1 erro
            """
               --------
               |      |
               |      O
               |      |
               |      |
               |      
               -
            """,  # 2 erros
            """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |      
               -
            """,  # 3 erros
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -
            """,  # 4 erros
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -
            """,  # 5 erros
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            """   # 6 erros
        ]
        print(estagios[6 - self.chances])

if __name__ == '__main__':
    jogo = JogoDaForca()
    jogo.iniciar_jogo()