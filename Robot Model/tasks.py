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


## Piece Picking Skills

#4) When a Resistor should be used 
sk_resistor = PieceSkill("resistor","piece","resistor") 


#6) When a switch should be used
sk_switch = PieceSkill("switch","piece","switch") 





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

# * (Skill 5) A Push Button Switch should be used
sk_button = PieceSkill("button","piece","button")

# * (Skill 6) A Lamp should be used
sk_lamp = PieceSkill("lamp", "piece", "lamp")

# * (Skill 7) A Battery should be used
sk_battery = PieceSkill("battery", "piece", "button")

# * (Skill 8) A Speaker should be used
sk_speaker = PieceSkill("speaker","piece","speaker") 

# * (Skill 9) A IC-Music should be used
sk_music = PieceSkill("music","piece","music") 

# * (Skill 10) A Motor should be used
sk_motor = PieceSkill("motor","piece","motor") 