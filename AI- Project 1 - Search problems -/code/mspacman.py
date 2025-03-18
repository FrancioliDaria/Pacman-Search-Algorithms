def drawPacman(self, pacman, index):
        position = self.getPosition(pacman)
        screen_point = self.to_screen(position)
        print(screen_point)
        endpoints = self.getEndpoints(self.getDirection(pacman))
        (screen_x, screen_y) = (self.to_screen(position))
        dir = self.getDirection(pacman) #directia pacman

        width = PACMAN_OUTLINE_WIDTH
        outlineColor = PACMAN_COLOR
        fillColor = PACMAN_COLOR

        BLUE = formatColor(0.0, 0.0, 1.0) #culoarea ochilor
        PURPLE = formatColor(1.0, 0.0, 1.0) #culoarea funditei
        BLACK = formatColor(0.0, 0.0, 0.0) #culoarea pupilei si a genelor
        WHITE = formatColor(1.0, 1.0, 1.0)

        dx = 0
        dy = 0
        if dir == 'North':
            dy = -0.2
        if dir == 'South':
            dy = 0.2
        if dir == 'East':
            dx = 0.2
        if dir == 'West':
            dx = -0.2

        bow_point = (screen_point[0] - self.gridSize / 4, screen_point[1] - self.gridSize / 4) #punctul funditei
        bpts = [bow_point]
        X1 = 10 #cat de in stanga e funda
        X2 = 20 #cat de in dreapta e funda ////X=latime
        Y1 = 20
        Y2 = 0 #cat de groasa e //// Y=inaltime
        bpts.append((bow_point[0] - X1, bow_point[1] + Y1))
        bpts.append((bow_point[0] + X2, bow_point[1] - Y2))
        bpts.append((bow_point[0] - X2, bow_point[1] + Y2))
        bpts.append((bow_point[0] + X1, bow_point[1] - Y1))

        return [circle(screen_point, PACMAN_SCALE * self.gridSize,
                       fillColor=fillColor, outlineColor=outlineColor,
                       endpoints=endpoints,
                       width=width),
                circle((screen_x + self.gridSize * PACMAN_SCALE * (-0.5 + dx / 1.0),
                        screen_y - self.gridSize * PACMAN_SCALE * (0.5 - dy / 1.0)), self.gridSize * PACMAN_SCALE * 0.2,
                       BLUE, BLUE),
                circle((screen_x + self.gridSize * PACMAN_SCALE * (-0.5 + dx),
                        screen_y - self.gridSize * PACMAN_SCALE * (0.5 - dy)),
                       self.gridSize * PACMAN_SCALE * 0.10, BLACK, WHITE),
                polygon(bpts, WHITE, [PURPLE])] ##Exterior, Interior funda