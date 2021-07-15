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

func get_index()->int:
	return int(name.split("_")[1])
	
func drop_data(position, data):
	var board = get_node("/root/Main/CenterContainer/Board")

	if board.has_method("move_to_slot"):
		board.move_to_slot(data["piece"],self)
	if board.has_method("log_message"):
		board.log_message("move"+ name)
	if board.has_method("clear_preview_moves"):
		board.clear_preview_moves()

func can_drop_data(position, data):
	return true



