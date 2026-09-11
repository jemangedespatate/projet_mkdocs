import pygame
import random
import sys
import logique  # Import du fichier élève

# Initialisation de Pygame
pygame.init()

# --- CONSTANTES ---
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = 600 // GRID_SIZE
GRID_HEIGHT = 600 // GRID_SIZE

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_GRAY = (50, 50, 50)
ORANGE = (255, 165, 0)

# Configuration de l'écran
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake - Visualisation de Liste Python")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Consolas", 16)
large_font = pygame.font.SysFont("Consolas", 32)

def draw_grid():
    """Dessine la grille de jeu pour visualiser les cases."""
    for x in range(0, 600, GRID_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (600, y))
    
    # Ligne de séparation entre le jeu et la visualisation de la liste
    pygame.draw.line(screen, BLACK, (600, 0), (600, SCREEN_HEIGHT), 2)

def draw_snake(snake_list):
    """
    Dessine le serpent.
    Chaque élément de la liste 'snake_list' correspond à un carré sur l'écran.
    """
    for i, segment in enumerate(snake_list):
        rect = pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        # La tête est d'une couleur différente pour bien voir l'insertion à l'index 0
        color = GREEN if i == 0 else (0, 200, 0)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, DARK_GRAY, rect, 1) # Bordure

def draw_food(food_pos):
    """Dessine la nourriture (la pomme)."""
    rect = pygame.Rect(food_pos[0] * GRID_SIZE, food_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    pygame.draw.rect(screen, RED, rect)

def draw_ui(snake_list, score, last_op):
    """
    Affiche la visualisation de la liste à droite.
    C'est ici que les élèves peuvent voir le lien entre le jeu et le code.
    """
    # Fond du panneau UI
    pygame.draw.rect(screen, WHITE, (600, 0, 300, SCREEN_HEIGHT))
    
    # Titre
    title = font.render("Visualisation de la Liste", True, BLACK)
    screen.blit(title, (610, 10))
    
    # Score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (610, 40))
    
    # Dernière opération effectuée sur la liste
    op_text = font.render(f"Opération: {last_op}", True, ORANGE)
    screen.blit(op_text, (610, 70))
    
    # Représentation de la liste
    y_offset = 110
    code_text = font.render("snake_body = [", True, BLUE)
    screen.blit(code_text, (610, y_offset))
    y_offset += 25
    
    # On affiche les éléments de la liste
    for i, segment in enumerate(snake_list):
        # Colorer l'index 0 (la tête) pour montrer où se fait l'insertion
        color = RED if i == 0 else BLACK
        comment = " # TÊTE (insert(0))" if i == 0 else ""
        if i == len(snake_list) - 1:
            comment = " # QUEUE (pop())"
            
        text = f"  ({segment[0]:02d}, {segment[1]:02d}),{comment}"
        rendered_text = font.render(text, True, color)
        screen.blit(rendered_text, (610, y_offset))
        y_offset += 20
        
        if y_offset > SCREEN_HEIGHT - 40:
            more_text = font.render("  ... ]", True, BLUE)
            screen.blit(more_text, (610, y_offset))
            return

    end_bracket = font.render("]", True, BLUE)
    screen.blit(end_bracket, (610, y_offset))

def game_loop():
    """Boucle principale du jeu."""
    # Position initiale du serpent (milieu de la grille)
    # C'est une LISTE de tuples (x, y)
    snake_list = logique.creer_serpent()
    direction = (0, -1) # Vers le haut
    
    # Nourriture
    food_pos = (15, 10)
    
    score = 0
    last_op = "Initialisation"
    running = True
    game_over = False
    
    print("Starting game loop")
    while running:
        # Gestion des événements (clavier, fermeture)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quit event received")
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_r:
                        game_loop() # Redémarrer
                        return
                    elif event.key == pygame.K_q:
                        print("Q pressed")
                        running = False
                else:
                    if event.key == pygame.K_LEFT and direction != (1, 0):
                        direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                        direction = (1, 0)
                    elif event.key == pygame.K_UP and direction != (0, 1):
                        direction = (0, -1)
                    elif event.key == pygame.K_DOWN and direction != (0, -1):
                        direction = (0, 1)

        if not game_over:
            # --- LOGIQUE DE LISTE (VIA MODULE ÉLÈVE) ---
            
            # 1. Calculer la nouvelle tête
            # Note: On passe la liste entière maintenant
            new_head = logique.calculer_nouvelle_tete(snake_list, direction)
            
            # 2. Insérer la nouvelle tête au début de la liste
            logique.inserer_tete(snake_list, new_head)
            last_op = "insert(0, head)"
            
            # 3. Vérification des collisions
            # Note: On vérifie APRES insertion, car la tête est maintenant dans la liste (index 0)
            if logique.verifier_collision(snake_list, GRID_WIDTH, GRID_HEIGHT):
                game_over = True
                last_op = "Collision!"
                # On pourrait retirer la tête pour l'affichage "mort" mais on laisse pour voir l'erreur
                continue

            # 4. Gérer la nourriture et la queue
            if new_head == food_pos:
                score += 1
                last_op += " + Miam!"
                # Nouvelle nourriture aléatoire
                while True:
                    food_pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
                    if food_pos not in snake_list:
                        break
            else:
                # Si on ne mange pas, on retire le dernier élément
                logique.supprimer_queue(snake_list)
                last_op += " + pop()"

        # --- DESSIN ---
        screen.fill(BLACK) 
        pygame.draw.rect(screen, BLACK, (0, 0, 600, SCREEN_HEIGHT))
        
        draw_grid()
        draw_snake(snake_list)
        draw_food(food_pos)
        draw_ui(snake_list, score, last_op)
        
        if game_over:
            overlay = pygame.Surface((600, SCREEN_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill(BLACK)
            screen.blit(overlay, (0, 0))
            
            msg = large_font.render("GAME OVER", True, RED)
            screen.blit(msg, (200, 250))
            restart_msg = font.render("Appuyez sur R pour recommencer", True, WHITE)
            screen.blit(restart_msg, (180, 300))
        
        pygame.display.flip()
        clock.tick(5) # Vitesse du jeu (5 images par seconde pour bien voir les mouvements)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()
