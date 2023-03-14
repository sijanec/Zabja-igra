extends Node2D

var vrednost

var text

signal vidljivost_tock

signal spremeni_potezo

func _ready():
	$Gumb.text = text 
	
func _on_Gumb_button_up():
	emit_signal("spremeni_potezo", vrednost)
	emit_signal("vidljivost_tock")
