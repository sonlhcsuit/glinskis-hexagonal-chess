extends Node2D
########################################################
#				Setting up board pieces               #
########################################################
var state={
	"white":{
		"pawn1":"B2",
		"pawn2":"C3",
		"pawn3":"D4",
		"pawn4":"E5",
		"pawn5":"F4",
		"pawn6":"G3",
		"pawn7":"H2",
		"bishop1":"E1",
		"bishop2":"E2",
		"bishop3":"E3",
		"rook1":"B1",
		"rook2":"H1",
		"knight1":"C1",
		"knight2":"G1",
		"queen1":"D1",
		"king":"F1",
	},
	"black":{
		"pawn1":"B6",
		"pawn2":"C6",
		"pawn3":"D6",
		"pawn4":"E6",
		"pawn5":"F6",
		"pawn6":"G6",
		"pawn7":"H6",
		"bishop1":"E8",
		"bishop2":"E9",
		"bishop3":"E10",
		"rook1":"B7",
		"rook2":"H7",
		"knight1":"C8",
		"knight2":"G8",
		"queen1":"D9",
		"king":"F9",
	}
}
var is_selected_piece:Dictionary = {
	"team":"null",
	"name":"null",
	"type":"null",
	"location":"null",
};
var boardName:Array = ["A","B","C","D","E","F","G","H","I"];
var moveable:Array =[]
var is_selected = false;
var whiteTurn = true;
var blackTurn = false;
########################################################
#				Setting up chess action               #
########################################################
func is_location_valid(location:String)->bool:
	if(location==null):
		return false
	var x= location[0];
	var y = int(location.lstrip("1"))
	if(x=="A" || x=="I"):
		if(y>=1 && y<=6):
			return true
	elif(x=="B"||x=="H"):
		if(y>=1 && y<=7):
			return true
	elif(x=="C"||x=="G"):
		if(y>=1 && y<=8):
			return true
	elif(x=="D"||x=="F"):
		if(y>=1 && y<=9):
			return true
	elif(x=="E"):
		if(y>=1 && y<=10):
			return true
	return false

func is_location_empty(state:Dictionary,location:String):
	for team in state:
		for piece in state[team]:
			if(location == state[team][piece]):
				return false
	return true
	
#+++++++++++++GENERATE NEXT POSSIBLE MOVE +++++++++++++#
func generate_pawn_move(location:String)->Array:
	var x= boardName.find(location[0])
	var y = int(location.lstrip("1"))
	var next_move = null
	var next_attack1 = null
	var next_attack2 = null
	var valid_move:Array=[]
	#white pawn move up, black pawn move down
	if(is_selected_piece["team"].to_upper()=="WHITE"):
		next_move = String(boardName[x])+String(y+1)
		if(is_location_valid(next_move) && is_location_empty(state,next_move)):
			valid_move.append(next_move)
		if(x<4):
			next_attack1 = String(boardName[x-1]) + String(y)
			next_attack2 = String(boardName[x+1]) + String(y+1)
		elif(x==4):
			next_attack1 = String(boardName[x-1]) + String(y)
			next_attack2 = String(boardName[x+1]) + String(y)
		elif(x>4):
			next_attack1 = String(boardName[x-1]) + String(y+1)
			next_attack2 = String(boardName[x+1]) + String(y)
		if(next_attack1!=null && is_location_valid(next_attack1) && !is_location_empty(state,next_attack1) && get_piece_info_at(state,next_attack1)["team"]!= is_selected_piece["team"]):
			valid_move.append(next_attack1)
		if(next_attack2!=null && is_location_valid(next_attack2) &&!is_location_empty(state,next_attack2) && get_piece_info_at(state,next_attack2)["team"]!= is_selected_piece["team"]):
			valid_move.append(next_attack2)
			
	elif(is_selected_piece["team"].to_upper()=="BLACK"):
		next_move = String(boardName[x])+String(y-1)
		if(is_location_valid(next_move) && is_location_empty(state,next_move)):
			valid_move.append(next_move)
		if(x<4):
			next_attack1 = String(boardName[x-1]) + String(y-1)
			next_attack2 = String(boardName[x+1]) + String(y)
		elif(x==4):
			next_attack1 = String(boardName[x-1]) + String(y-1)
			next_attack2 = String(boardName[x+1]) + String(y-1)
		elif(x>4):
			next_attack1 = String(boardName[x-1]) + String(y)
			next_attack2 = String(boardName[x+1]) + String(y-1)
		if(next_attack1!=null && is_location_valid(next_attack1) && !is_location_empty(state,next_attack1) && get_piece_info_at(state,next_attack1)["team"]!= is_selected_piece["team"]):
			valid_move.append(next_attack1)
		if(next_attack2!=null && is_location_valid(next_attack2) &&!is_location_empty(state,next_attack2) && get_piece_info_at(state,next_attack2)["team"]!= is_selected_piece["team"]):
			valid_move.append(next_attack2)
	return valid_move

func generate_knight_move(location:String)->Array:
	var x= boardName.find(location[0])
	var y = int(location.lstrip("1"))
	var next_move:Array = []
	var valid_move:Array=[]
	var cal:Array = []
	if(x==0 || x==1):
		cal=[-3,-1,-3,-2,
		-2,-3,-2,1,
		-1,-3,-1,2,
		1,-2,1,3,
		2,-1,2,3,
		3,1,3,2]
	elif(x==2):
		cal=[
		-3,-1,-3,-2,
		-2,-3,-2,1,
		-1,-3,-1,2,
		1,-2,1,3,
		2,-1,2,3,
		3,0,3,1]
	elif(x==3):
		cal=[
		-3,-1,-3,-2,
		-2,-3,-2,1,
		-1,-3,-1,2,
		1,-2,1,3,
		2,2,2,-2,
		3,0,3,-1]
	elif(x==4):
		cal=[
		-3,-1,-3,-2,
		-2,-3,-2,1,
		-1,-3,-1,2,
		1,-3,1,2,
		2,1,2,-3,
		3,-1,3,-2]
	elif(x==5):
		cal=[
		-3,0,-3,-1,
		-2,-2,-2,2,
		-1,-2,-1,3,
		1,-3,1,2,
		2,1,2,-3,
		3,-1,3,-2]
	elif(x==6):
		cal=[
		-3,0,-3,1,
		-2,-1,-2,3,
		-1,-2,-1,3,
		1,-3,1,2,
		2,1,2,-3,
		3,-1,3,-2]
	elif(x==7||x==8):
		cal=[
		-3,2,-3,1,
		-2,-1,-2,3,
		-1,-2,-1,3,
		1,-3,1,2,
		2,1,2,-3,
		3,-1,3,-2]
		
	for i in range(12):
			var xtemp = x+cal[2*i]
			var ytemp = y+cal[2*i+1]
			if(xtemp>=0 && xtemp<=8 ):
				next_move.append(String(boardName[xtemp]) + String(ytemp))
			else:
				continue
	for i in next_move:
		if(is_location_valid(i)):
			if(get_piece_info_at(state,i)["team"] != is_selected_piece["team"]):
				valid_move.append(i)
	return valid_move
	
func generate_bishop_move(location:String)->Array:
	var pureX= boardName.find(location[0])
	var x = pureX
	var pureY = int(location.lstrip("1"))
	var y = pureY
	var next_move:Array=[]
	var temp =""
	if(x<=4):
		var flags = [true,true,true,true]
		while true:
			x=x+2
			if(x>8):
				break
			if(x==5):
				y=y
			elif(x==4 ||x==2 || x==3):
				y=y+1
			elif(x==6||x==7 ||x==8):
				y=y-1
			temp = String(boardName[x])+String(y)
			if(is_location_empty(state,temp)):
				next_move.append(temp)
			else:
				if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
					next_move.append(temp)
				break
		x=pureX;y=pureY
		while true:
			x=x-2
			if(x<0):
				break
			y=y-1
			temp = String(boardName[x])+String(y)
			if(is_location_empty(state,temp)):
				next_move.append(temp)
			else:
				if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
					next_move.append(temp)
				break
		x=pureX;y=pureY
		while true:
			x=x-1
			if(x<0):
				break
			if(x==0 || x==1|| x==2||x==3):
				y=y-2
			temp = String(boardName[x])+String(y)
			if(is_location_empty(state,temp)):
				next_move.append(temp)
			else:
				if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
					next_move.append(temp)
				break
		x=pureX;y=pureY
		while true:
			x=x+1
			if(x>8):
				break
			if(x==0 || x==1|| x==2||x==3 || x==4):
				y=y+2
			elif(x==5 || x==6 ||x==7||x==8):
				y=y+1
			temp = String(boardName[x])+String(y)
			if(is_location_empty(state,temp)):
				next_move.append(temp)
			else:
				if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
					next_move.append(temp)
				break
		x=pureX;y=pureY
		while true:
			x=x-1
			if(x<0):
				break
			if(x==0 || x==1|| x==2||x==3):
				y=y+1
			temp = String(boardName[x])+String(y)
			if(is_location_empty(state,temp)):
				next_move.append(temp)
			else:
				if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
					next_move.append(temp)
				break
		x=pureX;y=pureY
		while true:
			x=x+1
			if(x>8):
				break
			if(x==0 || x==1|| x==2||x==3 || x==4):
				y=y-1
			elif(x==5 || x==6 ||x==7||x==8):
				y=y-2
			temp = String(boardName[x])+String(y)
			if(is_location_empty(state,temp)):
				next_move.append(temp)
			else:
				if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
					next_move.append(temp)
				break
	else:
		x=pureX;y=pureY
		while true:
			x=x-2
			if(x<0):
				break
			if(x==6 || x==5 ||x==4):
				y=y+1
			elif(x==0 ||x==1||x==2):
				y=y-1
			temp = String(boardName[x])+String(y)
			if(is_location_empty(state,temp)):
				next_move.append(temp)
			else:
				if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
					next_move.append(temp)
				break
		x=pureX;y=pureY
		while true:
			x=x+2
			if(x>8):
				break
			y=y-1
			temp = String(boardName[x])+String(y)
			if(is_location_empty(state,temp)):
				next_move.append(temp)
			else:
				if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
					next_move.append(temp)
				break
		x=pureX;y=pureY
		while true:
			x=x-1
			if(x<0):
				break
			if(x>=4):
				y=y-1

			elif(x==0 || x==1|| x==2||x==3):
				y=y-2
			temp = String(boardName[x])+String(y)
			if(is_location_empty(state,temp)):
				next_move.append(temp)
			else:
				if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
					next_move.append(temp)
				break
		x=pureX;y=pureY
		while true:
			x=x+1
			if(x>8):
				break
			y=y+1
			temp = String(boardName[x])+String(y)
			if(is_location_empty(state,temp)):
				next_move.append(temp)
			else:
				if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
					next_move.append(temp)
				break
		x=pureX;y=pureY
		while true:
			x=x-1
			if(x<0):
				break
			if(x>=4):
				y=y+2
			elif(x==0 || x==1|| x==2||x==3):
				y=y+1
			temp = String(boardName[x])+String(y)
			if(is_location_empty(state,temp)):
				next_move.append(temp)
			else:
				if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
					next_move.append(temp)
				break
		x=pureX;y=pureY
		while true:
			x=x+1
			if(x>8):
				break
			if(x==5 ||x==6||x==7||x==8):
				y=y-2
			temp = String(boardName[x])+String(y)
			if(is_location_empty(state,temp)):
				next_move.append(temp)
			else:
				if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
					next_move.append(temp)
				break
	var valid_move:Array=[]
	for i in next_move:
		if(is_location_valid(i)):
#			if(get_piece_info_at(state,i)["team"] != is_selected_piece["team"]):
			valid_move.append(i)
	return valid_move	
	
func generate_rook_move(location:String)->Array:
	var x= boardName.find(location[0])
	var pureY = int(location.lstrip("1"))
	var y = pureY
	var next_move:Array=[]
	var valid_move:Array = []
	for i in range(y,11):
		var temp = String(boardName[x])+String(i+1)
		if(is_location_empty(state,temp)):
			next_move.append(temp)
		else:
			if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
				next_move.append(temp)
			break
	for i in range(1,y):
		var temp = String(boardName[x])+String(y-i)
		if(is_location_empty(state,temp)):
			next_move.append(temp)
		else:
			if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
				next_move.append(temp)
			break
	if(x <= 4):
		for i in range(0,x):
			var j = abs(i-(x-1))
			y=y-1
			var temp = String(boardName[j])+String(y)
			if(is_location_empty(state,temp)):
				next_move.append(temp)
			else:
				if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
					next_move.append(temp)
				break
		y = pureY
		for i in range(x+1,9):
			var temp = ""
			if(i>4):
				temp = String(boardName[i])+String(y)
			else:
				y=y+1
				temp = String(boardName[i])+String(y)
			if(is_location_empty(state,temp)):
				next_move.append(temp)
			else:
				if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
					next_move.append(temp)
				break
		y = pureY
		for i in range(0,x+1):
			var j = abs(i-(x-1))
			var temp = String(boardName[j])+String(y)
			if(is_location_empty(state,temp)):
				next_move.append(temp)
			else:
				if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
					next_move.append(temp)
				break
		for i in range(x+1,9):
			var temp = ""
			if(i>4):
				y=y-1
				temp = String(boardName[i])+String(y)
			else:
				temp = String(boardName[i])+String(y)
			if(is_location_empty(state,temp)):
				next_move.append(temp)
			else:
				if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
					next_move.append(temp)
				break
	else:
		var flags= [true,true,true,true]
		for i in range(x+1,9):
			var temp = String(boardName[i])+String(y)
			if(is_location_empty(state,temp)):
				next_move.append(temp)
			else:
				if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
					next_move.append(temp)
				break
		for i in range(0,x):
			var j = abs(i-(x-1))
			var temp = ""
			if(j>=4):
				temp = String(boardName[j])+String(y)
			else:
				y=y-1
				temp = String(boardName[j])+String(y)
			if(is_location_empty(state,temp)):
				next_move.append(temp)
			else:
				if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
					next_move.append(temp)
				break
		y = pureY
		for i in range(x+1,9):
			y=y-1
			var temp = String(boardName[i])+String(y)
			next_move.append(temp)
			if(is_location_empty(state,temp)):
				next_move.append(temp)
			else:
				if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
					next_move.append(temp)
				break
		y = pureY
		for i in range(0,x):
			var j = abs(i-(x-1))
			var temp = ""
			if(j>=4):
				y=y+1
				temp = String(boardName[j])+String(y)
			else:
				temp = String(boardName[j])+String(y)
			if(is_location_empty(state,temp)):
				next_move.append(temp)
			else:
				if(get_piece_info_at(state,temp)["team"]!= is_selected_piece["team"]):
					next_move.append(temp)
				break
	for i in next_move:
		if(is_location_valid(i)):
			if(get_piece_info_at(state,i)["team"] != is_selected_piece["team"]):
				valid_move.append(i)
	return valid_move	
	
func generate_queen_move(location:String)->Array:
	return generate_rook_move(location) + generate_bishop_move(location)
	
func generate_king_move(location:String)->Array:
	var x = boardName.find(location[0])
	var pureY = int(location[1])
	var y = pureY
	var next_move:Array=[]
	var valid_move:Array=[]
	var  cal = []
	if(x==4):
		cal = [-1,-1,-1,0,0,-1,0,1,1,-1,1,0]
	elif(x<4):
		 cal = [-1,-1,-1,0,0,-1,0,1,1,1,1,0]
	elif(x>4):
		cal = [-1,0,-1,1,0,-1,0,1,1,0,1,-1]
	for i in range(6):
			var xtemp = x+cal[2*i]
			var ytemp = y+cal[2*i+1]
			if(xtemp>=0 && xtemp<=8 ):
				next_move.append(String(boardName[xtemp]) + String(ytemp))
			else:
				continue
	for i in next_move:
		if(is_location_valid(i)):
			if(get_piece_info_at(state,i)["team"] != is_selected_piece["team"]):
				valid_move.append(i)
	return valid_move
	
func generate_next_move(location:String)->Array:
	var type = is_selected_piece["type"]
	if(type=="pawn"):
		return generate_pawn_move(location)
	elif(type=="knight"):
		return generate_knight_move(location)
	elif(type=="bishop"):
		return generate_bishop_move(location)
	elif(type=="rook"):
		return generate_rook_move(location)
	elif(type=="king"):
		return generate_king_move(location)
	elif(type=="queen"):
		return generate_queen_move(location)
	else:
		return []
		
#+++++++++++++SHOW NEXT POSSIBLE MOVE AS RED DOT++++++#
func set_moveable(new_moveable:Array)->void:
	self.moveable = new_moveable
	return

func reset_movable()->void:
	self.moveable = [];
	return

func show_movable()->void:
	if(self.moveable.empty()):
		return
	for location in self.moveable:
		var temp_node = get_location(location)
		var texture = temp_node.get_focused_texture()
		temp_node.set_normal_texture(texture)
	return

func hide_movable()->void:
	for location in self.moveable:
		var temp_node = get_location(location)
		temp_node.set_normal_texture(null)
	return

func trigger_moveable(new_move:Array=[])->void:
	if(self.is_selected):
		set_moveable(new_move)
		show_movable()
	else:
		hide_movable()
		reset_movable()
	return

#++++++++++++++++++++SELECT MOVE ++++++++++++++++++++++++#
func reset_select()->void:
	self.is_selected = false
	self.is_selected_piece= {
	"team":"",
	"name":"",
	"type":"",
	"location":"",
	}
	return

func update_state(newpos)->void:
	self.state[self.is_selected_piece.team][self.is_selected_piece.name]=newpos
	return

func select_piece_at(location:String)->void:
	if(is_location_empty(state,location)):
		return
	else:
		var piece = get_piece_info_at(self.state,location)
		self.is_selected_piece["team"]=piece["team"]
		self.is_selected_piece["name"]=piece["name"]
		self.is_selected_piece["type"]=piece["type"]
		self.is_selected_piece["location"]=location
	return

func get_piece_info_at(state:Dictionary,location:String)->Dictionary:
	var answer={
		"team":null,
		"name":null,
		"type":null,
	}
	for team in state:
		for piece in state[team]:
			if (state[team][piece] ==location):
				answer["team"]=team
				answer["name"]=piece
				if(piece.to_upper()=="KING"):
					answer["type"]="king"
				else:
					answer["type"]=piece.rstrip(piece[piece.length()-1]).to_lower()
				return answer
	return answer
	
func get_piece(team:String,name:String)->Node:
	var path ="Chess"
	if(team.to_upper()=="BLACK"):
		path =path + "Black/"
	elif(team.to_upper()=="WHITE"):
		path = path + "White/"
	else:
		return null
	if(name.to_upper()=="KING"):
		path = path + name.capitalize() +team.capitalize()
	else:
		path = path + name.rstrip(name[name.length()-1]).capitalize() +team.capitalize() + name[name.length()-1]
	return get_node(path)
	
func get_location(name:String)->Node:
	var path = "ChessLocation/"+name[0] +'/'+name
	return get_node(path)
	
#MOVING A PIECES, it can 
func move_pieces_to(location:String)->bool:
	var piece_info = get_piece_info_at(state,self.is_selected_piece.location)
	var piece =get_piece(piece_info["team"],piece_info["name"])
	var node = get_location(location)
	piece.set_position(node.get_position())
	update_state(location)
	return true

func attack(location:String)->bool:
#	prevent attack itself
	if(location == self.is_selected_piece.location):
		return false
	else:
	#	delete pieces at destination location
		var pieces_will_be_deleted = get_piece_info_at(state,location)
		get_piece(pieces_will_be_deleted["team"],pieces_will_be_deleted["name"]).queue_free();
	#	move selected piece to destination location
		var piece = get_piece_info_at(state,self.is_selected_piece.location)
		move_pieces_to(location)
		self.state[pieces_will_be_deleted.team].erase(pieces_will_be_deleted.name)
		update_state(location)
		return true

func action_execute(turn:String,location:String)->bool:
	hide_movable()
	if(self.is_selected):
		if(location in moveable):
			if(is_location_empty(state,location)):
				move_pieces_to(location)
				reset_select()
				trigger_moveable()
				$Action.text = "Move"
				return true
			else:
				attack(location)
				reset_select()
				trigger_moveable()
				$Action.text = "Invade"
				return true
		else:
			if(is_location_empty(state,location)):
				reset_select()
				trigger_moveable()
				$Action.text = "Select Nothing"
			else:
				if(get_piece_info_at(state,location)["team"]==turn):
					select_piece_at(location)
					is_selected = true
					var temp = generate_next_move(location)
					trigger_moveable(temp)
					$Action.text = "Select: "+String(location)
	else:
		if(is_location_empty(state,location)):
			reset_select()
			trigger_moveable()
			$Action.text = "Select Nothing"
		else:
			if(get_piece_info_at(state,location)["team"]==turn):
				select_piece_at(location)
				is_selected = true
				var temp = generate_next_move(location)
				trigger_moveable(temp)
				$Action.text = "Select: "+String(location)
			
	return false

func initial_state()->void:
	$ChessBlack.set_visible(true)
	$ChessWhite.set_visible(true)
	for team in state:
		for piece in state[team]:
			select_piece_at(state[team][piece])
			move_pieces_to(state[team][piece])
	reset_select()
	return

func _on_location_select(location:String):
	if(whiteTurn):
		if(action_execute("white",location)):
			whiteTurn=false
			blackTurn=true
			$Notification.text="NOW IS THE BLACK TURN"
			$State.text=String(self.state)
			check_win_and_next_move()
		return
#	if(blackTurn):
#		black_team_call()
#		if(action_execute("black",location)):
#			whiteTurn=true
#			blackTurn=false
#			$Notification.text="NOW IS THE WHITE TURN"
##			$State.text=String(self.state)
##			$Selected_piece.text=String(is_selected_piece)
#			return
	pass
	
func generate_server_data()->String:
	var temp_state = {
	"\"white\"": {
		"\"pawn\"": [],
		"\"knight\"": [],
		"\"bishop\"": [],
		"\"rook\"": [],
		"\"queen\"": [],
		"\"king\"": [],
	},
	"\"black\"": {
		"\"pawn\"": [],
		"\"knight\"": [],
		"\"bishop\"": [],
		"\"rook\"": [],
		"\"queen\"": [],
		"\"king\"": [],
	}
	}
	for team in self.state:
		for piece in self.state[team]:
			var queryteam = String("\""+team+"\"")
			var loc = "\""+self.state[team][piece] +"\""
			if 'pawn'in piece:
				temp_state[queryteam]["\"pawn\""].append(loc)
			elif 'knight' in piece:
				temp_state[queryteam]["\"knight\""].append(loc)
			elif 'bishop' in piece:
				temp_state[queryteam]["\"bishop\""].append(loc)
			elif 'rook' in piece:
				temp_state[queryteam]["\"rook\""].append(loc)
			elif 'queen' in piece:
				temp_state[queryteam]["\"queen\""].append(loc)
			elif 'king' in piece:
				temp_state[queryteam]["\"king\""].append(loc)
			else:
				pass
#	$State.text = String(temp_state)..,,
	return JSON.print(String(temp_state).replace("...",""))
	
func connect_button()->void:
	var test = {
		"A":6,
		"B":7,
		"C":8,
		"D":9,
		"E":10,
		"F":9,
		"G":8,
		"H":7,
		"I":6
	}
	for ele in test:
		for number in range(1,test[ele]+1):
			var s = "ChessLocation/"+ele+"/"+ele+String(number)
			get_node(s).connect("pressed",self,"_on_location_select",[ele+String(number)])
	$make_request.connect("pressed",self,"_on_make_request")
	return
	
# Called when the node enters the scene tree for the first time.
func _ready():
	initial_state()
	connect_button()
	show_movable()
	$Notification.text="NOW IS THE WHITE TURN"
	$HTTPRequest.connect("request_completed", self, "_on_black_moves_completed")
	$HTTPRequest2.connect("request_completed", self, "_on_check_win_completed")
	$HTTPRequest3.connect("request_completed", self, "_on_check_win_and_next_move_completed")
	pass # Replace with function body.

func _on_TextureButton_pressed():
	get_tree().change_scene("res://Scenes/IntroWindown.tscn")
	pass # Replace with function body.

func _on_make_request():
	pass
#	black_moves()

func _on_check_win_and_next_move_completed(result, response_code, headers, body):
	var json_response = JSON.parse(String(body.get_string_from_ascii()))
	if(json_response.error== OK):
		var ans = json_response.result["winner"]
		if(ans =="not yet"):
			black_moves()
		else:
			win(ans)
	pass

func _on_check_win_completed(result, response_code, headers, body):
	var json_response = JSON.parse(String(body.get_string_from_ascii()))
	if(json_response.error== OK):
		var ans = json_response.result["winner"]
		if(ans =="not yet"):
			pass
		else:
			win(ans)
	pass

func _on_black_moves_completed(result, response_code, headers, body):
	var json_response = JSON.parse(String(body.get_string_from_ascii()))
	if(json_response.error== OK):
		if(json_response.result.has('black_move')):
			var move:String = json_response.result["black_move"]
			var original = move.split("->")[0]
			var destination = move.split("->")[1]
			action_execute('black',original)
			action_execute('black',destination)
			whiteTurn=true
			blackTurn=false
			check_win()
			$Notification.text="NOW IS THE WHITE TURN"
			$State.text = move
			
	else:
		pass
		$State.text = 'BUG'
		
#	$Action.text = String(self.state["white"]["king"])
	
func black_moves():
	var url = 'http://localhost:5000/move'
	var data = generate_server_data()
	var headers = ["Content-Type: application/json"]
	$HTTPRequest.request(url,headers,false,HTTPClient.METHOD_POST,data)
	
func check_win():
	var url = 'http://localhost:5000/checkwin'
	var data = generate_server_data()
	$State.text = String(data)
	var headers = ["Content-Type: application/json"]
	$HTTPRequest2.request(url,headers,false,HTTPClient.METHOD_POST,data)
	
func check_win_and_next_move():
	var url = 'http://localhost:5000/checkwin'
	var data = generate_server_data()
	$State.text = String(data)
	var headers = ["Content-Type: application/json"]
	$HTTPRequest3.request(url,headers,false,HTTPClient.METHOD_POST,data)

func win(team:String):
	$PopupDialog/State.text = team + 'WIN'
#	$ChessBlack.hide()
#	$ChessWhite.hide()
	$PopupDialog.show()
	$PopupDialog.popup()
