class Skill():
	def __init__(self,name, skill_type):
		self.name = name
		self.skill_type = skill_type
	
class PieceSkill(Skill):	
	def __init__(self,name,skill_type,piece):
		Skill.__init__(self,name, skill_type)
		self.piece = piece

class ConnectionSkill(Skill):	
	def __init__(self,name,skill_type,piece1,piece2):
		Skill.__init__(self,name, skill_type)
		self.piece1 = piece1
		self.piece2 = piece2

class ClosingSkill(Skill):	
	def __init__(self,name,skill_type):
		Skill.__init__(self,name, skill_type)
		
class MusicSkill(Skill):	
	def __init__(self,name, skill_type,port,piece):
		Skill.__init__(self,name, skill_type)
		self.port = port
		self.piece = piece
		
class DirectionSkill(Skill):
	def __init__(self, name, skill_type):
		Skill.__init__(self, name, skill_type)
		
class ConnectPieces(Skill):
	def __init__(self, name, skill_type):
		Skill.__init__(self, name, skill_type)

class Task():
	def __init__(self,task_id,name, pieces, skills, action = [], instruction = ""):
		self.id = task_id
		self.name = name
		self.pieces = pieces
		self.skills = skills
		self.action = action
		self.obs = []
		self.instruction = instruction




#------------------------------------------------------------------
## Piece Picking Skills

# * (Skill 1) When a LED should be used
sk_led = PieceSkill("led","piece","led") 

# * (Skill 2) When a FM Radio receiver should be used
sk_FM = PieceSkill("FM", "piece","FM")

# * (Skill 3) A Buzzrer should be used
sk_buzzrer = PieceSkill("buzzrer", "piece", "buzzrer")

# * (Skill 4) A Switch should be used
sk_switch = PieceSkill("switch", "piece", "switch")

# * (Skill 5) A Reed Switch should be used
sk_reed = PieceSkill("reed", "piece", "buzzrer")

# * (Skill 6) A Push Button Switch should be used
sk_button = PieceSkill("button","piece","button")

# * (Skill 7) A Lamp should be used
sk_lamp = PieceSkill("lamp", "piece", "lamp")

# * (Skill 8) A Battery should be used
sk_battery = PieceSkill("battery", "piece", "button")

# * (Skill 9) A Speaker should be used
sk_speaker = PieceSkill("speaker","piece","speaker") 

# * (Skill 10) A IC-Music should be used
sk_music = PieceSkill("music","piece","music") 

# * (Skill 11) A Motor should be used
sk_motor = PieceSkill("motor","piece","motor") 
#------------------------------------------------------------------
## Piece connecting skills

# * (skill 12) How to Connect two pieces together
sk_cp = ConnectPieces("connect", "connect_pieces")



#------------------------------------------------------------------
## Connection skills

# * (skill 13) - Connect LED to Switch
led_switch = ConnectionSkill("led_switch", "connection", "led", "switch")

# * (skill 14) - Connect LED to Button
led_button = ConnectionSkill("led_button", "connection", "led", "button")

# * (skill 15) - Connect LED to Reed Switch
led_reed = ConnectionSkill("led_mc", "connection", "led", "reed")

led_motor = ConnectionSkill("led_motor", "connection", "led", "motor")

# * (skill 16) - Connect Switch to Button
switch_button = ConnectionSkill("switch_button", "connection", "switch", "button")

# * (skill 17) - Connect Switch to Motor
switch_motor = ConnectionSkill("switch_motor", "connection", "switch", "motor")

# * (skill 18) - Connect Switch to Speaker
switch_speaker = ConnectionSkill("switch_speaker", "connection", "switch", "speaker")

# * (skill 19) - Connect Button to Motor
button_motor = ConnectionSkill("button_motor", "connection", "button", "motor")

# * (skill 20) - Connect Button to Speaker
button_speaker = ConnectionSkill("button_speaker", "connection", "button", "speaker")

# * (skill 21) - Connect Bulb to Switch
bulb_switch = ConnectionSkill("bulb_switch", "connection", "bulb", "switch")

# * (skill 22) - Connect Bulb to Button
bulb_button = ConnectionSkill("bulb_reed", "connection", "bulb", "button")

# * (skill 23) - Connect Bulb to Reed Switch
bulb_reed = ConnectionSkill("bulb_reed", "connection", "bulb", "reed")

# * (skill 24 ) - Connect Switch to MC
switch_mc = ConnectionSkill("switch_mc", "connection", "switch", "mc")

# * (skill 25 ) - Connect Button to MC
button_mc = ConnectionSkill("button_mc", "connection", "button", "mc")

# * (skill 26 ) - Connect Speaker to MC
speaker_mc = ConnectionSkill("speaker_mc", "connection", "speaker", "mc")

# * (skill 27 ) - Connect Speaker to FM
speaker_fm = ConnectionSkill("speaker_fm", "connection", "speaker", "fm")







#------------------------------------------------------------------
## LED direction skills

# * (skill 28) The correct directionality of an LED
sk_dir_led = DirectionSkill("led_direc", "led")


#------------------------------------------------------------------
## High level skills

# * (skill 29) How to power an MC
power_mc = MCSkill("power", "mc", "power", "wire")

# * (skill 30) How to connect the signal on the MC
signal_mc = MCSkill("signal", "mc", "signal", "wire")




#------------------------------------------------------------------
## Closing skills

# * (skill 31) That the circuit should be a circuit
closed_circuit = ClosingSkill("simple_closed", "closing")



