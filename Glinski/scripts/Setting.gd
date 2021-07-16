extends Node2D
signal open_setting
signal start_game
signal open_guide
signal save_setting(setting)
signal back_to_intro

var setting:Dictionary
onready var diff = $CenterContainer/VBoxContainer/VBoxContainer/Difficulty	
onready var mode = $CenterContainer/VBoxContainer/VBoxContainer/Mode
onready var server = $CenterContainer/VBoxContainer/VBoxContainer/server

func set_setting(setting:Dictionary):
	self.setting = setting
	render_setting()
	
func get_setting():
	return self.setting

func render_setting():
	if self.setting["difficulty"] == null:
		diff.select(0)
		mode.select(0)		
		diff.disabled = true
	else:
		diff.select(self.setting["difficulty"])
		mode.select(1)
	server.text = self.setting["url"]
func _ready():
	mode.add_item("Pass and play",0)
	mode.add_item("adversarial ai",1)
	diff.add_item("Noob",0)
	diff.add_item("easy",1)
	diff.add_item("medium",2)
	diff.add_item("hard",3)
	diff.add_item("hell",4)


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
		"difficulty":diff.selected,
		"url":server.text
	}
	if mode.selected == 0:
		data["difficulty"] = null

	emit_signal("save_setting",data)


func _on_BackButton_pressed():
	emit_signal("back_to_intro")


