extends Node2D

var selected_path = ""
# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func load_photo():
	$ColorRect.hide()
	$guidePhoto.texture = load(selected_path)
	$guidePhoto.show()

func _on_back_pressed():
	if( $guidePhoto.is_visible_in_tree()):
		hide_photo()
		
	else:
		get_tree().change_scene("res://Scenes/IntroWindown.tscn")
		pass
		
#		hide_photo()
	pass # Replace with function body.


func _on_KING_pressed():
	selected_path = "res://guidePhotos/KING.png"
	load_photo()
	pass # Replace with function body.


func _on_QUEEN_pressed():
	selected_path = "res://guidePhotos/QUEEN.png"
	load_photo()
	pass # Replace with function body.


func _on_ROOK_pressed():
	selected_path = "res://guidePhotos/ROOK.png"
	load_photo()
	pass # Replace with function body.


func _on_BISHOP_pressed():
	selected_path = "res://guidePhotos/BISHOP.png"
	load_photo()
	pass # Replace with function body.


func _on_KNIGHT_pressed():
	selected_path = "res://guidePhotos/KNIGHT.png"
	load_photo()
	pass # Replace with function body.


func _on_PAWN_pressed():
	selected_path = "res://guidePhotos/PAWN.png"
	load_photo()
	pass # Replace with function body.

func hide_photo():
	$guidePhoto.hide()
	$ColorRect.show()

func _on_DETAIL_pressed():
	$PopupDialog.show()
	$PopupDialog.popup()
	pass # Replace with function body.
