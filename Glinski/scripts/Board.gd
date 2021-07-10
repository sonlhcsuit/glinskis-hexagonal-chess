extends TextureRect


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	var x: float = 35
	var y: float = 570
	for i in range(1,6):
		var path = "Slots/Slot{index}".format({"index":i})
		var node:Button = get_node(path)
		get_node("Slots/Slot1")
		node.set_position(Vector2(x,y))
		y=y-80
		
	
	
	
	
	
	
	
	
	
	
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
