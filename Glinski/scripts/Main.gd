extends Node2D
#########################################################
#				Setting up board pieces                #
#########################################################

var setting:Dictionary ={}
var is_autoplay:bool = true
var level:int = 1
var is_waiting = false
signal open_setting
signal start_game
signal open_guide
signal save_setting
signal back_to_intro

func get_board():
	return get_node("/root/Game/Main/CenterContainer/Board")

func set_setting(setting):
	self.setting = setting

func get_setting(setting):
	return self.setting

func random_move()->Array:
	var board = get_board()
	var state = board.get_state()
	var moves = []
	var log_String = String(state)
	for slot_index in range(1,71):
		var slot_value = state[slot_index-1]
		if slot_value > 16:
			var next_moves = Piece.next_move_of_piece(slot_index,state)
			for m in next_moves:
				moves.append([slot_index,m])
	var l = len(moves)
	var rng = RandomNumberGenerator.new()
	return moves[rng.randi_range(0,l-1)]


func _on_BackButton_pressed():
	emit_signal("back_to_intro")

func _process(delta):
	var board = self.get_board()
	if not is_waiting and self.setting["difficulty"] != null and not board.is_white_turn():
		var notation= board.encode_notation(board.get_state())
		minimax(notation)
	pass

func _ready():
	$Request.connect("request_completed", self, "_on_request_completed")
	

func minimax(notation):
	var url = self.setting["url"] + "minimax"
	var headers = ["Content-Type: application/json"]
	var data = {
		"notation":notation
	}
	$Request.request(url,headers,false, HTTPClient.METHOD_POST,JSON.print(data))
	self.is_waiting = true

func _on_request_completed(result, response_code, headers, body):
	$Label.text = body.get_string_from_utf8()
	var json = JSON.parse(body.get_string_from_utf8())
	if json.error == OK:
		var move = json.result["move"]
		var board = get_board()
		board.move(int(move[0]),int(move[1]))
		self.is_waiting = false
	else:
#		$Label.text = "BUG"
		pass
		


























#	var board = get_board()
#	if is_autoplay and not board.is_white_turn():
#		var move = random_move()
#		board.move(move[0],move[1])
	
##+++++++++++++SHOW NEXT POSSIBLE MOVE AS RED DOT++++++#
#func set_moveable(new_moveable:Array)->void:
#	self.moveable = new_moveable
#	return
#
#func reset_movable()->void:
#	self.moveable = [];
#	return
#
#func show_movable()->void:
#	if(self.moveable.empty()):
#		return
#	for location in self.moveable:
#		var temp_node = get_location(location)
#		var texture = temp_node.get_focused_texture()
#		temp_node.set_normal_texture(texture)
#	return
#
#func hide_movable()->void:
#	for location in self.moveable:
#		var temp_node = get_location(location)
#		temp_node.set_normal_texture(null)
#	return
#
#func trigger_moveable(new_move:Array=[])->void:
#	if(self.is_selected):
#		set_moveable(new_move)
#		show_movable()
#	else:
#		hide_movable()
#		reset_movable()
#	return
#
##++++++++++++++++++++SELECT MOVE ++++++++++++++++++++++++#
#func reset_select()->void:
#	self.is_selected = false
#	self.is_selected_piece= {
#	"team":"",
#	"name":"",
#	"type":"",
#	"location":"",
#	}
#	return
#
#func update_state(newpos)->void:
#	self.state[self.is_selected_piece.team][self.is_selected_piece.name]=newpos
#	return
#
#func select_piece_at(location:String)->void:
#	if(is_location_empty(state,location)):
#		return
#	else:
#		var piece = get_piece_info_at(self.state,location)
#		self.is_selected_piece["team"]=piece["team"]
#		self.is_selected_piece["name"]=piece["name"]
#		self.is_selected_piece["type"]=piece["type"]
#		self.is_selected_piece["location"]=location
#	return
#
#func get_piece_info_at(state:Dictionary,location:String)->Dictionary:
#	var answer={
#		"team":null,
#		"name":null,
#		"type":null,
#	}
#	for team in state:
#		for piece in state[team]:
#			if (state[team][piece] ==location):
#				answer["team"]=team
#				answer["name"]=piece
#				if(piece.to_upper()=="KING"):
#					answer["type"]="king"
#				else:
#					answer["type"]=piece.rstrip(piece[piece.length()-1]).to_lower()
#				return answer
#	return answer
#
#func get_piece(team:String,name:String)->Node:
#	var path ="Chess"
#	if(team.to_upper()=="BLACK"):
#		path =path + "Black/"
#	elif(team.to_upper()=="WHITE"):
#		path = path + "White/"
#	else:
#		return null
#	if(name.to_upper()=="KING"):
#		path = path + name.capitalize() +team.capitalize()
#	else:
#		path = path + name.rstrip(name[name.length()-1]).capitalize() +team.capitalize() + name[name.length()-1]
#	return get_node(path)
#
#func get_location(name:String)->Node:
#	var path = "ChessLocation/"+name[0] +'/'+name
#	return get_node(path)
#
##MOVING A PIECES, it can 
#func move_pieces_to(location:String)->bool:
#	var piece_info = get_piece_info_at(state,self.is_selected_piece.location)
#	var piece =get_piece(piece_info["team"],piece_info["name"])
#	var node = get_location(location)
#	piece.set_position(node.get_position())
#	update_state(location)
#	return true
#
#func attack(location:String)->bool:
##	prevent attack itself
#	if(location == self.is_selected_piece.location):
#		return false
#	else:
#	#	delete pieces at destination location
#		var pieces_will_be_deleted = get_piece_info_at(state,location)
#		get_piece(pieces_will_be_deleted["team"],pieces_will_be_deleted["name"]).queue_free();
#	#	move selected piece to destination location
#		var piece = get_piece_info_at(state,self.is_selected_piece.location)
#		move_pieces_to(location)
#		self.state[pieces_will_be_deleted.team].erase(pieces_will_be_deleted.name)
#		update_state(location)
#		return true
#
#func action_execute(turn:String,location:String)->bool:
#	hide_movable()
#	if(self.is_selected):
#		if(location in moveable):
#			if(is_location_empty(state,location)):
#				move_pieces_to(location)
#				reset_select()
#				trigger_moveable()
#				$Action.text = "Move"
#				return true
#			else:
#				attack(location)
#				reset_select()
#				trigger_moveable()
#				$Action.text = "Invade"
#				return true
#		else:
#			if(is_location_empty(state,location)):
#				reset_select()
#				trigger_moveable()
#				$Action.text = "Select Nothing"
#			else:
#				if(get_piece_info_at(state,location)["team"]==turn):
#					select_piece_at(location)
#					is_selected = true
#					var temp = generate_next_move(location)
#					trigger_moveable(temp)
#					$Action.text = "Select: "+String(location)
#	else:
#		if(is_location_empty(state,location)):
#			reset_select()
#			trigger_moveable()
#			$Action.text = "Select Nothing"
#		else:
#			if(get_piece_info_at(state,location)["team"]==turn):
#				select_piece_at(location)
#				is_selected = true
#				var temp = generate_next_move(location)
#				trigger_moveable(temp)
#				$Action.text = "Select: "+String(location)
#
#	return false
#
#func initial_state()->void:
#	$ChessBlack.set_visible(true)
#	$ChessWhite.set_visible(true)
#	for team in state:
#		for piece in state[team]:
#			select_piece_at(state[team][piece])
#			move_pieces_to(state[team][piece])
#	reset_select()
#	return
#
#func ONLINE_MOVES(team:String):
#	var url = 'http://127.0.0.1:5000/move'
#	var headers = ["Content-Type: application/json"]
#	var data = generate_server_data(team)
#	$HTTPRequest.request(url,headers,false,HTTPClient.METHOD_POST,data)
#
#func _on_ONLINE_MOVES_completed(result, response_code, headers, body):
#	var json_response = JSON.parse(String(body.get_string_from_ascii()))
#	if(json_response.error== OK):
#		if(json_response.result.has('team')):
#			var move:String = json_response.result["move"]
#			var team = json_response.result["team"]
#			var original = move.split("->")[0]
#			var destination = move.split("->")[1]
#			action_execute(team.to_lower(),original)
#			action_execute(team.to_lower(),destination)
#			whiteTurn=!whiteTurn
#			blackTurn=!blackTurn
#			$State.text = team
#			check_win_and_next_move()
#	else:
#		pass
#		$State.text = 'BUG'
#
#func check_win_and_next_move():
#	var url = 'http://127.0.0.1:5000/checkwin'
#	var data = generate_server_data("WHITE")
#	$State.text = String(data)
#	var headers = ["Content-Type: application/json"]
#	$HTTPRequest3.request(url,headers,false,HTTPClient.METHOD_POST,data)
#
#func _on_check_win_and_next_move_completed(result, response_code, headers, body):
#	$State.text = String(response_code)
#	var json_response = JSON.parse(String(body.get_string_from_ascii()))
#	if(json_response.error== OK):
#		var ans = json_response.result["winner"]
#		if(ans =="not yet"):
#			autoplay()
#		else:
#			win(ans)
#	pass
#
#func autoplay():
#	if(whiteTurn):
#		ONLINE_MOVES("WHITE")
##		do the white
#	else:
#		ONLINE_MOVES("BLACK")
#
#
#func _on_location_select(location:String):
##	if(whiteTurn):
##		if(action_execute("white",location)):
##			whiteTurn=false
##			blackTurn=true
##			$Notification.text="NOW IS THE BLACK TURN"
##			$State.text=String(self.state)
##			check_win_and_next_move()
##		return
##	if(blackTurn):
##		black_team_call()
##		if(action_execute("black",location)):
##			whiteTurn=true
##			blackTurn=false
##			$Notification.text="NOW IS THE WHITE TURN"
###			$State.text=String(self.state)
###			$Selected_piece.text=String(is_selected_piece)
##			return
#	pass
#
#func generate_server_data(team:String)->String:
#	var temp_state = {
#		"\"team\"":"\""+team+"\"",
#		"\"board\"":{
#			"\"white\"": {
#				"\"pawn\"": [],
#				"\"knight\"": [],
#				"\"bishop\"": [],
#				"\"rook\"": [],
#				"\"queen\"": [],
#				"\"king\"": [],
#			},
#			"\"black\"": {
#				"\"pawn\"": [],
#				"\"knight\"": [],
#				"\"bishop\"": [],
#				"\"rook\"": [],
#				"\"queen\"": [],
#				"\"king\"": [],
#			}
#		}
#	}
#	for team in self.state:
#		for piece in self.state[team]:
#			var queryteam = String("\""+team+"\"")
#			var loc = "\""+self.state[team][piece] +"\""
#			if 'pawn'in piece:
#				temp_state["\"board\""][queryteam]["\"pawn\""].append(loc)
#			elif 'knight' in piece:
#				temp_state["\"board\""][queryteam]["\"knight\""].append(loc)
#			elif 'bishop' in piece:
#				temp_state["\"board\""][queryteam]["\"bishop\""].append(loc)
#			elif 'rook' in piece:
#				temp_state["\"board\""][queryteam]["\"rook\""].append(loc)
#			elif 'queen' in piece:
#				temp_state["\"board\""][queryteam]["\"queen\""].append(loc)
#			elif 'king' in piece:
#				temp_state["\"board\""][queryteam]["\"king\""].append(loc)
#			else:
#				pass
##	$State.text = String(temp_state)..,,
#	return JSON.print(String(temp_state).replace("...",""))
#
#func connect_button()->void:
#	var test = {
#		"A":6,
#		"B":7,
#		"C":8,
#		"D":9,
#		"E":10,
#		"F":9,
#		"G":8,
#		"H":7,
#		"I":6
#	}
#	for ele in test:
#		for number in range(1,test[ele]+1):
#			var s = "ChessLocation/"+ele+"/"+ele+String(number)
#			get_node(s).connect("pressed",self,"_on_location_select",[ele+String(number)])
#	$make_request.connect("pressed",self,"_on_make_request")
#	return
#
## Called when the node enters the scene tree for the first time.

