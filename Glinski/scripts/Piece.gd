extends TextureRect
class_name Piece


var knight_set = [
	[5,1],
	[0,2],
	[1,3],
	[2,4],
	[3,5],
	[4,0],
]
var bishop_set = [
	[0,1],
	[0,5],
	[2,1],
	[2,3],
	[4,3],
	[4,5]
]

## columns offets
var file_offsets = [
	[6,35,570],
	[7,105,610],
	[8,175,650],
	[9,245,690],
	[10,315,730],
	[9,385,690],
	[8,455,650],
	[7,525,610],
	[6,595,570],
]
func get_neighbors_of(board_number: int) -> Array:
	if not (0 < board_number and board_number < 71):
		assert(false,"Board number are not valid, must in the range [1,70]")
	var result = [board_number,board_number,board_number,board_number,board_number,board_number ]
	var key_values = [65, 58, 50, 41, 31, 22, 14, 7, 1]
	var offset = [
		[1, 6, 5, -1, -7, -6],
		[1, 7, 6, -1, -8, -7],
		[1, 8, 7, -1, -9, -8],
		[1, 9, 8, -1, -10, -9],
		[1, 10, 9, -1, -10, -9],
		[1, 10, 9, -1, -9, -8],
		[1, 9, 8, -1, -8, -7],
		[1, 8, 7, -1, -7, -6],
		[1, 7, 6, -1, -6, -5],
	]
	for i in range(len(key_values)):
		
		if board_number >= key_values[i]:
			var off = offset[i]
			
			for j in range(len(result)):
				result[j] = result[j] + off[j] 
				
			if board_number == 40:
				result[0] = 0
				result[1] = 0
				result[5] = 0
			elif board_number == 31:
				result[2] = 0
				result[3] = 0
				result[4] = 0
			elif board_number == key_values[i] and board_number < 31:
				result[3] = 0
				result[4] = 0
			elif board_number == key_values[i] and board_number > 31:
				result[2] = 0
				result[3] = 0
			elif board_number == key_values[i - 1] - 1 and board_number < 40:
				result[0] = 0
				result[5] = 0
			elif board_number == key_values[i - 1] - 1 and board_number > 40:
				result[0] = 0
				result[1] = 0
				
			for k in range(len(result)):
				if not (0 <= result[k] and result[k] <= 70):
					result[k] = 0
				
			break
	return result


func log_message(message:String)->void:
	$Label.text = message
#
#func legal_slot(slot:int,white:bool)->bool:
#	if slot == 0:
#		return false
#	if state[slot - 1] == 0:
#		return true
#	if white:
##		must be black piece
#		return state[slot - 1] > 16 
#	else:
##		must be white piece
#		return state[slot -1 ] > 8 and state[slot -1 ] < 16
#
#func knight_move(slot_value:int,state:Array,white:bool)-> Array:
#	var moves = []
#	var neighbors = get_neighbors_of(slot_value)
#	for i in range(6):
#		if neighbors[i] != 0:
#			var n = get_neighbors_of(neighbors[i])[i]
#			if n != 0:
#				var offset = get_neighbors_of(n)
#				var move_1 = offset[knight_set[i][0]]
#				var move_2 = offset[knight_set[i][1]]
#				if legal_slot(move_1,white):
#					moves.append(move_1)
#				if legal_slot(move_2,white):
#					moves.append(move_2)
#	return moves
#
#func bishop_move(slot_value:int,state:Array,white:bool)-> Array:
#	var moves = []
#	for direction in bishop_set:
#		var slot = slot_value
#		while true:
#			var neighbors = get_neighbors_of(slot) 
#			if neighbors[direction[0]] != 0 :
#				var move = get_neighbors_of(neighbors[direction[0]])[direction[1]]
#				if legal_slot(move,white):
#					moves.append(move)
#					slot = move
#					if state[move - 1] !=0:
#						break
##					if state[move] != 0:
##						break
#
#				else:
#					break
#			else:
#				break
#	return moves
#
#func next_move_of_piece(slot_value:int,state:Array) -> Array:
#	if len(state) != 70 or slot_value > 70 :
#		assert(false,"State of the game is not valid")
#	var piece_value = state[slot_value -1]
#	var next_moves:Array = []
#	var white = true
#	var moves = []
#
#	if piece_value > 16 :
#		piece_value = piece_value - 16
#		white = false
#	else:
#		piece_value = piece_value - 8
#
#	if piece_value == 1:
##		pawn next moves
#		var neighbors = get_neighbors_of(slot_value)
#		log_message(String(neighbors))
#		if white:
#			var top = neighbors[0]
#			var top_left = neighbors[1]
#			var top_right = neighbors[5]
#			if state[top-1] == 0:
#				moves.append(top)
#			if state[top_left-1] - 16 > 0 :
#				moves.append(top_left)
#			if state[top_right-1] -16 > 0:
#				moves.append(top_right) 
#		else:
#			var bottom = neighbors[3]
#			var bottom_left = neighbors[4]
#			var bottom_right = neighbors[2]
#			if state[bottom-1] == 0:
#				moves.append(bottom)
#			if state[bottom_left-1] > 8  and state[bottom_left-1] < 16:
#				moves.append(bottom_left)
#			if state[bottom_right-1] > 8 and state[bottom_right-1] < 16   :
#				moves.append(bottom_right)
#	elif piece_value == 2:
##		knight
#		moves = knight_move(slot_value,state,white)
#	elif piece_value == 3:
##		bishop
#		moves = bishop_move(slot_value,state,white)
#	elif piece_value == 4:
#		pass
#	elif piece_value == 5:
#		pass
#	elif piece_value == 6:
#		pass
#	return moves
#

var _value:int = 0
var piece_resources:Dictionary = {
9:"res://sprites/pawn.tres",
10:"res://sprites/knight.tres",
11:"res://sprites/bishop.tres",
12:"res://sprites/rook.tres",
13:"res://sprites/queen.tres",
14:"res://sprites/king.tres",
17:"res://sprites/pawn_b.tres",
18:"res://sprites/knight_b.tres",
19:"res://sprites/bishop_b.tres",
20:"res://sprites/rook_b.tres",
21:"res://sprites/queen_b.tres",
22:"res://sprites/king_b.tres"
}
func _init(value):
	self._value = value
	load_resources()

func set_value(value:int)->void:
	self._value = value
	load_resources()
	
func get_value()->int:
	return self._value
	
func load_resources():
	var resource = piece_resources[self._value]
	var texture = load(resource)
	self.set_texture(texture)
	self.set_size(texture.get_size())
	self.set_scale(Vector2(0.5,0.5))
	
# Drag & Drop setting up

func get_drag_data(position):
	#	create drag texture (for preview)
	var drag_texture = TextureRect.new()
	drag_texture.texture = texture
	drag_texture.expand = true
	drag_texture.rect_size = texture.get_size()
	drag_texture.set_scale(Vector2(0.5,0.5))
	var control = Control.new()
	control.add_child(drag_texture)
	drag_texture.rect_position = -0.25 *drag_texture.rect_size
	set_drag_preview(control)
	
	var data = {
		"piece":self
	}
	return data

func can_drop_data(position, data):
	return true
	
func drop_data(position, data):
	var board = get_node("/root/Main/CenterContainer/Board")
	if board.has_method("log_message"):
		board.log_message("eat!!!!")
	if board.has_method(""):
		pass
