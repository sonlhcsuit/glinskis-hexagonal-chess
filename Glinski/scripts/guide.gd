extends Node2D

func load_photo(path:String):
	$ColorRect.hide()
	var texture:AtlasTexture = load(path)
	$CenterContainer/GuidePhoto.texture = texture
	$CenterContainer/GuidePhoto.show()
	$CenterContainer/ChessPieces.hide()

func _on_BackButton_pressed():
	if( $CenterContainer/GuidePhoto.is_visible_in_tree()):
		hide_photo()
		$CenterContainer/ChessPieces.show()
	else:
		get_tree().change_scene("res://Scenes/Intro.tscn")


func _on_KING_pressed():
	load_photo("res://sprites/guide-sprites/king-guide.tres")

func _on_QUEEN_pressed():
	load_photo("res://sprites/guide-sprites/queen-guide.tres")

func _on_ROOK_pressed():
	load_photo("res://sprites/guide-sprites/rook-guide.tres")
	
func _on_BISHOP_pressed():
	load_photo("res://sprites/guide-sprites/bishop-guide.tres")

func _on_KNIGHT_pressed():
	load_photo("res://sprites/guide-sprites/knight-guide.tres")

func _on_PAWN_pressed():
	load_photo("res://sprites/guide-sprites/pawn-guide.tres")

func _on_DETAIL_pressed():
	$CenterContainer/PopupDialog.show()
	$CenterContainer/PopupDialog.popup()

func hide_photo():
	$CenterContainer/GuidePhoto.hide()
	$ColorRect.show()

