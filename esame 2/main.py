import pygame
import random
import sys

# Inizializzazione Pygame
pygame.init()

# Impostazioni dello schermo
larghezza_schermo = 400  # Ridotta la larghezza
altezza_schermo = 400  # Ridotta l'altezza
schermo = pygame.display.set_mode((larghezza_schermo, altezza_schermo))
pygame.display.set_caption("Snake di giammy")

# Caricamento delle immagini
sfondo_img = pygame.image.load('sfondo_riprova.jpeg')
sfondo_img = pygame.transform.scale(sfondo_img, (200, 200))  # Ridimensiona lo sfondo

# Caricamento immagini della mela di varie dimensioni
mela_imgs = {
    10: pygame.transform.scale(pygame.image.load('mela.png'), (10, 10)),
    15: pygame.transform.scale(pygame.image.load('mela.png'), (15, 15)),
    20: pygame.transform.scale(pygame.image.load('mela.png'), (20, 20))
}

# Colori
nero = (0, 0, 0)
verde = (0, 200, 0)
bianco = (255, 255, 255)

# Impostazioni del serpente
dimensione_blocco = 20

# Font
font = pygame.font.SysFont(None, 30)

# Variabili di gioco
direzione = 'DESTRA'
cambio_direzione = direzione
mele_mangiate = 0
lunghezza_serpente = 1
serpente = []
testa_serpente = [larghezza_schermo / 2, altezza_schermo / 2]
serpente.append(testa_serpente)
dimensione_mela = 20  # Imposta la dimensione predefinita della mela
posizione_mela = [random.randint(1, (larghezza_schermo - dimensione_blocco) // dimensione_blocco) * dimensione_blocco,
                  random.randint(1, (altezza_schermo - dimensione_blocco) // dimensione_blocco) * dimensione_blocco]

# Variabile di fine partita
fine_partita = False

# Variabile di difficoltà
difficolta = 'normale'

# Velocità iniziale del serpente
velocita_serpente = 10

def mostra_menu():
    global difficolta
    menu = True

    while menu:
        schermo.fill(nero)
        mostra_testo("Scegli la difficoltà:", bianco, -50)
        mostra_testo("1. Facile", bianco, -10)
        mostra_testo("2. Normale", bianco, 20)
        mostra_testo("3. Difficile", bianco, 50)
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    difficolta = 'facile'
                    menu = False
                if evento.key == pygame.K_2:
                    difficolta = 'normale'
                    menu = False
                if evento.key == pygame.K_3:
                    difficolta = 'difficile'
                    menu = False

def fine_gioco():
    global fine_partita
    fine_partita = True

    while True:
        schermo.fill(nero)
        schermo.blit(sfondo_img, (100, 100))  # Posiziona lo sfondo ridimensionato
        mostra_testo("Premi 'R' per riprovare o 'ESC' per uscire.", bianco, 50)
        mostra_punteggio()
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    fine_partita = False
                    reset_game()
                    return
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def reset_game():
    global direzione, cambio_direzione, mele_mangiate, lunghezza_serpente, serpente, testa_serpente, posizione_mela, velocita_serpente
    direzione = 'DESTRA'
    cambio_direzione = direzione
    mele_mangiate = 0
    lunghezza_serpente = 1
    serpente.clear()
    testa_serpente = [larghezza_schermo / 2, altezza_schermo / 2]
    serpente.append(testa_serpente)
    posizione_mela = [random.randint(1, (larghezza_schermo - dimensione_blocco) // dimensione_blocco) * dimensione_blocco,
                      random.randint(1, (altezza_schermo - dimensione_blocco) // dimensione_blocco) * dimensione_blocco]
    velocita_serpente = 10 # Resetta la velocità

def mostra_punteggio(velocita_attuale=''):
    testo = font.render("Mele mangiate: " + str(mele_mangiate), True, bianco)
    schermo.blit(testo, [10, 10])
    # Mostra la velocità attuale del serpente in alto a destra
    testo_velocita = font.render("Velocità: " + str(velocita_attuale), True, bianco)
    schermo.blit(testo_velocita, [larghezza_schermo - 150, 10])

def mostra_testo(testo, colore, y_displacement=0):
    surface = font.render(testo, True, colore)
    rect = surface.get_rect()
    rect.center = (larghezza_schermo / 2), (altezza_schermo / 2) + y_displacement
    schermo.blit(surface, rect)

def main():
    global direzione, cambio_direzione, mele_mangiate, lunghezza_serpente, serpente, testa_serpente, posizione_mela, fine_partita, dimensione_mela, velocita_serpente

    # Mostra il menu di selezione della difficoltà
    mostra_menu()

    # Imposta la velocità del serpente in base alla difficoltà
    if difficolta == 'facile':
        velocita_serpente = 10
    elif difficolta == 'medio':
        velocita_serpente = 10
    elif difficolta == 'difficile':
        velocita_serpente = 10

    while True:
        schermo.fill(nero)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and direzione != 'DESTRA':
                    cambio_direzione = 'SINISTRA'
                if evento.key == pygame.K_RIGHT and direzione != 'SINISTRA':
                    cambio_direzione = 'DESTRA'
                if evento.key == pygame.K_UP and direzione != 'GIU':
                    cambio_direzione = 'SU'
                if evento.key == pygame.K_DOWN and direzione != 'SU':
                    cambio_direzione = 'GIU'
                if evento.key == pygame.K_1:  # Imposta dimensione mela a 10
                    dimensione_mela = 10
                if evento.key == pygame.K_2:  # Imposta dimensione mela a 15
                    dimensione_mela = 15
                if evento.key == pygame.K_3:  # Imposta dimensione mela a 20
                    dimensione_mela = 20
                if evento.key == pygame.K_r:  # Resetta il gioco e la velocità
                    reset_game()

        direzione = cambio_direzione

        # Muovi il serpente
        if direzione == 'SU':
            testa_serpente[1] -= dimensione_blocco
            if difficolta != 'difficile' and testa_serpente[1] < 0:  # Rimbalza dal bordo in facile e normale
                testa_serpente[1] = altezza_schermo - dimensione_blocco
        if direzione == 'GIU':
            testa_serpente[1] += dimensione_blocco
            if difficolta != 'difficile' and testa_serpente[1] >= altezza_schermo:  # Rimbalza dal bordo in facile e normale
                testa_serpente[1] = 0
        if direzione == 'SINISTRA':
            testa_serpente[0] -= dimensione_blocco
            if difficolta != 'difficile' and testa_serpente[0] < 0:  # Rimbalza dal bordo in facile e normale
                testa_serpente[0] = larghezza_schermo - dimensione_blocco
        if direzione == 'DESTRA':
            testa_serpente[0] += dimensione_blocco
            if difficolta != 'difficile' and testa_serpente[0] >= larghezza_schermo:  # Rimbalza dal bordo in facile e normale
                testa_serpente[0] = 0

        # Meccaniche del corpo del serpente
        serpente.append(list(testa_serpente))
        if len(serpente) > lunghezza_serpente:
            del serpente[0]

        # Condizioni di fine partita
        if difficolta == 'difficile':  # Se il serpente tocca i bordi in modalità difficile, è fine partita
            if testa_serpente[0] < 0 or testa_serpente[0] >= larghezza_schermo or \
                    testa_serpente[1] < 0 or testa_serpente[1] >= altezza_schermo:
                fine_gioco()

        for blocco in serpente[:-1]:
            if blocco == testa_serpente:
                fine_gioco()

        # Controllo se il serpente ha mangiato la mela
        if testa_serpente[0] == posizione_mela[0] and testa_serpente[1] == posizione_mela[1]:
            mele_mangiate += 1
            lunghezza_serpente += 1
            posizione_mela = [random.randint(1, (larghezza_schermo - dimensione_blocco) // dimensione_blocco) * dimensione_blocco,
                              random.randint(1, (altezza_schermo - dimensione_blocco) // dimensione_blocco) * dimensione_blocco]
            # Aumenta leggermente la velocità per ogni mela mangiata
            velocita_serpente += 1

        # Disegna la griglia
        for x in range(0, larghezza_schermo, dimensione_blocco):
            pygame.draw.line(schermo, verde, (x, 0), (x, altezza_schermo))
        for y in range(0, altezza_schermo, dimensione_blocco):
            pygame.draw.line(schermo, verde, (0, y), (larghezza_schermo, y))

        # Disegna il serpente
        for pos in serpente:
            pygame.draw.rect(schermo, verde, pygame.Rect(pos[0], pos[1], dimensione_blocco, dimensione_blocco))

        # Disegna l'immagine della mela
        schermo.blit(mela_imgs[dimensione_mela], (posizione_mela[0], posizione_mela[1]))

        # Mostra il numero di mele mangiate e la velocità attuale del serpente
        mostra_punteggio(velocita_serpente)

        # Aggiorna lo schermo
        pygame.display.update()

        # Controllo della velocità del serpente
        pygame.time.Clock().tick(velocita_serpente)

if __name__ == "__main__":
    main()
