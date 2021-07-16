extends Node2D
signal open_setting
signal start_game
signal open_guide
signal save_setting
signal back_to_intro
func load_photo(path:String):
	var texture:AtlasTexture = load(path)
	$CenterContainer/GuidePhoto.texture = texture
	$CenterContainer/GuidePhoto.show()
	$CenterContainer/ChessPieces.hide()

func _on_BackButton_pressed():
	if $CenterContainer/GuidePhoto.texture!=null:
		hide_photo()
		$CenterContainer/ChessPieces.show()
	else:
		emit_signal("back_to_intro")

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
	$CenterContainer/GuidePhoto.texture = null

