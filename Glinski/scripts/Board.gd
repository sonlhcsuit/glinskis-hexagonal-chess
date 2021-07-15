extends TextureRect
var default_state:Array = [0, 0, 0, 0, 0, 0, 12, 9, 0, 0, 0, 17, 20, 10, 0, 9, 0, 0, 17, 0, 18, 13, 0, 0, 9, 0, 17, 0, 0, 21, 11, 11, 11, 0, 9, 17, 0, 19, 19, 19, 14, 0, 0, 9, 0, 17, 0, 0, 22, 10, 0, 9, 0, 0, 17, 0, 18, 12, 9, 0, 0, 0, 17, 20, 0, 0, 0, 0, 0, 0]
var PIECES = 'pnbrqk//PNBRQK//'

var Piece = load("res://scripts/Piece.gd")

var state = [0, 0, 0, 0, 0, 0, 12, 9, 0, 0, 0, 17, 20, 10, 0, 9, 0, 0, 17, 0, 18, 13, 0, 0, 9, 0, 17, 0, 0, 21, 11, 11, 11, 0, 9, 17, 0, 19, 19, 19, 14, 0, 0, 9, 0, 17, 0, 0, 22, 10, 0, 9, 0, 0, 17, 0, 18, 12, 9, 0, 0, 0, 17, 20, 0, 0, 0, 0, 0, 0]
var available_moves = []

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

func get_state()->Array:
	return self.state

func set_state(state:Array)->void:
	self.state = state

func set_available_moves(available_moves:Array)->void:
	self.available_moves=available_moves
	
func get_available_moves()->Array:
	return available_moves


func log_message(message:String)->void:
	$Label.text = message

func preview_moves():
	for move in self.available_moves:
		if move != 0:
			var path_str = "Slots/Slot_{i}".format({"i":move})
			var slot:TextureButton = get_node(path_str)
			if slot.has_method("trigger"):
				slot.trigger(true)
	
func clear_preview_moves()->void:
	for i in range(0,70):
		var path_str = "Slots/Slot_{i}".format({"i":i+1})
		var slot:TextureButton = get_node(path_str)
		if slot.has_method("trigger"):
			slot.trigger(false)

	
func create_piece(value:int)->TextureRect:
	return Piece.new(value)
	
func render_state(state:Array)->void:
	self.remove_child($Pieces)
	var pieces_container = Node2D.new()
	pieces_container.name = "Pieces"
	for i in range(len(state)):
		if state[i]!=0:
			var piece = create_piece(state[i])
			var path_str = "Slots/Slot_{i}".format({"i":i+1})
			var slot:TextureButton = get_node(path_str)
			stick_piece_with_slot(piece,slot)
			pieces_container.add_child(piece)
	self.add_child(pieces_container)
	
# make sure the move is LEGAL
func move(from, to)->void:
	if from < 0 or from > 70:
		assert(false, "Move are illegal")
	if from < 0 or from > 70:
		assert(false, "Move are illegal")
	if from == to :
		return
	self.state[to-1] = self.state[from-1]
	self.state[from-1]=0
	self.render_state(state)

func stick_piece_with_slot(piece:Piece, slot:Slot):
	var slot_position:Vector2 = slot.get_position()
	var slot_size:Vector2 = slot.get_size()
	var piece_size:Vector2 = piece.get_size() * piece.get_scale()
	
	var newpos = Vector2(
		slot_position.x - (piece_size.x - slot_size.x)/2,
		slot_position.y - (piece_size.y - slot_size.y)/2
		)
	piece.set_position(newpos)
	piece.set_slot(slot.get_slot())

	
func arrange_slots():
	var index = 1
	for file_offset in file_offsets:
		var x_offset = file_offset[1]
		var y_offset = file_offset[2]
		for _i in range(file_offset[0]):
			var path = "Slots/Slot_{i}".format({"i":index})
			var btn: TextureButton= get_node(path)
			btn.set_position(Vector2(x_offset,y_offset))
			index = index + 1
			y_offset = y_offset - 80
			

# Called when the node enters the scene tree for the first time.
func _ready():
	self.arrange_slots()
	state[54-1] = 14
	self.render_state(self.state)
#	var t = []
#	for i in range(0,70):
#		t.append(0)
#	t[54-1]=12
#	state = t
#	render_state(t)
	pass # Replace with function body.
	
func _input(event):
	if event is InputEventMouseButton and not event.is_pressed():
	   self.clear_preview_moves()
