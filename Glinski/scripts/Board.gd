extends TextureRect

var PIECES = 'pnbrqk//PNBRQK//'
var defaul_state = [0, 0, 0, 0, 0, 0, 12, 9, 0, 0, 0, 17, 20, 10, 0, 9, 0, 0, 17, 0, 18, 13, 0, 0, 9, 0, 17, 0, 0, 21, 11, 11, 11, 0, 9, 17, 0, 19, 19, 19, 14, 0, 0, 9, 0, 0, 17, 0, 22, 10, 0, 9, 0, 0, 0, 17, 18, 12, 9, 0, 0, 0, 17, 20, 0, 0, 0, 0, 0, 0]

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


# Called when the node enters the scene tree for the first time.

func create_piece(value:int)->TextureRect:
	var resource = piece_resources[value]
	var texture = load(resource)
	var piece:TextureRect = TextureRect.new()
	piece.set_texture(texture)
	piece.set_size(texture.get_size())
	piece.set_scale(Vector2(0.5,0.5))
	return piece
	

func move_to_slot(piece:TextureRect, slot:TextureButton):
	var slot_position:Vector2 = slot.get_position()
	var slot_size:Vector2 = slot.get_size()
	var piece_size:Vector2 = piece.get_size() * piece.get_scale()
	
	var newpos = Vector2(
		slot_position.x - (piece_size.x - slot_size.x)/2,
		slot_position.y - (piece_size.y - slot_size.y)/2
		)
	piece.set_position(newpos)
	pass
func arrange_slots():
	var index = 1
	for file_offset in file_offsets:
		var x_offset = file_offset[1]
		var y_offset = file_offset[2]
		for _i in range(file_offset[0]):
			var path = "Slots/Slot{i}".format({"i":index})
#			var btn: Button = get_node(path)
			var btn: TextureButton= get_node(path)
			
#			btn.text = str(index)
			btn.set_position(Vector2(x_offset,y_offset))
			index = index + 1
			y_offset = y_offset - 80
			

func _ready():
	arrange_slots()
	
	var piece = create_piece(9)
	move_to_slot(piece,$Slots/Slot1)
	$Pieces.add_child(piece)
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
