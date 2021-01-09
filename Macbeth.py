import simplegui, math, random, time

atan = math.atan
cos = math.cos
sin = math.sin

#Constants
WIDTH = 1280
HEIGHT = 720
GAME_TITLE = "MACBETH: THE GAME"
GAME_START_BUTTON_TEXT = "Play"
DIALOGUE_COLOR = "#ffffff99" #white with 99 opacity (base 16, opacity is last byte)
DIALOGUE_SPEED = 0.04
START_SCENE = 0

MACBETH_SPRITE = {
    "image": simplegui.load_image("https://www.threebow.com/i/7a2979456707.png"),
    "width": 256,
    "height": 256
}

MACBETH_KING_SPRITE = {
    "image": simplegui.load_image("https://www.threebow.com/i/6ac1ca494a08.png"),
    "width": 256,
    "height": 256
}

LADY_MACBETH_SPRITE = {
    "image": simplegui.load_image("https://www.threebow.com/i/263262a52716.png"),
    "width": 256,
    "height": 256
}

MACDUFF_SPRITE = {
    "image": simplegui.load_image("https://www.threebow.com/i/45c1f0be5f2a.png"),
    "width": 256,
    "height": 256
}

DUNCAN_SPRITE = {
    "image": simplegui.load_image("https://www.threebow.com/i/262b62546ac6.png"),
    "width": 128,
    "height": 128
}

WITCH_SPRITE = {
    "image": simplegui.load_image("https://www.threebow.com/i/60e28f55b823.png"),
    "width": 128,
    "height": 128
}

BANQUO_SPRITE = {
    "image": simplegui.load_image("https://www.threebow.com/i/8d131c69552f.png"),
    "width": 256,
    "height": 256
}

BANQUO_GHOST_SPRITE = {
    "image": simplegui.load_image("https://www.threebow.com/i/c44e667e9589.png"),
    "width": 256,
    "height": 256
}

DAGGER_BIG_SPRITE = {
    "image": simplegui.load_image("https://www.threebow.com/i/e1feb264b8d6.png"),
    "width": 144,
    "height": 144
}

CAULDRON_SPRITE = {
    "image": simplegui.load_image("https://www.threebow.com/i/991e3e01631a.png"),
    "width": 256,
    "height": 256
}

APPARITION_1_SPRITE = {
    "image": simplegui.load_image("https://www.threebow.com/i/0ffee08271af.png"),
    "width": 128,
    "height": 128
}

APPARITION_2_SPRITE = {
    "image": simplegui.load_image("https://www.threebow.com/i/863fa6a1a8e3.png"),
    "width": 128,
    "height": 128
}

APPARITION_3_SPRITE = {
    "image": simplegui.load_image("https://www.threebow.com/i/c3f273c0a4e0.png"),
    "width": 144,
    "height": 144
}

AXE_SPRITE = {
    "image": simplegui.load_image("https://www.threebow.com/i/c2fc7c8e6927.png"),
    "width": 64,
    "height": 64
}

PLOT = [
    { #Field with Banquo and the witches
        "dialogue": [
            ["???", "Fair is foul, and foul is fair, hover through the fog and filthy air."	],
            ["Witch 1", "All hail, Macbeth, hail to thee, thane of Glamis!"],
            ["Witch 2", "All hail, Macbeth, hail to thee, thane of Cawdor!"],
            ["Witch 3", "All hail, Macbeth, thou shalt be king hereafter!"],
            ["Macbeth", "Wait, what? How can that be possible?"],
            ["Macbeth", "I'm already the thane of Glamis, but the thane of Cawdor is still alive."],
            ["Macbeth", "And... How can I..."],
            ["Banquo", "What about me? What do you have to say for my future?"],
            ["Witch 3", "You will not be a king, however your descendants will be kings for many generations."],
            ["Witches", "All hail..."]
        ],
        "positions": {
            0: {
                "macbeth": [WIDTH*0.2, HEIGHT*0.35, 0.00]
            },
            4: {
                "macbeth": [WIDTH*0.3, HEIGHT*0.35, 0.03]
            }
        },
        "background": {
            "image": simplegui.load_image("https://www.threebow.com/i/2094ae5c12d7.png"),
            "width": 1280,
            "height": 709
        },
        "sprites": [
            {
                "sprite": WITCH_SPRITE,
                "positions": {
                    0: [WIDTH*0.6, HEIGHT/2, 0.00],
                    9: [WIDTH*0.6, -256, 0.02]
                }
            },
            {
                "sprite": WITCH_SPRITE,
                "positions": {
                    0: [WIDTH*0.7, HEIGHT/2, 0.00],
                    9: [WIDTH*0.7, -256, 0.02]
                }
            },
            {
                "sprite": WITCH_SPRITE,
                "positions": {
                    0: [WIDTH*0.8, HEIGHT/2, 0.00],
                    9: [WIDTH*0.8, -256, 0.02]
                }
            },
            {
                "sprite": BANQUO_SPRITE,
                "positions": {
                    0: [WIDTH*0.32, HEIGHT*0.35, 0.00],
                    4: [WIDTH*0.42, HEIGHT*0.35, 0.03]
                }
            }
        ],
        "instantTransition": True
    },
    
    { #Pre-duncan-kill, talking with lady macbeth
        "dialogue": [
            ["Lady Macbeth", "I have received your letter. Your only choice is to kill Duncan!"],
            ["Macbeth", "The king has honored me, and treats us well. We cannot do this!"],
            ["Lady Macbeth", "Are you really going to just be a coward?"],
            ["Lady Macbeth", "If you don't do this, you are the farthest thing from a man."],
            ["Lady Macbeth", "He is coming over for dinner tonight, the perfect opportunity..."],
            ["Lady Macbeth", "I'll make sure the guards are drunk, and pin the crime on them."],
            ["Macbeth", "Let me decide, woman!"],
            ["Macbeth", "..."],
            ["Macbeth", "Okay."]
        ],
        "positions": {
            0: {
                "macbeth": [WIDTH*0.18, HEIGHT*0.57, 0.00]
            }
        },
        "background": {
            "image": simplegui.load_image("https://www.threebow.com/i/8fd2044ffce3.png"),
            "width": 1228,
            "height": 871
        },
        "sprites": [
            {
                "sprite": LADY_MACBETH_SPRITE,
                "positions": {
                    0: [WIDTH*0.3, HEIGHT*0.57, 0.00]
                }
            }
        ],
        "instantTransition": True
        #TODO: Implement Boss Fight (have the screen shaded red)
    },
    
    #Duncan Kill
    {
        "dialogue": [
            ["Duncan", "It's time for bed."],
            ["Macbeth", "No, it's time to die, old man..."],
            ["Duncan", "Who is there?! Is that you, Macbeth?"],
            ["Duncan", "Treason!! Treason!! Where are the royal guards?"],
            ["Macbeth", "It has been done. I better get back to Lady Macbeth."]
        ],
        
        "positions": {
            
            0: {
                "macbeth": [0, HEIGHT*0.60, 0.00]
            },
            
            2: {
                "macbeth": [WIDTH*0.60, HEIGHT*0.60, 0.003]
            },
            
            4: {
                "macbeth": [WIDTH*0.90, HEIGHT*0.60, 0.003]
            }
        },
        "background": {
            "image": simplegui.load_image("https://www.threebow.com/i/8fd2044ffce3.png"),
            "width": 1228,
            "height": 871
        },
        "sprites": [
            {
                "sprite": DUNCAN_SPRITE,
                "positions": {
                    0: [WIDTH*0.75, HEIGHT*0.75, 0.00, 0],
                    1: [WIDTH*0.8, HEIGHT*0.8, 0.02, 90],
                    2: [WIDTH*0.75, HEIGHT*0.75, 0.01, 0],
                    3: [WIDTH*0.90, HEIGHT*0.30, 0.08, -20],
                    4: [WIDTH*0.85, HEIGHT*0.8, 0.03, -90]
                }
            },
            {
                "sprite": DAGGER_BIG_SPRITE,
                "positions": {
                    0: [WIDTH*0.03, HEIGHT*0.60, 0.00],
                    2: [WIDTH*0.58+70, HEIGHT*0.60, 0.003,-10],
                    3: [WIDTH*0.90, HEIGHT*0.30, 0.08, 60],
                    4: [WIDTH*0.90, HEIGHT*0.85, 0.03, 20]
                }
            },
            {
                "sprite": DAGGER_BIG_SPRITE,
                "positions": {
                    0: [WIDTH*0.055, HEIGHT*0.60, 0.00],
                    2: [WIDTH*0.60+70, HEIGHT*0.60, 0.003,5],
                    3: [WIDTH*0.90, HEIGHT*0.25, 0.08, 40],
                    4: [WIDTH*0.75, HEIGHT*0.85, 0.03, -90]
                }
            }
        ],
        "instantTransition": True
        
    },
    
    
    { #Banquo's Death Talk
        "dialogue": [
            ["Macbeth", "M'lady... Duncan is dead, and I've issued Banquo's death."],
            ["Lady Macbeth", "What?! Why would you do that? Wasn't Banquo your best friend?"],
            ["Macbeth", "I was just scared that he would be the reason why I lose my crown."],
            ["Lady Macbeth", "That's insane. You really shouldn't have done such a thing."],
            ["Lady Macbeth", "This would look really bad on us if somebody found out we were behind this."],
            ["Macbeth", "I really wish I didn't act so quickly and recklessly. I hope that Banquo survives."]
        ],
        "positions": {
            0: {
                "macbeth": [WIDTH*0.32, HEIGHT*0.57, 0.00]
            }
        },
        "background": {
            #make image the one inside castle with candles
            "image": simplegui.load_image("https://www.threebow.com/i/e2dd7a19c39b.png"),
            "width": 473,
            "height": 224
        },
        "sprites": [
            {
                "sprite": LADY_MACBETH_SPRITE,
                "positions": {
                    0: [WIDTH*0.48, HEIGHT*0.57, 0.00]
                }
            }
        ],
        "instantTransition": True,
        "king": True
    },
    
    
    #Banquo dies scene
    {
        "dialogue": [
            ["Assassin","Let's get him!"],
            ["Banquo","Dear God, do not hurt me!"],
            
            #Daggers fly at Banquo, his health bar disappears, and he rotates and falls.
            ["Banquo", "..."],

            ["Banquo","GAHH!! Murder! Murder!"],
            ["Assassin","Wait! Where is his son?"],
        ],
        "positions": {
            0: {
                "macbeth": [0, 0, 0]
            }
        },
        "sprites": [
            {
                "sprite": BANQUO_SPRITE,
                "positions": {
                    0: [WIDTH/2-128, HEIGHT*0.6, 0.00],
                    3: [WIDTH/2, HEIGHT*0.7, 0.02, 90] #TODO: Rotate on death
                }
            },
            
            {
                "sprite": DAGGER_BIG_SPRITE,
                "positions": {
                    0: [30, HEIGHT*0.3, 0],
                    2: [WIDTH/2-128, HEIGHT*0.6, 0.03, 100],
                    3: [WIDTH/2, HEIGHT*0.71, 0.02, 135]
                }
            },
            {
                "sprite": DAGGER_BIG_SPRITE,
                "positions": {
                    0: [WIDTH-174, HEIGHT*0.45, 0],
                    2: [WIDTH/2, HEIGHT*0.67, 0.03, -85],
                    3: [WIDTH/2+50, HEIGHT*0.73, 0.02, -135]
                }
            }
        ],
        "background": {
            #make image the one dark road outside castle
            "image": simplegui.load_image("https://www.threebow.com/i/42982411d7d8.jpg"),
            "width": 748,
            "height": 421
        },
        "instantTransition": True,
        "hideMacbeth": True
    },
    
    #Macbeth goes to see apparations
    {
        "dialogue": [
            ["Witch 2", "By the pricking of my thumbs, something wicked this way comes."],
            ["Macbeth","Witches, tell me my future. I want to see them, now!"],
            ["Witches","Very well. You may see them. These apparations are very potent."],
            ["Apparition 1","Macbeth! Macbeth! Macbeth! beware Macduff."],
            ["Apparition 2","Nobody born from a woman shall harm Macbeth."],
            ["Apparition 3","You will be safe, until the trees Great Birnam move to Dunsinane hill."],
            ["Macbeth","God, what does that mean? Then am I immortal now?"],
            ["Macbeth","What about Banquo now. Shall his blood ever reign the kingdom now?"],
            ["Witch 1", "Why don't you take a look?"],
            ["Macbeth", "Banquo's descendants. What a horrible sight!"]
        ],
        "positions": {
            0: {
                "macbeth": [0, HEIGHT*0.35, 0]
            },
            1: {
                "macbeth": [WIDTH*0.12, HEIGHT*0.35, 0.03]
            }
        },
        "background": {
            "image": simplegui.load_image("https://www.threebow.com/i/43bd7796f410.png"),
            "width": 1679,
            "height": 944
        },
        "sprites": [
            {
                "sprite": WITCH_SPRITE,
                "positions": {
                    0: [WIDTH*0.6, HEIGHT/2, 0.00]
                }
            },
            {
                "sprite": WITCH_SPRITE,
                "positions": {
                    0: [WIDTH*0.7, HEIGHT/2, 0.00]
                }
            },
            {
                "sprite": WITCH_SPRITE,
                "positions": {
                    0: [WIDTH*0.8, HEIGHT/2, 0.00]
                }
            },
            {
                "sprite": CAULDRON_SPRITE,
                "positions": {
                    0: [WIDTH*0.3, HEIGHT*0.3, 0.00]
                }
            },
            {
                "sprite": APPARITION_1_SPRITE,
                "positions": {
                    0: -1,
                    3: [WIDTH*0.3+56, HEIGHT*0.27, 0.03],
                    4: -1
                }
            },
            {
                "sprite": APPARITION_2_SPRITE,
                "positions": {
                    0: -1,
                    4: [WIDTH*0.3+56, HEIGHT*0.27, 0.03],
                    5: -1
                }
            },
            {
                "sprite": APPARITION_3_SPRITE,
                "positions": {
                    0: -1,
                    5: [WIDTH*0.3+56, HEIGHT*0.27, 0.03],
                    6: -1
                }
            }
        ],
        "king": True,
        "instantTransition": True
    },
    
    #Plot death of Macduff. 
    {
        "dialogue": [
            ["Macbeth", "I'm planning on killing Macduff."],
            ["Lady Macbeth", "Why would you? Haven't you already killed enough royals already?"],
            ["Macbeth", "I'm already deep enough in the rabbit hole, I might as well go all the way through."],
            ["Lady Macbeth", "This reasoning is not very suitable for a king to use."],
            ["Macbeth", "I fear that Macduff will be the greatest threat to me."],
            ["Macbeth", "The witches have warned me about him"],
            ["Lady Macbeth", "Do you not feel guilty enough having already killed both the king and Banquo?"],
            ["Macbeth", "..."]
        ],
        "positions": {
            0: {
                "macbeth": [WIDTH*0.32, HEIGHT*0.57, 0.00]
            }
        },
        "background": {
            #make image the one inside castle with candles
            "image": simplegui.load_image("https://www.threebow.com/i/e2dd7a19c39b.png"),
            "width": 473,
            "height": 224
        },
        "sprites": [
            {
                "sprite": LADY_MACBETH_SPRITE,
                "positions": {
                    0: [WIDTH*0.48, HEIGHT*0.57, 0.00]
                }
            }
        ],
        "instantTransition": True,
        "king": True
    },
    
    #Macduff vows revenge on Macbeth
    {
        "dialogue": [
            ["Macduff","I cannot believe it. Macbeth has finally crossed the line."],
            ["Macduff","Not only has he killed me wife, but all of my beautiful kids as well. ALL OF THEM!!"],
            ["Macduff","I will have my vengeance."]
        ],
        "positions": {
            0: {
                "macbeth": [0, 0, 0]
            }
        },
        "background": {
            #Use image of Macduff's castle
            "image": simplegui.load_image("https://www.threebow.com/i/cff7c389cfbb.png"),
            "width": 1610,
            "height": 790
        },
        "sprites": [
            {
                "sprite": MACDUFF_SPRITE,
                "positions": {
                    0: [WIDTH/2-128, HEIGHT/2, 0]
                }
            }
        ],
        "instantTransition": True,
        "hideMacbeth": True
    },
    
    #Lady Macbeth death scene
    {
        "dialogue": [
            ["Lady Macbeth", "Out, damned spot! Out, I say!"],
            ["Lady Macbeth", "..."],
            ["Lady Macbeth", "YEEEEEEEEEEEEEEEEEEEEEEEEET"]
        ],
        "positions": {
            0: {
                "macbeth": [0, 0, 0]
            }
        },
        "background": {
            "image": simplegui.load_image("https://www.threebow.com/i/97e48f9615e7.jpg"),
            "width": 700,
            "height": 394
        },
        "sprites": [
            {
                "sprite": LADY_MACBETH_SPRITE,
                "positions": {
                    0: [WIDTH*0.05, HEIGHT*0.35, 0.00],
                    1: [WIDTH*0.33, HEIGHT*0.29, 0.0015],
                    2: [WIDTH+2000, -1000, 0.007, 500]
                }
            }
        ],
        "instantTransition": True,
        "hideMacbeth": True
    },
    
    #Macbeth vs Macduff
    {
        "dialogue": [
            ["Macduff", "Well look who it is? If it isn't the tyrant Macbeth. I will kill you."],
            ["Macbeth", "I bear a charmed life, which cannot be harmed by one born from a woman."],
            ["Macduff", "Haha. Well listen here kid, I'm a C-section baby."],
            ["Macduff", "Macduff was from his mother untimely ripped."],
            ["Macbeth", "Alright then. I don't really care, but I don't want to fight you."],
            ["Macduff", "You're dead, Macbeth."]
        ],
        "positions": {
            0: {
                "macbeth": [WIDTH*0.2, HEIGHT*0.55, 0]
            }
        },
        "sprites": [
            {
                "sprite": MACDUFF_SPRITE,
                "positions": {
                    0: [WIDTH*0.5, HEIGHT*0.6, 0]
                }
            }
        ],
        "background": {
            "image": simplegui.load_image("https://www.threebow.com/i/3b56cb6fa0b1.png"),
            "width": 1680,
            "height": 1050
        }
    }
    
]

    
for i in range(8, 0, -1):
    PLOT[5]["sprites"].append({
        "sprite": BANQUO_GHOST_SPRITE,
        "positions": {
            0: -1,
            9: [WIDTH*0.15+48*i, HEIGHT*0.45-12*i, 0.03]
        }
    })

DIALOGUE = True
CURRENT_DIALOGUE = 0
CURRENT_SCENE = 0
GAME_STARTED = False

TRANSITIONING = False
TRANSITION_PROGRESS = 0
TRANSITION_IN = False

#Runtime
startTime = time.time()
def curTime():
    return time.time() - startTime

#Oscillator
def osc():
    return (math.cos(curTime()*3)+1)/2
    
#Linear interpolation
def lerp(delta, fr, to):
    if(delta > 1):
        return to
    if(delta < 0):
        return fr
    return fr + (float(to) - float(fr)) * delta

#Helper function to draw a rect
def drawRect(canvas, x, y, w, h, color):
    canvas.draw_polygon([
        [x, y],
        [x + w, y],
        [x + w, y + h],
        [x, y + h],
    ], 1, color, color)

#Clamping a number
def clamp(n, n_min, n_max):
    return min(max(n, n_min), n_max)

#Dot product
def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]

#Class to help with managing inputs
class InputManager:
    keyMap = []
    
    def pressKey(self, key):
        self.keyMap.append(key)
        
    def releaseKey(self, key):
        if(key in self.keyMap): self.keyMap.remove(key)
        
    def keyDown(self, key):
        return simplegui.KEY_MAP[key] in self.keyMap
    
    def keysDown(self, *args):
        for arg in args:
            if(self.keyDown(arg)):
                return True
        return False
    
    def active(self):
        return len(self.keyMap) > 0

#Gives physics capability
class PhysicsObject:
    #Size and position of the physobj
    _xPos = 0
    _yPos = 0
    _width = 0
    _height = 0
    
    #Physics stuff
    _velocity = [0, 0] #Normalized directional vector
    _drag = 0.2
    _speed = 0.8
    _canLeave = False
    
    #Initialize the class with width and height
    def __init__(self, width, height):
        self._width = width
        self._height = height
        
    #Drag and Speed
    def setSpeed(self, speed):
        self._speed = speed
        
    def getSpeed(self):
        return self._speed
        
    def setDrag(self, drag):
        self._drag = drag
        
    def getDrag(self):
        return self._drag
    
    #Velocity
    def setVelocity(self, x, y):
        self._velocity = [x, y]
    
    def getVelocity(self):
        return self._velocity
        
    #Position
    def setPos(self, pos):
        if(self._canLeave):
            self._xPos = pos[0]
            self._yPos = pos[1]
        else:
            self._xPos = clamp(pos[0], 0, WIDTH-self._width)
            self._yPos = clamp(pos[1], 0, HEIGHT-self._height)
        
    def getPos(self):
        return [self._xPos, self._yPos]
    
    def getBounds(self):
        return [self._xPos, self._yPos, self._width, self._height]
    
    def setCanLeave(self, canLeave):
        self._canLeave = canLeave
    
    #Alex brand physics engine (tm)
    def think(self):
        scaled = map(lambda n: n*self._speed, self._velocity)
        
        [x, y] = self.getPos()
        
        self.setPos([
            x + scaled[0],
            y + scaled[1]
        ])
        
        self.setVelocity(
            lerp(self._drag, self._velocity[0], 0),
            lerp(self._drag, self._velocity[1], 0)
        )
        
#Projectiles
projs = []
class Projectile():
    rotation = 0
    shotByPlayer = False
    target = None
    
    def __init__(self, img, position, velocity, rotation=0):
        self.img = img
        self.physObj = PhysicsObject(self.img["width"], self.img["height"])
        self.physObj.setPos(position)
        self.physObj.setVelocity(*velocity)
        self.physObj.setDrag(0.02)
        self.physObj.setSpeed(2.5)
        self.physObj.setCanLeave(True)
        self.rotation = rotation
    
    def setKills(self, ent):
        self.target = ent
    
    def draw(self, canvas):
        [x, y, w, h] = self.physObj.getBounds()
        canvas.draw_image(self.img["image"], (w/2, h/2), (w, h), (x+w/2, y+h/2), (w, h), self.rotation + math.pi)
        
    def think(self):
        self.physObj.think()
        if(self.target is not None):
            [x, y, w, h] = self.physObj.getBounds()
            [ex, ey, ew, eh] = self.target.physObj.getBounds()
            
            dist = math.hypot(ex+ew/2 - x+w/2, ey+eh/2 - y+h/2)
            return dist < 256

    def outofbounds(self):
        self.position = self.physObj.getPos()
        return True in [self.position[0] >= WIDTH + 100, self.position[0] <= -100, self.position[1] >= HEIGHT + 100, self.position[1] <= -100]

def angle(zloc,ploc):
    return math.pi+atan(float(zloc[1]-ploc[1])/(zloc[0]-ploc[0]+0.000002)) if ploc[0] >= zloc[0] else atan(float(zloc[1]-ploc[1])/(zloc[0]-ploc[0]+0.00002)) 

def follow(zloc,ploc,s):
    if zloc[0] == ploc[0]:
        return [s,0] if zloc[1] < ploc[1] else [-s,0]
    if zloc[1] == ploc[1]:
        return [0,s] if zloc[0] < ploc[0] else [0,-s]
    angle = atan(float(zloc[1]-ploc[1])/(zloc[0]-ploc[0]))
    return [s*cos(angle),s*sin(angle)] if ploc[0] > zloc[0] else [-s*cos(angle),-s*sin(angle)]

def f_angle(angle, s):
    return [s*cos(angle),s*sin(angle)]

#Boss class
cyclic = 0
class Boss():
    _shots = []
    _moveX = 1
    _moveY = 1
    target = None
    
    maxHealth = 2000
    health = maxHealth
    
    def __init__(self, width, height):
        self.physObj = PhysicsObject(width, height)
        self.physObj.setSpeed(5)
        
    def draw(self, canvas):
        [x, y, w, h] = self.physObj.getBounds()
        canvas.draw_image(MACDUFF_SPRITE["image"], (w/2, h/2), (w, h), (x+w/2, y+h/2), (w, h))
        
        frac = float(self.health)/self.maxHealth
        
        drawRect(canvas, x, y, w, 10, "white")
        drawRect(canvas, x, y, w*frac, 10, "red")
        
        for i in self._shots:
            i.draw(canvas)
            i.rotation += 0.2
    
    def hurt(self, amt=10):
        self.health = clamp(self.health-amt, 0, self.maxHealth)
            
    def think(self):
        self.physObj.setVelocity(self._moveX, self._moveY)
        self.physObj.think()
        
        [x, y, w, h] = self.physObj.getBounds()
        if(x+w >= WIDTH or x == 0):
            self._moveX = self._moveX * -1
        elif(y+h >= HEIGHT or y == 0):
            self._moveY = self._moveY * -1
        
        for i in self._shots:
            hit = i.think()
            
            if(hit):
                self.target.hurt()
            
            if(hit or i.outofbounds()):
                self._shots.remove(i)
                break
    
    def fire(self, velocity):
        proj = Projectile(AXE_SPRITE, self.physObj.getPos(), velocity)
        proj.setKills(self.target)
        self._shots.append(proj)
    
    def shoop_de_whoop(self):
        for i in range(0, 360, 60):
            x = 10 * math.cos(math.radians(i))
            y = 10 * math.sin(math.radians(i))
            self.fire([x, y])
        
inputManager = InputManager()

#Our controllable player
class Player():
    animProgress = 0
    animActive = False
    
    maxHealth = 100
    health = maxHealth
    
    def __init__(self, width, height):
        self.physObj = PhysicsObject(width, height)
        self.physObj.setSpeed(8)
        self.physObj.setDrag(0.12)
    
    def hurt(self, amt=10):
        new = self.health - amt
        if(new <= 0):
            gameOver()
        else:
            self.health = new
            
    def think(self):
        vel = [0, 0]
        
        if(inputManager.keyDown("w")):
            vel[1] = -1
        if(inputManager.keyDown("a")):
            vel[0] = -1
        if(inputManager.keyDown("s")):
            vel[1] = 1
        if(inputManager.keyDown("d")):
            vel[0] = 1
        
        if(inputManager.keysDown("w", "a", "s", "d")):
            self.physObj.setVelocity(*vel)
            
        self.physObj.think()
        
    def draw(self, canvas, king):
        [x, y, w, h] = self.physObj.getBounds()
        img = (MACBETH_KING_SPRITE if king else MACBETH_SPRITE)["image"]
        canvas.draw_image(img, (w/2, h/2), (w, h), (x+w/2, y+h/2), (w, h))
        
        frac = float(self.health)/self.maxHealth
        
        if(CURRENT_SCENE == 9 and not DIALOGUE):
            drawRect(canvas, x, y, w, 10, "white")
            drawRect(canvas, x, y, w*frac, 10, "green")
        
#Define the instance of Macbeth supplying the bounding box's size
macbeth = Player(MACBETH_SPRITE["width"], MACBETH_SPRITE["height"])

#Define the final boss
macduff_god = Boss(MACDUFF_SPRITE["width"], MACDUFF_SPRITE["height"])
macduff_god.physObj.setPos([WIDTH*0.5, HEIGHT*0.6])
macduff_god.target = macbeth

#Switch dialogue
dialogueStr = ""
def setDialogue(dialogue):
    global CURRENT_DIALOGUE, dialogueStr
    CURRENT_DIALOGUE = dialogue
    dialogueStr = ""
    macbeth.animActive = False
    macbeth.animProgress =  0
    PLOT[CURRENT_SCENE]
    
    for i in PLOT[CURRENT_SCENE].get("sprites", []):
        i["animActive"] = False
        i["animProgress"] = 0

#Scene shit
def setScene(scene):
    global DIALOGUE, CURRENT_SCENE
    
    DIALOGUE = True
    CURRENT_SCENE = scene
    setDialogue(0)
    macbeth.physObj.setPos(PLOT[CURRENT_SCENE]["positions"][0]["macbeth"])
    
#Transitioning
def startTransition():
    global TRANSITIONING, TRANSITION_IN
    TRANSITIONING = True
    TRANSITION_IN = True

#Game over scene draw handler
def gameOverScene(canvas):
    drawRect(canvas, 0, 0, WIDTH, HEIGHT, "black")
    w = frame.get_canvas_textwidth("THE END", 100, "sans-serif")
    canvas.draw_text("THE END", (WIDTH/2-w/2, HEIGHT/2+50), 100, "#ffffff", "sans-serif")

    #Game over
def gameOver():
    frame.set_draw_handler(gameOverScene)
    
#Main game drawing
nextDialogueAdd = 0
def draw(canvas):
    scene = PLOT[CURRENT_SCENE]
    
    #Background image
    img = scene["background"]["image"]
    imgW = scene["background"]["width"]
    imgH = scene["background"]["height"]
    canvas.draw_image(img, (imgW/2, imgH/2), (imgW, imgH), (WIDTH/2, HEIGHT/2), (WIDTH, HEIGHT))
    
    #Draw the player character
    if("hideMacbeth" not in scene):
        macbeth.draw(canvas, "king" in scene)
    
    #Draw any extra sprites
    for i in scene.get("sprites", []) if DIALOGUE else []:
        anims = i["positions"]

        #Define some default things
        if("curPos" not in i):
            i["animActive"] = False
            i["animProgress"] = 0
            i["curPos"] = anims[0]
            i["rotation"] = 0
            i["hidden"] = False

        if(CURRENT_DIALOGUE in anims):
            anim = anims[CURRENT_DIALOGUE]
            i["hidden"] = anim == -1
            
            if(not i["hidden"]):
                [targetX, targetY, speed] = anim

                if(not i["animActive"] and i["animProgress"] == 0):
                    [curX, curY] = anim if i["curPos"] == -1 else i["curPos"]

                    i["animProgress"] = 0
                    i["animActive"] = True
                    i["lastX"], i["lastY"] = curX, curY

                #Position
                i["curPos"] = [
                    lerp(i["animProgress"], i["lastX"], targetX),
                    lerp(i["animProgress"], i["lastY"], targetY)
                ]

                #Rotation
                targetRot = anim[3] if len(anim) > 3 else 0
                i["rotation"] = lerp(i["animProgress"], i["rotation"], targetRot)

                #Progress
                i["animProgress"] = clamp(i["animProgress"] + speed, 0, 100)

                if(i["animProgress"] >= 100):
                    i["animActive"] = False
        
        if(not i["hidden"]):
            img = i["sprite"]["image"]
            [x, y] = i["curPos"]
            w = i["sprite"]["width"]
            h = i["sprite"]["height"]
        
            canvas.draw_image(img, (w/2, h/2), (w, h), (x+w/2, y+h/2), (w, h), math.radians(i["rotation"]))

    #Draw dialogue
    if(DIALOGUE):
        y = HEIGHT*0.7
        
        drawRect(canvas, 0, y, WIDTH, HEIGHT, DIALOGUE_COLOR)
        
        curDialogue = scene["dialogue"][CURRENT_DIALOGUE]
        
        #Adding to the current dialogue string
        global dialogueStr, nextDialogueAdd
        if(len(dialogueStr) != len(curDialogue[1]) and curTime() > nextDialogueAdd):
            dialogueStr += curDialogue[1][len(dialogueStr)]
            nextDialogueAdd = curTime() + DIALOGUE_SPEED
            
        canvas.draw_text(curDialogue[0]+":", (30, y+42), 42, "black", "sans-serif")
        canvas.draw_text(dialogueStr, (30, y+42+6+32), 32, "black", "sans-serif")
        
        #Animations for the player character
        anims = scene["positions"]
        if(CURRENT_DIALOGUE in anims):
            [targetX, targetY, speed] = anims[CURRENT_DIALOGUE]["macbeth"]
            
            if(not macbeth.animActive):
                [curX, curY] = macbeth.physObj.getPos()
                
                macbeth.animProgress = 0
                macbeth.animActive = True
                macbeth.lastX, macbeth.lastY = curX, curY
            
            macbeth.physObj.setPos([
                lerp(macbeth.animProgress, macbeth.lastX, targetX),
                lerp(macbeth.animProgress, macbeth.lastY, targetY)
            ])
            
            macbeth.animProgress = clamp(macbeth.animProgress + speed, 0, 100)
            
            if(macbeth.animProgress >= 100):
                macbeth.animActive = False
                macbeth.animProgress = 0
    else:
        #Handle character movement
        macbeth.think()
        
    #Transitioning
    global TRANSITIONING, TRANSITION_PROGRESS, TRANSITION_IN
    if(TRANSITIONING):
        TRANSITION_PROGRESS = lerp(0.08, TRANSITION_PROGRESS, 1 if TRANSITION_IN else 0)
        if(TRANSITION_IN and TRANSITION_PROGRESS > 0.99):
            TRANSITION_IN = False
           
            #Switching scenes
            if(len(PLOT)-1 > CURRENT_SCENE):
                setScene(CURRENT_SCENE + 1)
                
        elif(not TRANSITION_IN and TRANSITION_PROGRESS < 0.01):
            TRANSITIONING = False
            TRANSITION_PROGRESS = 0
            
        alpha = hex(int(clamp(TRANSITION_PROGRESS*255, 1, 255)))[2:]
        if(len(alpha) == 1): alpha = "0" + alpha
        drawRect(canvas, 0, 0, WIDTH, HEIGHT, "#000000" + alpha)
        
    for proj in projs:
        proj.draw(canvas)
        hit = proj.think()
        
        if(hit):
            macduff_god.hurt(15)
        
        if(hit or proj.outofbounds()):
            projs.remove(proj)
            break
            
    #Boss fight
    if(CURRENT_SCENE == 9 and not DIALOGUE):
        macduff_god.draw(canvas)
        macduff_god.think()
        
        global cyclic
        cyclic = cyclic + 1
        if cyclic%60 == 0:
            macduff_god.shoop_de_whoop()
    
#Input event handlers
def keydown(key):
    inputManager.pressKey(key)
    
def keyup(key):
    inputManager.releaseKey(key)

#Button class for UI
buttons = []
class Button:
    text = "Button"
    x = y = 0
    w = 100
    h = 30
    
    def __init__(self):
        buttons.append(self)
        
    def setPos(self, x, y):
        self.x, self.y = x, y
        
    def setSize(self, w, h):
        self.w, self.h = w, h
        
    def draw(self, canvas):
        canvas.draw_polygon([
            [self.x, self.y],
            [self.x + self.w, self.y],
            [self.x + self.w, self.y + self.h],
            [self.x, self.y + self.h],
        ], 1, "white", "gray")
        
        h = self.h-10
        w = frame.get_canvas_textwidth(GAME_START_BUTTON_TEXT, h, "sans-serif")
        canvas.draw_text(GAME_START_BUTTON_TEXT, (self.x+self.w/2-w/2, self.y+self.h/2+h/2.8), h, "white", "sans-serif")

#Creating our start button
startButton = Button()
startButton.text = GAME_START_BUTTON_TEXT
startButton.setSize(300, 50)
startButton.setPos(WIDTH/2-startButton.w/2, HEIGHT*0.6)

#Title screen
def titleScreen(canvas):
    w = frame.get_canvas_textwidth(GAME_TITLE, 100, "sans-serif")
    canvas.draw_text(GAME_TITLE, (WIDTH/2-w/2, HEIGHT/2-osc()*50), 100, "#ffffff", "sans-serif")
    startButton.draw(canvas)

#Called when we hit the start game button
def startGame():
    frame.set_draw_handler(draw) #Scene draw handler
    setScene(START_SCENE) #Initialize the first scene
    
    global GAME_STARTED
    GAME_STARTED = True

startButton.onClick = startGame

#Click handler that checks buttons
def clickButtons(pos):
    [x, y] = pos
    for but in buttons:
        if(x >= but.x and x <= but.x+but.w and
           y >= but.y and y <= but.y+but.h and
           hasattr(but, "onClick")):
             but.onClick()
             return True

#Mouseclick handler
def mouseClick(pos):
    #Handle buttonclicks first, if anything happened then just bail
    if(not GAME_STARTED):
        clickButtons(pos)
        return
    
    #Handle dialogue skipping
    global DIALOGUE
    if(DIALOGUE):
        dialogue = PLOT[CURRENT_SCENE]["dialogue"]
        [title, text] = dialogue[CURRENT_DIALOGUE]
        
        #Complete the dialogue if it's partial
        global dialogueStr
        if(len(dialogueStr) < len(text)):
            dialogueStr = text
        else:
            #Load new dialogue
            if(CURRENT_DIALOGUE < len(dialogue)-1):
                setDialogue(CURRENT_DIALOGUE + 1)
            else:
                #Break out of dialogue mode
                if("instantTransition" in PLOT[CURRENT_SCENE]):
                    startTransition()
                    
                DIALOGUE = False
    else:
        [x, y] = macbeth.physObj.getPos()
        mbp = [x+155, y+150]
        x += 155
        y += 150
        proj = Projectile(DAGGER_BIG_SPRITE, mbp, follow(mbp,pos,10), angle(mbp,pos)+math.pi/2)
        proj.shotByPlayer = True
        proj.setKills(macduff_god)
        projs.append(proj)

#Frame declaration and handler assignment
frame = simplegui.create_frame(GAME_TITLE, WIDTH, HEIGHT)
frame.set_draw_handler(titleScreen)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(mouseClick)
frame.add_button("Transition", startTransition)
frame.start()
