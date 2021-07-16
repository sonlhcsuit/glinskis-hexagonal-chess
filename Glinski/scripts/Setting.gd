extends Node2D
signal back_to_intro
signal save_setting(setting)
# Called when the node enters the scene tree for the first time.
func _ready():
	var diff = $CenterContainer/VBoxContainer/VBoxContainer/Difficulty	
	var mode = $CenterContainer/VBoxContainer/VBoxContainer/Mode
	var server = $CenterContainer/VBoxContainer/VBoxContainer/server
	mode.add_item("Pass and play",0)
	mode.add_item("adversarial ai",1)
	mode.select(1)
	diff.add_item("Noob",0)
	diff.add_item("easy",1)
	diff.add_item("medium",2)
	diff.add_item("hard",3)
	diff.add_item("hell",4)
	diff.select(1)
	server.text = "http:127.0.0.1:5000/"

func _on_Mode_item_selected(index):
	var diff = $CenterContainer/VBoxContainer/VBoxContainer/Difficulty	
	if index == 0:
		diff.disabled = true
	else:
		diff.disabled=false


func _on_Save_pressed():
	var diff = $CenterContainer/VBoxContainer/VBoxContainer/Difficulty	
	var mode = $CenterContainer/VBoxContainer/VBoxContainer/Mode
	var server = $CenterContainer/VBoxContainer/VBoxContainer/server
	var data = {
		"mode":mode.selected,
		"difficulty":diff.selected,
		"url":server.text
	}
	if mode.selected == 0:
		data["difficulty"] = null
		
	emit_signal("save_setting",data)


func _on_BackButton_pressed():
	emit_signal("back_to_intro")


