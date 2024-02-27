import turtle, random 

def validate_TileInput (RANGE_MIN, RANGE_MAX):
    while True:
        try:
            input_value = input("Please choose between {} and {} ... >".format(RANGE_MIN, RANGE_MAX))
            value = int(input_value)
            if RANGE_MIN <= value <= RANGE_MAX:
                return value                         
            else:
                print(f'INVALID value: {value}! Please choose within range from ({RANGE_MIN} to {RANGE_MAX} only!)')
        except ValueError:
            print(f'Unrecognized input {input_value}! Please input an integer from ({RANGE_MIN} to {RANGE_MAX} only!)')
    
    
# 1. INPUT PROMPT and VALIDATE number of tiles
    
INPUT_MIN = 2
INPUT_MAX = 5
print("Tell me how many tiles you want for this game?")
tiles = validate_TileInput(INPUT_MIN, INPUT_MAX)
print("Test: Valid tile input is ",tiles)
tilesArr = tiles -1

# 2. DEFINE class for DRAWING number of tiles according to user input
_thick_PENSIZE = 10
_thin_PENSIZE = 6
_BGCOLOR ="gold"
_GAMETEXTFONT = "Arial"
colorTile = "white"
colorMy ="blue"
colorUser = "purple"
colorResult ="black"
_SCREEN_HEIGHT = 300
_SCREEN_WIDTH = 600
_TILESIDES = 4
_TILEANGLE = 360/_TILESIDES
_TILESIZE = 50
_TILE_OFFSET = 30
_TILE_ADJ = _TILE_OFFSET/2
_DIALOGUE_YOFFSET = _TILESIZE + _TILE_OFFSET
x_start = ((_TILESIZE +_TILE_OFFSET)*tiles/2)
y_start = ((_TILESIZE+_TILE_OFFSET) / 2)
_RESULT_YOFFSET = y_start + _TILE_OFFSET + _TILE_ADJ
_RESULT_XOFFSET = -x_start

class CubeDrawer:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.bgcolor(_BGCOLOR)
        self.window.setup(_SCREEN_WIDTH, _SCREEN_HEIGHT,0,0)
        self.t = turtle.Turtle()
    
    def drawFillPolygon(self, draw_color, x, y):
        self.t.pensize(_thick_PENSIZE)
        self.t.color(draw_color)
        self.t.penup()
        self.t.goto(x,y)
        self.t.pendown()
        self.t.begin_fill()
        for i in range(_TILESIDES):
            self.t.forward(_TILESIZE)
            self.t.right(_TILEANGLE)
        self.t.end_fill()
        self.t.penup()
        self.t.hideturtle()

    def drawPolygon(self, drawSides, adj, draw_color, x, y):
        self.t.pensize(_thin_PENSIZE)
        self.t.penup()
        self.t.goto(x+adj,y-adj)
        self.t.pendown()
        self.t.color(draw_color)
        drawAngle = 360/drawSides
        for i in range(drawSides):
            self.t.forward(_TILESIZE-2*adj)
            self.t.right(drawAngle)
        self.t.penup()
        self.t.hideturtle()

    def write_text(self, draw_color, text, fontstyle, x, y):
        self.t.penup()
        self.t.color(draw_color)
        self.t.goto(x,y)
        self.t.pendown()
        self.t.write(text, align = "left", font = fontstyle)
        self.t.penup()
        self.t.hideturtle()
    
    def close(self):
        self.window.bye()


# 3 DRAW and SAVE x-y position of each tile drawn
game_tilelist={}

t = CubeDrawer()
tx= -x_start
ty= y_start
print(f"Test: < { x_start } -{ y_start} >")
for i in range(tiles):
    #save x-y pos
    xname = "x" + str(i)
    yname = "y" + str(i)
    game_tilelist[xname] = tx
    game_tilelist[yname] = ty
    #drawFillPolygon
    t.drawFillPolygon(colorTile, tx, ty)
    cubeFontStyle=("Arial", 11, "normal")
    cubeText = "Tile: (" + str(i+1) + ")"
    t.write_text(colorResult, cubeText, cubeFontStyle , tx, ty + _TILE_ADJ)
    tx = tx+ _TILESIZE + _TILE_OFFSET

print("Test:>>", game_tilelist)


#4 Ask user to CHOOSE a tile
print("Guess which tile I chose ... ?")
userChoice = validate_TileInput(1, tiles)
print("Test: User choice tile input is ",userChoice)
userArrChoice = userChoice -1

xname = "x" + str(userArrChoice)
yname = "y" + str(userArrChoice)
tx=game_tilelist[xname]
ty=game_tilelist[yname]
t.drawPolygon(_TILESIDES,0, colorUser, tx, ty)
ty -= _DIALOGUE_YOFFSET
userFontStyle=(_GAMETEXTFONT, 10, "normal")
t.write_text(colorUser, '(Your guess)', userFontStyle , tx, ty)


# 5. RANDOM PICK one tile
myNumber = random.randint(1,tiles)
print(f"I chose tile no: {myNumber}")
myArrNumber = myNumber - 1

xname = "x" + str(myArrNumber)
yname = "y" + str(myArrNumber)
tx=game_tilelist[xname]
ty=game_tilelist[yname]
t.drawPolygon(_TILESIDES, _TILE_ADJ, colorMy, tx, ty)
ty -= _DIALOGUE_YOFFSET + _TILE_OFFSET
myFontStyle=(_GAMETEXTFONT, 10, "normal")
t.write_text(colorMy, '(My Choice)', myFontStyle , tx, ty)


# 6. DISPLAY Game Result
if userChoice == myNumber:
    result = 'Yeah! You WIN!'
else:
    result = 'Sorry, you LOSE!'
print(result)

resultFontStyle=(_GAMETEXTFONT, 25, "bold italic")
t.write_text(colorResult, result, resultFontStyle , _RESULT_XOFFSET, _RESULT_YOFFSET)

input_value = input(print("Thank YOU and goodbye ..."))
