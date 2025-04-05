import pygame
import sys
import os

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500, 500))
font = pygame.font.Font(None, 50) 

songs = [
    {
        "name": "Shabyt kelse",
        "path": "/Users/Admin/Desktop/Lab7/task2/1.mp3"
    },
    {
        "name": "Losing Interest",
        "path": "/Users/Admin/Desktop/Lab7/task2/2.mp3"
    },
    {
        "name": "Another Love",
        "path": "/Users/Admin/Desktop/Lab7/task2/3.mp3"
    }
]

curr_index = 0

def play(index):
    pygame.mixer.music.load(songs[index]["path"])
    pygame.mixer.music.play()
    print(f"Playing: {songs[index]['name']}")

def stop():
    pygame.mixer.music.stop()
    print("Music Stopped")

def next():
    global curr_index
    curr_index = (curr_index + 1) % len(songs)
    play(curr_index)

def prev():
    global curr_index
    curr_index = (curr_index - 1) % len(songs)
    play(curr_index)

print("UP: Play \nDOWN: Stop \nRIGHT: Next \nLEFT: Prev")
running = True
while running:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                play(curr_index)
            elif event.key == pygame.K_DOWN:
                stop()
            elif event.key == pygame.K_RIGHT:
                next()
            elif event.key == pygame.K_LEFT:
                prev()

    screen.fill((255, 255, 255))
    current_text = font.render(songs[curr_index]["name"],True, (0, 0, 0))
    screen.blit(current_text, (20, 60))
    pygame.display.flip()

pygame.quit()
sys.exit()
