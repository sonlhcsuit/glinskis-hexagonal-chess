extends TextureRect
class_name Piece

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
	var data = {
		"value":self._value,
		"texture": load(piece_resources[self._value]),
		"piece":self
		
	}
	var drag_texture = TextureRect.new()
	drag_texture.texture = texture
	drag_texture.expand = true
	drag_texture.rect_size = texture.get_size()
	drag_texture.set_scale(Vector2(0.5,0.5))
	
	var control = Control.new()
	control.add_child(drag_texture)
	drag_texture.rect_position = -0.25 *drag_texture.rect_size
	set_drag_preview(control)
	
	return data

