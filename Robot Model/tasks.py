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
sk_reed = PieceSkill("reed", "piece", "reed")

# * (Skill 6) A Push Button Switch should be used
sk_button = PieceSkill("button","piece","button")

# * (Skill 7) A Lamp should be used
sk_lamp = PieceSkill("lamp", "piece", "lamp")

# * (Skill 8) A Battery should be used
sk_battery = PieceSkill("battery", "piece", "battery")

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



# #------------------------------------------------------------------
# ## Connection skills

# # * (skill 13) - Connect LED to Switch
# led_switch = ConnectionSkill("led_switch", "connection", "led", "switch")

# # * (skill 14) - Connect LED to Button
# led_button = ConnectionSkill("led_button", "connection", "led", "button")

# # * (skill 15) - Connect LED to Reed Switch
# led_reed = ConnectionSkill("led_mc", "connection", "led", "reed")

# led_motor = ConnectionSkill("led_motor", "connection", "led", "motor")

# # * (skill 16) - Connect Switch to Button
# switch_button = ConnectionSkill("switch_button", "connection", "switch", "button")

# # * (skill 17) - Connect Switch to Motor
# switch_motor = ConnectionSkill("switch_motor", "connection", "switch", "motor")

# # * (skill 18) - Connect Switch to Speaker
# switch_speaker = ConnectionSkill("switch_speaker", "connection", "switch", "speaker")

# # * (skill 19) - Connect Button to Motor
# button_motor = ConnectionSkill("button_motor", "connection", "button", "motor")

# # * (skill 20) - Connect Button to Speaker
# button_speaker = ConnectionSkill("button_speaker", "connection", "button", "speaker")

# # * (skill 21) - Connect Bulb to Switch
# bulb_switch = ConnectionSkill("bulb_switch", "connection", "bulb", "switch")

# # * (skill 22) - Connect Bulb to Button
# bulb_button = ConnectionSkill("bulb_reed", "connection", "bulb", "button")

# # * (skill 23) - Connect Bulb to Reed Switch
# bulb_reed = ConnectionSkill("bulb_reed", "connection", "bulb", "reed")

# # * (skill 24 ) - Connect Switch to MC
# switch_mc = ConnectionSkill("switch_mc", "connection", "switch", "mc")

# # * (skill 25 ) - Connect Button to MC
# button_mc = ConnectionSkill("button_mc", "connection", "button", "mc")

# # * (skill 26 ) - Connect Speaker to MC
# speaker_mc = ConnectionSkill("speaker_mc", "connection", "speaker", "mc")

# # * (skill 27 ) - Connect Speaker to FM
# speaker_fm = ConnectionSkill("speaker_fm", "connection", "speaker", "fm")



#------------------------------------------------------------------
## LED direction skills

# * (skill 13) The correct directionality of an LED
sk_dir_led = DirectionSkill("led_direc", "led")


#------------------------------------------------------------------
## High level skills

# * (skill 14) How to power an MC
power_mc = MCSkill("power", "mc", "power", "wire")

# * (skill 15) How to change the signal on the FM
signal_fm = MCSkill("signal", "FM", "signal", "FM")

# * (skill 16) How to change the signal on the FM
signal_fm = MCSkill("signal", "fm", "signal", "wire")

#------------------------------------------------------------------
## Closing skills

# * (skill 17) That the circuit should be a circuit
closed_circuit = ClosingSkill("simple_closed", "closing")



all_skills = [sk_led, sk_FM,sk_buzzrer,sk_switch, sk_reed, sk_button,sk_lamp, sk_battery, sk_speaker, sk_music, sk_motor,sk_cp, sk_dir_led, power_mc, signal_FM, closed_circuit]

################################################


task1 = Task(1,"sw_la", ["switch", "lamp"], [], 
		[0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
		"Build a circuit that you can turn a light on and off using a switch")

task2 = Task(2,"bu_la", ["button", "lamp"], [],
		[0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
		"Build a circuit that you can turn a light on and off using a button")

task3 = Task(3,"re_la", ["reed", "lamp"], [],
		[0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
		"Build a circuit that you can turn a light on and off using a reed switch")

task4 = Task(4,"sw_mo", ["switch", "motor"], [],
		[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1 ],
		"Build a circuit that you can turn a motor on and off using a switch")

task5 = Task(5,"bu_mo", ["button", "motor"], [],
		[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1 ],
		"Build a circuit that you can turn a motor on and off using a switch")

task6 = Task(6,"re_mo", ["reed", "motor"], [],
		[0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1 ],
		"Build a circuit that you can turn a motor on and off using a switch")

task7 = Task(7,"mo", ["motor"], [],
		[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1 ],
		"Build a circuit that constantly will have a motor spinning")

task8 = Task(8,"sw_le", ["switch", "led"], [],
		[1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1 ],
		"Build a circuit that you can turn a LED on and off using a switch")

task9 = Task(9,"le", ["led"], [],
		[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1 ],
		"Build a circuit that has a constant LED on")

task10 = Task(10,"mc_sp", ["mc", "speaker"], [],
	    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1 ],
		"Build a circuit that plays music")

task11 = Task(11,"mc_sp_sw", ["mc", "speaker", "switch"], [],
		[0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1 ],
		"Build a circuit that plays music when a switch is turned on")

task12 = Task(12,"mc_sp_bu", ["mc", "speaker", "button"], [],
		[0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1 ],
		"Build a circuit that plays music when a button is pressed")

task13 = Task(13,"mc_sp_re", ["mc", "speaker", "reed"], [],
		[0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1 ],
		"Build a circuit that plays music when a reed switch is turned on")

task14 = Task(14,"mc_le", ["mc", "led"], [],
		[1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1 ],
		"Build a circuit that blinks a light in a rythm of a song")

task15 = Task(15,"mc_le_sw", ["mc", "led", "switch"], [],
		[1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1 ],
		"Build a circuit that blinks a light in the rythm of a song when a switch is turned on")

task16= Task(16,"mc_le_bu", ["mc", "led", "button"], [], 
		[1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1 ],
		"Build a circuit that blinks a light in the rythm of a song when a button is pressed")

task15 = Task(15,"mc_le_re", ["mc", "led", "reed"], [],
		[1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1 ],
		"Build a circuit that blinks a light in the rythm of a song when a reed switch is turned on")