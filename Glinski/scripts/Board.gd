extends TextureRect

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



# Called when the node enters the scene tree for the first time.

func move(piece,slot):
	pass
func arrange_slots():
	var index = 1
	for file_offset in file_offsets:
		var x_offset = file_offset[1]
		var y_offset = file_offset[2]
		for _i in range(file_offset[0]):
			var path = "Slots/Slot{i}".format({"i":index})
			var btn: Button = get_node(path)
			btn.text = str(index)
			btn.set_position(Vector2(x_offset,y_offset))
			index = index + 1
			y_offset = y_offset - 80
			

func _ready():
	arrange_slots()
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
