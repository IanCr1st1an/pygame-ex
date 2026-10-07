import pygame


class Input(object):

    def __init__(self):
        # o utilizador fechou a aplicação?
        self.quit = False
        # listas para armazenar os estados das teclas
        # down, up: evento discreto; dura uma iteração
        # pressed: evento contínuo, entre os eventos down e up
        self.keyDownList = []
        self.keyPressedList = []
        self.keyUpList = []

    def update(self):
        # itera sobre todos os eventos de entrada do utilizador (como teclado ou
        # rato) ocorridos desde a última vez que os eventos foram verificados
        # repõe os estados discretos das teclas
        self.keyDownList = []
        self.keyUpList = []
        for event in pygame.event.get():
            # o evento quit ocorre ao clicar no botão para fechar a janela
            if event.type == pygame.QUIT:
                self.quit = True
            # verifica os eventos keydown e keyup;
            #   obtém o nome da tecla a partir do evento
            #   e adiciona-o ou remove-o das listas correspondentes
            if event.type == pygame.KEYDOWN:
                keyName = pygame.key.name(event.key)
                self.keyDownList.append(keyName)
                self.keyPressedList.append(keyName)
            if event.type == pygame.KEYUP:
                keyName = pygame.key.name(event.key)
                if keyName in self.keyPressedList:
                    self.keyPressedList.remove(keyName)
                self.keyUpList.append(keyName)

    # funções para verificar os estados das teclas
    def isKeyDown(self, keyCode):
        return keyCode in self.keyDownList

    def isKeyPressed(self, keyCode):
        return keyCode in self.keyPressedList

    def isKeyUp(self, keyCode):
        return keyCode in self.keyUpList
