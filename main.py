import pygame
from sys import exit

# Inicializa o pygame
pygame.init()

# Cria
tamanho = (700,300)
tela = pygame.display.set_mode(tamanho)

# Define o titulo da tela
pygame.display.set_caption("Capivara Runner")

# Cria um relógio para controlar os frames
relogio = pygame.time.Clock()

# Importa a imagem da capivara
capivara_supe = pygame.image.load('assets/capivara/andando/tile000.png')
capivara_rect = capivara_supe.get_rect(center = (30, 150))

# Propriedades da Capivara
gravidade_capivara = 0

# Imagens de fundo
chao_super = pygame.image.load('assets/fundos/ground.png')
ceu_super = pygame.image.load('assets/fundos/Sky.png')

# Importa Gamba
gamba_supe = pygame.image.load('assets/gamba/tile000.png')
gamba_rect = gamba_supe.get_rect(center = (730, 150))

# LOOP PRINCIPAL
while True:
    # Verifica a ocorrencia de eventos
    for evento in pygame.event.get():
        # Verfica se o usuário quer sair
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

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

    # Coloca o gamba na tela
    tela.blit(gamba_supe, gamba_rect)
    gamba_rect.x -= 5

    # Impede a capivara de cair
    if capivara_rect.centery > 150: capivara_rect.centery = 150

    # Atualiza a tela
    pygame.display.update()

    # Define a quantidade de frames por segundo
    relogio.tick(60)