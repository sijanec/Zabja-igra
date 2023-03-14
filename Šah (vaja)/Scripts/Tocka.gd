extends Node2D

var pos : Vector2

var mozne_poteze = []

func _ready():
	show()
	pass

func _process(delta):
	connect("vidljivost_tock", self, "spremeni_vidljivost")

func spremeni_vidljivost():
	mozne_poteze = get_parent().mozne_poteze
	if pos in mozne_poteze:
		show()
	else:
		hide()
