extends Node2D

signal open_setting
signal start_game
signal open_guide
signal save_setting
signal back_intro

func _on_Quit_pressed():
	get_tree().quit()
	pass # Replace with function body.

func _on_Start_pressed():
	emit_signal("start_game")

func _on_About_pressed():
	$CenterContainer/Dialog.popup(Rect2( 0, 0, 0, 0 ))
	pass # Replace with function body.


func _on_Guide_pressed():
	emit_signal("open_guide")
