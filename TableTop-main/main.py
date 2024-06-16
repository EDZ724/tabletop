from pyray import *
import sys
import numpy as np
from scripts.mathe import Mathe
from scripts.models import Models
import os

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

CUBE_SIZE = 1.0
MAP_WIDTH = 30
MAP_HEIGHT = 15

player_num = 1

objects_models = []
objects_path = 'objetos/objeto_'

map = Mathe.new_matrix(MAP_HEIGHT, MAP_WIDTH, '0:0:0:0')

map[Mathe.getting_num(2, 1, MAP_WIDTH)] = '1:1:1:1'

players = [[], [], [], [], [], [], [], [], []]


if __name__ == '__main__':

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'TableTop')

    #Carregando os modelos
    qtd_models = 0
    while(Models.verifying_models(qtd_models, objects_path)):
        objects_models = Models.load_models(objects_models, qtd_models, objects_path)
        qtd_models += 1
    
    #Carregando os modelos dos personagens
    qtd_players = 0
    while qtd_players < 9:
        qtd_player_models = 0
        
        while(Models.verifying_models(qtd_player_models, f'player_{qtd_players + 1}/skin_')):
            players[qtd_players] = Models.load_models(players[qtd_players], qtd_player_models, f'player_{qtd_players + 1}/skin_')
            qtd_player_models += 1

        qtd_players += 1



    while not window_should_close():

        begin_drawing()

        clear_background(RAYWHITE)

        i = 0
        while(i < MAP_WIDTH * MAP_HEIGHT):

            (row, col) = Mathe.getting_row_col(i, MAP_WIDTH)
            if map[i] == '0:0:0:0':
                draw_rectangle(col * 20, row * 20, 20, 20, RED)
            else:
                draw_rectangle(col * 20, row * 20, 20, 20, GREEN)

            i += 1

        draw_fps(700, 400)
        end_drawing()

    #Unloads
    for model in objects_models:
        unload_model(model)

    close_window()

    