# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [2,1]
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_vel = 0
paddle2_vel = 0
PointPlayer1 = 0
PointPlayer2 = 0
#paddle1_draw = [, ]
#paddle2_draw = [, ]
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, WIDTH,HEIGHT # these are vectors stored as lists
    global PointPlayer1,PointPlayer2
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if(direction == 'RIGHT'):
        ball_vel[0] = random.randrange(120, 240)/60
        ball_vel[1] = -random.randrange(60, 180)/60
        PointPlayer1=0
        PointPlayer2=0
    if(direction == RIGHT):
        ball_vel[0] = random.randrange(120, 240)/60
        ball_vel[1] = -random.randrange(60, 180)/60
        PointPlayer2 = PointPlayer2 +1
    if(direction == 'LEFT'):
        ball_vel[0] = -random.randrange(120, 240)/60
        ball_vel[1] = -random.randrange(60, 180)/60
        PointPlayer1=0
        PointPlayer2=0
    if(direction == LEFT):
        ball_vel[0] = -random.randrange(120, 240)/60
        ball_vel[1] = -random.randrange(60, 180)/60
        PointPlayer1 = PointPlayer1+1


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2 
    global ball_pos,WIDTH, HEIGHT
    ball_pos = [WIDTH / 2, HEIGHT / 2]  
    left_or_right = ['LEFT', 'RIGHT']
    spawn_ball(random.choice(left_or_right))
    
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos
    global ball_vel, BALL_RADIUS,PAD_WIDTH,WIDTH,PAD_HEIGHT
    global paddle1_draw, paddle2_draw, paddle1_vel,paddle2_vel
    global PointPlayer1, PointPlayer2
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    paddle1_pos = paddle1_pos + paddle1_vel  
    paddle2_pos = paddle2_pos - paddle2_vel
    
    ## bouncing of balls of ceiling
    if(ball_pos[1]<=BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    if(ball_pos[1]>=(HEIGHT-1)-BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    #
    
    ##restricting paddle movement
    if paddle1_pos<=PAD_HEIGHT/2 or paddle1_pos>=HEIGHT-PAD_HEIGHT/2:
        paddle1_vel=0
    if paddle2_pos<=PAD_HEIGHT/2 or paddle2_pos>=HEIGHT-PAD_HEIGHT/2:
        paddle2_vel=0
    #
    
    ##hitting the ball with paddles or spawning
    if(ball_pos[0] <=PAD_WIDTH + BALL_RADIUS and ball_pos[1]<=paddle1_pos+PAD_HEIGHT/2 and ball_pos[1]>=paddle1_pos-PAD_HEIGHT/2 ):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] = ball_vel[0] + 0.1*ball_vel[0]
        ball_vel[1] = ball_vel[1] + 0.1*ball_vel[1]
    elif(ball_pos[0] <=PAD_WIDTH + BALL_RADIUS and (ball_pos[1]>paddle1_pos+PAD_HEIGHT/2 or ball_pos[1]<paddle1_pos-PAD_HEIGHT/2)) :
        spawn_ball(RIGHT)
    if(ball_pos[0] >=WIDTH-PAD_WIDTH-BALL_RADIUS and ball_pos[1]<=paddle2_pos+PAD_HEIGHT/2 and ball_pos[1]>=paddle2_pos-PAD_HEIGHT/2):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] = ball_vel[0] + 0.1*ball_vel[0]
        ball_vel[1] = ball_vel[1] + 0.1*ball_vel[1]
    elif(ball_pos[0] >=WIDTH-PAD_WIDTH-BALL_RADIUS and (ball_pos[1]>paddle2_pos+PAD_HEIGHT/2 or ball_pos[1]<paddle2_pos-PAD_HEIGHT/2)) :
        spawn_ball(LEFT)
    #
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    canvas.draw_line([PAD_WIDTH/2,paddle1_pos+PAD_HEIGHT/2],[PAD_WIDTH/2,paddle1_pos-PAD_HEIGHT/2], PAD_WIDTH, 'WHITE')
    canvas.draw_line([WIDTH-PAD_WIDTH/2,paddle2_pos-PAD_HEIGHT/2],[WIDTH-PAD_WIDTH/2,paddle2_pos+PAD_HEIGHT/2], PAD_WIDTH, 'WHITE')
    canvas.draw_text(str(PointPlayer1), [WIDTH/2-50,50], 30, "White")
    canvas.draw_text(str(PointPlayer2), [WIDTH/2+50,50], 30, "White")
    #canvas.draw_text("PONG@KherDevelopers", [WIDTH/2-80,390], 20, "White")
    # update ball
            
    # draw ball
    
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel,paddle1_pos,paddle2_pos
    acc=4
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel= paddle1_vel + acc
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel+=paddle1_vel - acc
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel= paddle2_vel + acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel+=paddle2_vel - acc

   
def keyup(key):
    global paddle1_vel, paddle2_vel,paddle1_pos,paddle2_posl
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel=0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel=0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel=0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel=0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)



# start frame
new_game()
frame.start()
