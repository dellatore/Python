#Importando as bibliotecas
import pygame

#Inicializando o Pygame
pygame.init() #inicializando o pygame
tela = pygame.display.set_mode((600,400)) #definindo as proporções da tela
relogio = pygame.time.Clock() #defini quanto tempo o jogo ficara rodadndo 
rodando = True
delta = 0 
VALOR_MOVIMENTO = 100 #CONSTANTE 

jogador_posicao = pygame.Vector2(tela.get_width() / 2, tela.get_height() / 2) #inicializa a posição do jogador
jogador2_posicao = pygame.Vector2(40,40)

#Loop Principal
while rodando:
    #Eventos:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    #Atualização do projeto        
    tela.fill("white") #cor do background 
    
    pygame.draw.circle(tela, "red", jogador_posicao,40) #definindo o objeto jogador
    pygame.draw.circle(tela, "blue", jogador2_posicao,40)
    
    
    teclas = pygame.key.get_pressed() #pega a ação do usuario
    
    
    #MOVIMENTAÇÃO JOGADOR1
    #k ==> key <> chave
    if teclas[pygame.K_w]:  #move para cima
        if (jogador_posicao.y - VALOR_MOVIMENTO * delta) >= 89 and  (0 < jogador_posicao.x >60 ):
            jogador_posicao.y -= VALOR_MOVIMENTO * delta
        
    if teclas[pygame.K_s]:  #move para baixo
        jogador_posicao.y += VALOR_MOVIMENTO * delta
        
    
    if teclas[pygame.K_a]:  #move para a esquerda
        jogador_posicao.x -= VALOR_MOVIMENTO * delta
        
        
    if teclas[pygame.K_d]:  #move para a direita
        jogador_posicao.x += VALOR_MOVIMENTO * delta
        
        
    #MOVIMENTAÇÃO JOGADOR2
    if teclas[pygame.K_UP]:
        jogador2_posicao.y -= VALOR_MOVIMENTO * delta
        
    if teclas[pygame.K_DOWN]:
        jogador2_posicao.y += VALOR_MOVIMENTO * delta
        
    if teclas[pygame.K_LEFT]:
        jogador2_posicao.x -= VALOR_MOVIMENTO * delta
        
    if teclas[pygame.K_RIGHT]:
        jogador2_posicao.x += VALOR_MOVIMENTO * delta    
    
    #Renderização
    pygame.display.flip()
    delta = relogio.tick(60) / 1000
    
    