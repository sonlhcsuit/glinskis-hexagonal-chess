extends TextureButton


# Declare member variables here. Examples:
# var a = 2
# var b = "text"
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


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


