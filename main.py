import pygame
pygame.init()
display_width=1280
display_height=650
gameDisplay=pygame.display.set_mode((display_width,display_height))

#setting color values
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
light_red=(226,110,110)

#loading images
boatImg=pygame.image.load('images/boat.png')
bgImg=pygame.image.load('images/bg1.png')
mImg=pygame.image.load('images/missionary.png')
cImg=pygame.image.load('images/cannibal.png')
c1Img=pygame.image.load('images/cannibal1.png')
m1Img=pygame.image.load('images/missionary1.png')
ngImg=pygame.image.load('images/newgame.png')
ng1Img=pygame.image.load('images/newgame1.png')
gameoverImg=pygame.image.load('images/gameover.png')
wonImg=pygame.image.load('images/winner.png')
goImg=pygame.image.load('images/go.png')
go1Img=pygame.image.load('images/go1.png')
soundonImg=pygame.image.load('images/soundon.png')
soundoffImg=pygame.image.load('images/soundoff.png')
gameoversd = pygame.mixer.Sound('music/gameover.wav')
wonsd = pygame.mixer.Sound('music/won.wav')

#functions for loading images
def boat(x,y):
    gameDisplay.blit(boatImg,(x,y))

def missionary(x,y):
    gameDisplay.blit(mImg, (x, y))

def cannibal(x,y):
    gameDisplay.blit(cImg, (x, y))

def cannibal1(x,y):
    gameDisplay.blit(c1Img, (x, y))

def missionary1(x,y):
    gameDisplay.blit(m1Img, (x, y))

#setting default font
font=pygame.font.SysFont(None,25)

def main():
    x = (display_width * 0.1)
    y = (display_height * 0.8)
    x_change, y_change = 0, 0

    #coordinate of missionaries and cannibals at new game
    mc_x = [x - 135, x - 90, x - 45, x - 135, x - 90, x - 45]  # C1,c2, c3, m1, m2, m3
    mc_y = [y - 100, y - 100, y - 100, y - 250, y - 250, y - 250]
    mc_x_default = list(mc_x)
    mc_y_default = list(mc_y)

    mc_xchange = [0] * 6 #initialized displacements of missionaries and cannibas to 0. used later for movement
    pos = [0] * 6
    #pos indicate position of M and C;
    #  0 and 1 indicates left and right shore respectively
    # 2 and 4 indicates left an right of boat at left shore
    # 3 and 5 indicates left an right of boat at right shore

    pygame.display.set_caption('Missionaries and cannibals')
    clock = pygame.time.Clock()
    crashed = False
    boat_position = 0 #indicates boat at left shore
    a, b = 0, 0
    action = [a, b] #indicates no of missionaries and cannibals to move
    m, c, bt = 3, 3, 1 #indicates 3 missionaries, 3 canibals and boat at left shore
    state = [m, c, bt] #indicates state of missionaries, cannibals and boat at left shore

    gameover = False
    gameoverplayed,wonplayed=False,False
    left,right=False,False
    won=False
    moves=0 #for counting the no of moves

    #loading the background music
    pygame.mixer.music.load('music/bgmusic.mp3')
    pygame.mixer.music.play(-1) #play the bg music infinite times
    sound=True
    while not crashed:
        #loading bgimage and new game image
        gameDisplay.blit(bgImg, (0, 0))
        gameDisplay.blit(ngImg, (1000, 45))

        if sound:
            gameDisplay.blit(soundonImg, (1150, 40))
        else:
            gameDisplay.blit(soundoffImg, (1150, 40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        #loading the missionaries and cannibals image
        missionary(mc_x[0], mc_y[0])
        missionary(mc_x[1], mc_y[1])
        missionary(mc_x[2], mc_y[2])
        cannibal(mc_x[3], mc_y[3])
        cannibal(mc_x[4], mc_y[4])
        cannibal(mc_x[5], mc_y[5])

        #displaying states, actions, moves
        state_text = font.render("State: " + str(state), True, black)
        gameDisplay.blit(state_text, [20, 20])
        action_text = font.render("Action: " + str(action), True, black)
        gameDisplay.blit(action_text, [20, 50])
        moves_text = font.render("No. of moves: " + str(moves), True, black)
        gameDisplay.blit(moves_text, [20, 80])

        cur = pygame.mouse.get_pos() #getting cursor position

        #click and point actions of sound button
        if 1150 + 50 > cur[0] > 1150 and 40 + 50 > cur[1] > 40:
            if sound:
                gameDisplay.blit(soundoffImg, (1150, 40))
            else:
                gameDisplay.blit(soundonImg, (1150, 40))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if sound:
                    sound=False
                    pygame.mixer.music.pause()
                else:
                    sound=True
                    pygame.mixer.music.play()

        #click and point actions of new game button
        if 1000 + 119 > cur[0] > 1000 and 45 + 36 > cur[1] > 45:
            gameDisplay.blit(ng1Img, (1000, 20))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                main()
        boat(x, y)  #display boat

        #checking gameover
        if (state[0] < state[1] and state[0]>0 )or  (state[0] > state[1] and state[0] < 3 ):
            gameDisplay.blit(gameoverImg, (400, 250))
            gameover = True

        #checking game won
        if state==[0,0,0] and action==[0,0]:
            gameDisplay.blit(wonImg, (400, 250))
            won=True

        if not gameover and not won:
            # click and point actions of go button
            if 590+88 > cur[0] > 590 and 300 + 90 > cur[1] > 300 and action != [0, 0]:
                gameDisplay.blit(go1Img, (590, 300))
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    if boat_position == 0:
                        x_change = 10
                        for i in range(6):
                            if pos[i] == 2 or pos[i] == 4: mc_xchange[i] = 10
                    else:
                        x_change = -10
                        for i in range(6):
                            if pos[i] == 3 or pos[i] == 5: mc_xchange[i] = -10
            else:
                gameDisplay.blit(goImg, (590, 300))

            #stopping condition of boat
            if x >= 620 and boat_position == 0:
                x_change = 0
                mc_xchange = [0] * 6
                boat_position = 1
                moves+=1
                state[0], state[1], state[2] = state[0] - action[0], state[1] - action[1], 0
                for i in range(6):
                    if pos[i] == 2: pos[i] = 3
                    if pos[i] == 4: pos[i] = 5
            if x <= 128 and boat_position == 1:
                x_change = 0
                mc_xchange = [0] * 6
                boat_position = 0
                moves+=1
                state[0], state[1], state[2] = state[0] + action[0], state[1] + action[1], 1
                for i in range(6):
                    if pos[i] == 3: pos[i] = 2
                    if pos[i] == 5: pos[i] = 4

            # if boat is not full
            if action != [1, 1] and action != [0, 2] and action != [2, 0]:
                # click and point actions of missionary 1 at left shore
                if 45 > cur[0] > 5 and 420 + 100 > cur[1] > 420 and pos[0] == 0 and boat_position == 0:  # pos over missionary 1 left
                    missionary1(mc_x[0], mc_y[0])
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        a += 1
                        if action == [0, 1] or action == [1, 0]:
                            print (pos)
                            print(left, right)
                            for i in range(6):
                                if pos[i]==2:
                                    left=True
                                if pos[i]==4:
                                    right=True
                            print(left,right)
                            if left:
                                mc_x[0], mc_y[0] = x + 180, y - 50
                                pos[0] = 4
                            elif right:
                                mc_x[0], mc_y[0] = x + 20, y - 50
                                pos[0] = 2
                        else:
                            mc_x[0], mc_y[0] = x + 20, y - 50
                            pos[0] = 2

                # click and point actions of missionary 1 at right shore
                if 905 + 40 > cur[0] > 905 and 420 + 100 > cur[1] > 420 and pos[0] == 1 and boat_position == 1:
                    missionary1(mc_x[0], mc_y[0])
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        a += 1
                        if action == [0, 1] or action == [1, 0]:
                            for i in range(6):
                                if pos[i] == 3:
                                    left = True
                                if pos[i] == 5:
                                    right = True
                            if left:
                                mc_x[0], mc_y[0] = x + 180, y - 50
                                pos[0] = 5
                            elif right:
                                mc_x[0], mc_y[0] = x + 20, y - 50
                                pos[0] = 3
                        else:
                            mc_x[0], mc_y[0] = x + 20, y - 50
                            pos[0] = 3
                # click and point actions of missionary 2 at left shore
                if 50 + 40 > cur[0] > 50 and 420 + 100 > cur[1] > 420 and pos[1] == 0 and boat_position == 0:
                    missionary1(mc_x[1], mc_y[1])
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        a += 1
                        if action == [0, 1] or action == [1, 0]:
                            for i in range(6):
                                if pos[i]==2:
                                    left=True
                                if pos[i]==4:
                                    right=True
                            if left:
                                mc_x[1], mc_y[1] = x + 180, y - 50
                                pos[1] = 4
                            elif right:
                                mc_x[1], mc_y[1] = x + 20, y - 50
                                pos[1] = 2
                        else:
                            mc_x[1], mc_y[1] = x + 20, y - 50
                            pos[1] = 2

                # click and point actions of missionary 2 at right shore
                if 950 + 40 > cur[0] > 950 and 420 + 100 > cur[1] > 420 and pos[1] == 1 and boat_position == 1:
                    missionary1(mc_x[1], mc_y[1])
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        a += 1
                        if action == [0, 1] or action == [1, 0]:
                            for i in range(6):
                                if pos[i] == 3:
                                    left = True
                                if pos[i] == 5:
                                    right = True
                            if left:
                                mc_x[1], mc_y[1] = x + 180, y - 50
                                pos[1] = 5
                            elif right:
                                mc_x[1], mc_y[1] = x + 20, y - 50
                                pos[1] = 3
                        else:
                            mc_x[1], mc_y[1] = x + 20, y - 50
                            pos[1] = 3

                # click and point actions of missionary 3 at left shore
                if 100 + 40 > cur[0] > 100 and 420 + 100 > cur[1] > 420 and pos[2] == 0 and boat_position == 0:
                    missionary1(mc_x[2], mc_y[2])
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        a += 1
                        if action == [0, 1] or action == [1, 0]:
                            for i in range(6):
                                if pos[i]==2:
                                    left=True
                                if pos[i]==4:
                                    right=True
                            if left:
                                mc_x[2], mc_y[2] = x + 180, y - 50
                                pos[2] = 4
                            elif right:
                                mc_x[2], mc_y[2] = x + 20, y - 50
                                pos[2] = 2
                        else:
                            mc_x[2], mc_y[2] = x + 20, y - 50
                            pos[2] = 2

                # click and point actions of missionary 3 at right shore
                if 1000 + 40 > cur[0] > 1000 and 420 + 100 > cur[1] > 420 and pos[2] == 1 and boat_position == 1:
                    missionary1(mc_x[2], mc_y[2])
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        a += 1
                        if action == [0, 1] or action == [1, 0]:
                            for i in range(6):
                                if pos[i] == 3:
                                    left = True
                                if pos[i] == 5:
                                    right = True
                            if left:
                                mc_x[2], mc_y[2] = x + 180, y - 50
                                pos[2] = 5
                            elif right:
                                mc_x[2], mc_y[2] = x + 20, y - 50
                                pos[2] = 3
                        else:
                            mc_x[2], mc_y[2] = x + 20, y - 50
                            pos[2] = 3

                # click and point actions of cannibal 1 at left shore
                if 45 > cur[0] > 5 and 275 + 100 > cur[1] > 275 and pos[3] == 0 and boat_position == 0:
                    cannibal1(mc_x[3], mc_y[3])
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        b += 1
                        if action == [0, 1] or action == [1, 0]:
                            for i in range(6):
                                if pos[i]==2:
                                    left=True
                                if pos[i]==4:
                                    right=True
                            if left:
                                mc_x[3], mc_y[3] = x + 180, y - 50
                                pos[3] = 4
                            elif right:
                                mc_x[3], mc_y[3] = x + 20, y - 50
                                pos[3] = 2

                        else:
                            mc_x[3], mc_y[3] = x + 20, y - 50
                            pos[3] = 2

                # click and point actions of cannibal 1 at right shore
                if 905 + 40 > cur[0] > 905 and 275 + 100 > cur[1] > 275 and pos[3] == 1 and boat_position == 1:
                    cannibal1(mc_x[3], mc_y[3])
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        b += 1
                        if action == [0, 1] or action == [1, 0]:
                            for i in range(6):
                                if pos[i] == 3:
                                    left = True
                                if pos[i] == 5:
                                    right = True
                            if left:
                                mc_x[3], mc_y[3] = x + 180, y - 50
                                pos[3] = 5
                            elif right:
                                mc_x[3], mc_y[3] = x + 20, y - 50
                                pos[3] = 3

                        else:
                            mc_x[3], mc_y[3] = x + 20, y - 50
                            pos[3] = 3

                # click and point actions of cannibal2 at left shore
                if 50 + 40 > cur[0] > 50 and 275 + 100 > cur[1] > 275 and pos[
                    4] == 0 and boat_position == 0:
                    cannibal1(mc_x[4], mc_y[4])
                    if pygame.mouse.get_pressed() == (1, 0, 0):

                        b += 1
                        if action == [0, 1] or action == [1, 0]:
                            for i in range(6):
                                if pos[i]==2:
                                    left=True
                                if pos[i]==4:
                                    right=True
                            if left:
                                mc_x[4], mc_y[4] = x + 180, y - 50
                                pos[4] = 4
                            elif right:
                                mc_x[4], mc_y[4] = x + 20, y - 50
                                pos[4] = 2
                        else:
                            mc_x[4], mc_y[4] = x + 20, y - 50
                            pos[4] = 2

                # click and point actions of cannibal 2 at right shore
                if 950 + 40 > cur[0] > 950 and 275 + 100 > cur[1] > 275 and pos[
                    4] == 1 and boat_position == 1:
                    cannibal1(mc_x[4], mc_y[4])
                    if pygame.mouse.get_pressed() == (1, 0, 0):

                        b += 1
                        if action == [0, 1] or action == [1, 0]:
                            for i in range(6):
                                if pos[i] == 3:
                                    left = True
                                if pos[i] == 5:
                                    right = True
                            if left:
                                mc_x[4], mc_y[4] = x + 180, y - 50
                                pos[4] = 5
                            elif right:
                                mc_x[4], mc_y[4] = x + 20, y - 50
                                pos[4] = 3
                        else:
                            mc_x[4], mc_y[4] = x + 20, y - 50
                            pos[4] = 3

                # click and point actions of cannibal 3 at left shore
                if 100 + 40 > cur[0] > 100 and 275 + 100 > cur[1] > 275 and pos[
                    5] == 0 and boat_position == 0:
                    cannibal1(mc_x[5], mc_y[5])
                    if pygame.mouse.get_pressed() == (1, 0, 0):

                        b += 1
                        if action == [0, 1] or action == [1, 0]:
                            for i in range(6):
                                if pos[i]==2:
                                    left=True
                                if pos[i]==4:
                                    right=True
                            if left:
                                mc_x[5], mc_y[5] = x + 180, y - 50
                                pos[5] = 4
                            elif right:
                                mc_x[5], mc_y[5] = x + 20, y - 50
                                pos[5] = 2
                        else:
                            mc_x[5], mc_y[5] = x + 20, y - 50
                            pos[5] = 2

                # click and point actions of cannibal 3 at right shore
                if 1000 + 40 > cur[0] > 1000 and 275 + 100 > cur[1] > 275 and pos[
                    5] == 1 and boat_position == 1:
                    cannibal1(mc_x[5], mc_y[5])
                    if pygame.mouse.get_pressed() == (1, 0, 0):

                        b += 1
                        if action == [0, 1] or action == [1, 0]:
                            for i in range(6):
                                if pos[i]==3:
                                    left=True
                                if pos[i]==5:
                                    right=True
                            if left:
                                mc_x[5], mc_y[5] = x + 180, y - 50
                                pos[5] = 5
                            elif right:
                                mc_x[5], mc_y[5] = x + 20, y - 50
                                pos[5] = 3
                        else:
                            mc_x[5], mc_y[5] = x + 20, y - 50
                            pos[5] = 3

            # if any 1 or more person on boat
            if action != [0, 0]:

                # click and point actions of missionary or cannibal at boat position 2
                if 157 + 40 > cur[0] > 157 and 478 + 100 > cur[1] > 478:
                    k = 7
                    for i in range(6):
                        if pos[i] == 2:
                            k = i
                    if k != 7:
                        if k - 3 < 0:
                            missionary1(x + 20, y - 50)
                        else:
                            cannibal1(x + 20, y - 50)
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                            if k - 3 < 0:
                                a -= 1
                            else:
                                b -= 1
                            mc_x[k], mc_y[k] = mc_x_default[k], mc_y_default[k]
                            pos[k] = 0
                            left=False

                # click and point actions of missionary or cannibal at boat position 3
                if 656 + 40 > cur[0] > 656 and 478 + 100 > cur[1] > 478:
                    k = 7
                    for i in range(6):
                        if pos[i] == 3:
                            k = i
                    if k != 7:
                        if k - 3 < 0:
                            missionary1(x + 20, y - 50)
                        else:
                            cannibal1(x + 20, y - 50)
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                            if k - 3 < 0:
                                a -= 1
                            else:
                                b -= 1
                            mc_x[k], mc_y[k] = 900 + mc_x_default[k], mc_y_default[k]
                            pos[k] = 1
                            left=False

                # click and point actions of missionary or cannibal at boat position 4
                if 318 + 40 > cur[0] > 318 and 478 + 100 > cur[1] > 478:
                    k = 7
                    for i in range(6):
                        if pos[i] == 4:
                            k = i
                    if k != 7:
                        if k - 3 < 0:
                            missionary1(x + 180, y - 50)
                        else:
                            cannibal1(x + 180, y - 50)
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                            if k - 3 < 0:
                                a -= 1
                            else:
                                b -= 1
                            mc_x[k], mc_y[k] = mc_x_default[k], mc_y_default[k]
                            pos[k] = 0
                            right=False

                # click and point actions of missionary or cannibal at boat position 5
                if 817 + 40 > cur[0] > 817 and 478 + 100 > cur[1] > 478:
                    k = 7
                    for i in range(6):
                        if pos[i] == 5:
                            k = i
                    if k != 7:
                        if k - 3 < 0:
                            missionary1(x + 180, y - 50)
                        else:
                            cannibal1(x + 180, y - 50)
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                            if k - 3 < 0:
                                a -= 1
                            else:
                                b -= 1
                            mc_x[k], mc_y[k] = 900 + mc_x_default[k], mc_y_default[k]
                            pos[k] = 1
                            right=False

            #update boat position for movement
            x = x + x_change

            #update missionary and cannibal position for movement
            for i in range(6):
                mc_x[i] += mc_xchange[i]
            action = [a, b]

        #actions for gameover
        elif gameover and not gameoverplayed:
            pygame.mixer.music.stop()
            gameoversd.play(0)
            gameoverplayed=True

        #actions for game won
        elif won and not wonplayed:
            pygame.mixer.music.stop()
            wonsd.play(0)
            wonplayed = True

        pygame.display.update()
        clock.tick(25)

    pygame.quit()
    quit()

if __name__=="__main__":
    main()