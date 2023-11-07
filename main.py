import pygame
from sys import exit
from random import randint

# Inicializa o pygame
pygame.init()

# Cria
tamanho = (700,300)
tela = pygame.display.set_mode(tamanho)

# Define o titulo da tela
pygame.display.set_caption("Capivara Runner")

# Cria um relógio para controlar os frames
relogio = pygame.time.Clock()

# Importa a fonte do jogo
pixel_font = pygame.font.Font('assets/font/Pixeltype.ttf', 80)

# Importa a imagem da capivara
# capivara_supe = pygame.image.load('assets/capivara/andando/tile000.png')
capivara_lista_imagens = []
for imagem in range(0, 8):
    capivara_superficie = pygame.image.load(f'assets/capivara/andando/tile00{imagem}.png')
    capivara_lista_imagens.append(capivara_superficie)

index_capivara = 0
capivara_supe = capivara_lista_imagens[index_capivara] 
capivara_rect = capivara_supe.get_rect(center = (60, 150))

# Propriedades da Capivara
gravidade_capivara = 0

# Imagens de fundo
chao_super = pygame.image.load('assets/fundos/ground.png')
ceu_super = pygame.image.load('assets/fundos/Sky.png')

# Importa Gamba
gamba_supe = pygame.image.load('assets/gamba/tile000.png')
gamba_rect = gamba_supe.get_rect(center = (730, 150))
lista_gambas = []

# TIMER
novo_gamba_timer = pygame.USEREVENT + 1
pygame.time.set_timer(novo_gamba_timer, 800)

novo_ponto_timer = pygame.USEREVENT + 1
pygame.time.set_timer(novo_ponto_timer, 1000)

# Pontuacao 
pontos = 0

# LOOP PRINCIPAL
while True:
    # Verifica a ocorrencia de eventos
    for evento in pygame.event.get():
        # Verfica se o usuário quer sair
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # Verifica se uma tecla foi apertada
        if evento.type == pygame.KEYDOWN:
            # Verifica se apertou espaço
            if evento.key == pygame.K_SPACE:
                # Diminui a gravidade para -20
                # Apenas se a capivara estiver tocando o chão
                if capivara_rect.centery == 150:
                    gravidade_capivara = -15

        # Adiciona um novo gamba na lista de gambas
        if evento.type == novo_gamba_timer:
            x = randint(730, 950)
            novo_gamba = gamba_supe.get_rect(center = (x, 150))
            lista_gambas.append(novo_gamba)

        # Adiciona um ponto a cada segundo
        if evento.type == novo_ponto_timer:
            pontos += 1

    # Coloca uma cor de fundo na tela
    tela.fill("#7FFF00")

    # Coloca as imagens de fundo
    tela.blit(ceu_super, (0, 0))
    tela.blit(chao_super, (0, 160))

    # Coloca a capivara na tela
    tela.blit(capivara_supe, capivara_rect)

    # Aumenta a gravidade de 1 em 1
    gravidade_capivara += 1
    capivara_rect.centery += gravidade_capivara

    # Desenha e movimenta a lista de gambas
    if lista_gambas:
        # Executa um código para cada gamba na lista
        for posicao, gamba in enumerate(lista_gambas):
            gamba.x -= 5
            tela.blit(gamba_supe, gamba)

            if gamba.x < -100:
                # Remove um gamba da lista de gambas
                lista_gambas.pop(posicao)

            # Verifica se a capivara colidiu com um gamba
            if capivara_rect.colliderect(gamba):
                print("Você morreu!")

    # Impede a capivara de cair
    if capivara_rect.centery > 150: capivara_rect.centery = 150

    # Mostra os pontos na tela
    pontos_text = pixel_font.render(str(pontos), False, 'black')
    pontos_rect = pontos_text.get_rect(topright = (680, 20))
    tela.blit(pontos_text, pontos_rect)

    # Atualiza a tela
    pygame.display.update()

    # Define a quantidade de frames por segundo
    relogio.tick(60)