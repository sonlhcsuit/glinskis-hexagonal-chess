extends Node
signal open_setting
signal start_game
signal open_guide
signal save_setting
signal back_to_intro

onready var scene = $Intro

func _ready():
	connect_signal()

func connect_signal():
	scene.connect("start_game",self,"start_game_handler")
	scene.connect("back_to_intro",self,"back_to_intro_handler")
	scene.connect("open_guide",self,"open_guide_handler")
	scene.connect("open_setting",self,"open_setting_handler")

func start_game_handler():
	var next_scene = load("res://Scenes/Main.tscn").instance()
	add_child(next_scene)
	scene.queue_free()
	scene = next_scene
	connect_signal()

func back_to_intro_handler():
	var next_scene = load("res://Scenes/Intro.tscn").instance()
	add_child(next_scene)
	scene.queue_free()
	scene = next_scene
	connect_signal()
	
func open_guide_handler():
	var next_scene = load("res://Scenes/Guide.tscn").instance()
	add_child(next_scene)
	scene.queue_free()
	scene = next_scene
	connect_signal()

func open_setting_handler():
	var next_scene = load("res://Scenes/Setting.tscn").instance()
	add_child(next_scene)
	scene.queue_free()
	scene = next_scene
	connect_signal()
