extends TextureButton

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

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

func node_name():
	return str(name.replace("@", "").replace(str(int(name)), ""))
	
func drop_data(position, data):
	var board = get_node("/root/Main/CenterContainer/Board")

	if board.has_method("move_to_slot"):
		board.move_to_slot(data["piece"],self)

func can_drop_data(position, data):
	return true



