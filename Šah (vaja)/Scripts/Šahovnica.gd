extends Node2D

var polje = preload("res://Scenes/Polje.tscn")

var zabica = preload("res://Scenes/Zabica.tscn").instance()

var tocka = preload("res://Scenes/Tocka.tscn")

var tile_grid = []

var mozne_poteze = tile_grid

func ustvari_polje(x,y):
	for i in range(0,x):
		for j in range(0,y):
			var p = polje.instance()
			p.position = Vector2(i*64,j*64)
			p.pos = Vector2(i,j)
			
			add_child(p)
			tile_grid.append(Vector2(i,j))

func nastavi_tocke(x,y):
	for i in range(0,x):
		for j in range(0,y):
			var t = tocka.instance()
			t.position = Vector2(i*64,j*64)
			t.pos = Vector2(i,j)
			add_child(t)
			
			
			
func _ready():
	ustvari_polje(8,8)
	nastavi_tocke(8,8)
	add_child(zabica)
	zabica.position = Vector2(64 , 64)
	zabica.pos = Vector2(0,4)
	
	connect("spremeni_potezo", self, "spremeni_premikanje")
	
	pass





func check_valid(pos):
	if pos in mozne_poteze:
		return true

func attempt_move(pos):
	if (check_valid(pos)):
		zabica.pos = pos
		zabica.position = pos * 64

#TUKAJ
#SO
#POTEZE

func lovska_poteza(tile_gridd, pos):
	var mozno = []

	for i in [1, -1]:
		for j in [1, -1]:
			var x = 1
			while true:
				var tile_pos = Vector2(pos.x + x * i, pos.y + x * j)
				if tile_gridd.has_cell(tile_pos.x, tile_pos.y):
					mozno.append(tile_pos)
					x += 1
				else:
					break
	return mozno

var lovska_poteza_ref = funcref(self,"lovska_poteza")

func trdnjavska_poteza(tile_gridd, pos):
	var mozno = []

	for i in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
		var x = 1
		while true:
			var tile_pos = Vector2(pos.x + i[0] * x, pos.y + i[1] * x)
			if tile_gridd.has_cell(tile_pos.x, tile_pos.y):
				mozno.append(tile_pos)
				x += 1
			else:
				break
	return mozno

var trdnjavska_poteza_ref = funcref(self,"trdnjavska_poteza")

func damina_poteza(tile_gridd, pos):
	return trdnjavska_poteza(tile_gridd, pos) + lovska_poteza(tile_gridd, pos)

var damina_poteza_ref = funcref(self, "damina_poteza")

func konjska_poteza(tile_gridd, pos):
	var mozno = []

	for i in [-1, 1]:
		for j in [-1, 1]:
			for k in [1, 2]:
				var tile_pos = Vector2(pos.x + i * k, pos.y + j * (3 - k))
				if tile_gridd.has_cell(tile_pos.x, tile_pos.y):
					mozno.append(tile_pos)
	return mozno

var konjska_poteza_ref = funcref(self, "konjska_poteza")

func kraljeva_poteza(tile_gridd, pos):
	var mozno = []
	for tile_pos in tile_gridd.get_used_cells():
		if (tile_pos - pos).length() <= 1 and tile_pos != pos:
			mozno.append(tile_pos)
	return mozno
	
var kraljeva_poteza_ref = funcref(self, "kraljeva_poteza")

func dash_poteza(tile_gridd, pos):
	var mozno = []

	for i in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
		var x = 1
		while true:
			var tile_pos = Vector2(pos.x + i[0] * x, pos.y + i[1] * x)
			if tile_gridd.has_cell(tile_pos.x, tile_pos.y):
				x += 1
			else:
				mozno.append(Vector2(pos.x + i[0] * (x-1), pos.y + i[1] * (x-1)))
				break
	return mozno

var dash_poteza_ref = funcref(self, "dash_poteza")

var slovar_funkcij_potez = {
	"konj" : konjska_poteza_ref,
	"trdnjava": trdnjavska_poteza_ref,
	"dama": damina_poteza_ref,
	"kralj": kraljeva_poteza_ref,
	"lovec": lovska_poteza_ref,
	"dash": dash_poteza_ref
}

func spremeni_premikanje(vrednost):
	mozne_poteze = slovar_funkcij_potez[vrednost].call_func(tile_grid,zabica.pos)



#var slovar_funkcij_poti = {
#	"konj": konjska_pot,
#	"trdnjava": trdnjavska_pot,
#	"dama": damina_pot,
#	"kralj": kraljevska_pot,
#	"lovec": lovska_pot,
#	"dash": dash_pot
#}

