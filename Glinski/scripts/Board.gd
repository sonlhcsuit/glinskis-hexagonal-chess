extends TextureRect


var default_state:Array = [0, 0, 0, 0, 0, 0, 12, 9, 0, 0, 0, 17, 20, 10, 0, 9, 0, 0, 17, 0, 18, 13, 0, 0, 9, 0, 17, 0, 0, 21, 11, 11, 11, 0, 9, 17, 0, 19, 19, 19, 14, 0, 0, 9, 0, 17, 0, 0, 22, 10, 0, 9, 0, 0, 17, 0, 18, 12, 9, 0, 0, 0, 17, 20, 0, 0, 0, 0, 0, 0]
var PIECES = 'pnbrqk//PNBRQK//'

var state = [0, 0, 0, 0, 0, 0, 12, 9, 17, 0, 0, 17, 20, 10, 0, 9, 0, 0, 17, 0, 18, 13, 0, 0, 9, 0, 17, 0, 0, 21, 11, 11, 11, 0, 9, 17, 0, 19, 19, 19, 14, 0, 0, 9, 0, 17, 0, 0, 22, 10, 0, 9, 0, 0, 17, 0, 18, 12, 9, 0, 0, 0, 17, 20, 0, 0, 0, 0, 0, 0]

var knight_set = [
	[5,1],
	[0,2],
	[1,3],
	[2,4],
	[3,5],
	[4,0],
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

func neighbor(board_number: int) -> Array:
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

func legal_slot(slot:int,white:bool)->bool:
	if slot == 0:
		return false
	if state[slot - 1] == 0:
		return true
	if white:
#		must be black piece
		return state[slot - 1] > 16 
	else:
#		must be white piece
		return state[slot -1 ] > 8 and state[slot -1 ] < 16

func knight_move(slot_value:int,state:Array,white:bool)-> Array:
	var moves = []
	var neighbors = neighbor(slot_value)
	for i in range(6):
		if neighbors[i] != 0:
			var n = neighbor(neighbors[i])[i]
			if n != 0:
				var offset = neighbor(n)
				var move_1 = offset[knight_set[i][0]]
				var move_2 = offset[knight_set[i][1]]
				if legal_slot(move_1,white):
					moves.append(move_1)
				if legal_slot(move_2,white):
					moves.append(move_2)
	return moves

func next_move_of_piece(slot_value:int,state:Array) -> Array:
	if len(state) != 70 or slot_value > 70 :
		assert(false,"State of the game is not valid")
	var piece_value = state[slot_value -1]
	var next_moves:Array = []
	var white = true
	var moves = []
	
	if piece_value > 16 :
		piece_value = piece_value - 16
		white = false
	else:
		piece_value = piece_value - 8
		
	if piece_value == 1:
#		pawn next moves
		var neighbors = neighbor(slot_value)
		log_message(String(neighbors))
		if white:
			var top = neighbors[0]
			var top_left = neighbors[1]
			var top_right = neighbors[5]
			if state[top-1] == 0:
				moves.append(top)
			if state[top_left-1] - 16 > 0 :
				moves.append(top_left)
			if state[top_right-1] -16 > 0:
				moves.append(top_right) 
		else:
			var bottom = neighbors[3]
			var bottom_left = neighbors[4]
			var bottom_right = neighbors[2]
			if state[bottom-1] == 0:
				moves.append(bottom)
			if state[bottom_left-1] > 8  and state[bottom_left-1] < 16:
				moves.append(bottom_left)
			if state[bottom_right-1] > 8 and state[bottom_right-1] < 16   :
				moves.append(bottom_right)
	elif piece_value == 2:
#		knight
		moves = knight_move(slot_value,state,white)
	elif piece_value == 3:
		pass
	elif piece_value == 4:
		pass
	elif piece_value == 5:
		pass
	elif piece_value == 6:
		pass
	return moves

func next_move_of(pos):
	
	var moves = next_move_of_piece(pos,state)
	for move in moves:
		var path_str = "Slots/Slot{i}".format({"i":move})
		var slot:TextureButton = get_node(path_str)
		if slot.has_method("trigger_image"):
			slot.trigger_image()


func create_piece(value:int)->TextureRect:
	var resource = piece_resources[value]
	var texture = load(resource)
	var piece:TextureRect = TextureRect.new()
	piece.set_texture(texture)
	piece.set_size(texture.get_size())
	piece.set_scale(Vector2(0.5,0.5))
	return piece
	
func render_state(state:Array)->void:
	
	for i in range(len(state)):
		if state[i]!=0:
			var piece = create_piece(state[i])
			var path_str = "Slots/Slot{i}".format({"i":i+1})
			var slot:TextureButton = get_node(path_str)
			slot.connect("pressed",self,"next_move_of",[i+1])
			move_to_slot(piece,slot)
			$Pieces.add_child(piece)
	
func move_to_slot(piece:TextureRect, slot:TextureButton):
	var slot_position:Vector2 = slot.get_position()
	var slot_size:Vector2 = slot.get_size()
	var piece_size:Vector2 = piece.get_size() * piece.get_scale()
	
	var newpos = Vector2(
		slot_position.x - (piece_size.x - slot_size.x)/2,
		slot_position.y - (piece_size.y - slot_size.y)/2
		)
	piece.set_position(newpos)
	
	
func arrange_slots():
	var index = 1
	for file_offset in file_offsets:
		var x_offset = file_offset[1]
		var y_offset = file_offset[2]
		for _i in range(file_offset[0]):
			var path = "Slots/Slot{i}".format({"i":index})
			var btn: TextureButton= get_node(path)
			btn.set_position(Vector2(x_offset,y_offset))
			index = index + 1
			y_offset = y_offset - 80
			

# Called when the node enters the scene tree for the first time.
func _ready():
	arrange_slots()
	state[25] = 10
	render_state(state)
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
