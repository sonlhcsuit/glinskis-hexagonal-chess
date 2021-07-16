extends TextureButton
class_name Slot

var status:bool = false

func trigger(status:bool)->void:
	if self.status == status:
		return
	if status:
		var texture = load("res://sprites/circle.tres")
		set_normal_texture(texture)
	else:
		set_normal_texture(null)
	self.status = status

func trigger_image():
	trigger(not status)

func get_slot()->int:
	return int(name.split("_")[1])

func get_board():
	return get_node("/root/Main/CenterContainer/Board")


# moves are legal, update state allow piece move from slot A to slot B 
func drop_data(position, data):
	var board = get_board()
	if board.has_method("clear_preview_moves"):
		board.clear_preview_moves()
	if board.has_method("move"):
		board.move(data["slot"],get_slot())

# check if slot are droppable (legal slot for next moves)
func can_drop_data(position, data):
	var board = get_board()
	var moves = board.get_available_moves()
	var index = self.get_slot()
	if index in moves:
		return true
	return false



