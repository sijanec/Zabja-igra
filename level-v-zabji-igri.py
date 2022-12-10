def naredi_polje(n,k,zamik_n=1,zamik_k=1):
	polje = []
	for i in range (zamik_n,n+1):
		for j in range (zamik_k,k+1):
			polje.append([i,j])
	return(polje)

def zmanjsaj_polje(polje,list):
	for i in polje:
		if i in list:
			i.append(False)
	return(polje)
		
	
def lovska_poteza(polje,frog_position):
	mozno =[]

	for i in[1,-1]	:
		for j in [1,-1]:
			x = 1
			while True:
				if [frog_position[0]+x*i,frog_position[1]+x*j] in polje:
					mozno.append([frog_position[0]+x*i,frog_position[1]+x*j])
					x += 1
				else:
					break
	return(mozno)


def trdnjavska_poteza(polje,frog_position):
	mozno=[]

	for i in [[0,1],[0,-1],[1,0],[-1,0]]:
		x = 1
		while True:
			if [frog_position[0]+i[0]*x,frog_position[1]+i[1]*x] in polje:
				mozno.append([frog_position[0]+i[0]*x,frog_position[1]+i[1]*x])
				x +=1
			else:
				break
	return mozno
			
def damina_poteza(polje,frog_position):
	return trdnjavska_poteza(polje,frog_position) + lovska_poteza(polje,frog_position)

def konjska_poteza(polje,frog_position):
	mozno =[]

	for i in [-1,1]:
		for j in [-1,1]:
			for k in [1,2]:
				if [frog_position[0]+i*k,frog_position[1]+j*(3-k)] in polje:
					mozno.append([frog_position[0]+i*k,frog_position[1]+j*(3-k)])
	return mozno

def kraljeva_poteza(polje,frog_position):
	mozno=[]

	for i in naredi_polje(frog_position[0]+1, frog_position[1]+1, frog_position[0]-1, frog_position[1]-1):
		if i in polje and i!= frog_position:
			mozno.append(i)
	return mozno


def trdnjavska_pot(start,finish):
	return naredi_polje(finish[0],finish[1],start[0],start[1])
		
def lovska_pot(start,finish):
	pot=[]

	if finish[0] > start[0]:
		a=1
	else:
		a=-1
	if finish[1] > start[1]:
		b=1
	else:
		b=-1
	for i in range (0,abs(finish[0]-start[0])+1):
		pot.append([start[0]+i*a,start[1]+i*b])
	return pot

def damina_pot(start,finish):
	if finish[0] == start[0] or finish[1] == start[1]:
		return trdnjavska_pot(start,finish)
	else:
		return lovska_pot(start,finish)


def konjska_pot(start,finish):
	return [start,finish]

def kraljevska_pot(start,finish):
	return [start,finish]

def shrani_game_state(game_state,muhe,poteze,frog_position,kljuc=False):
	return game_state.append([muhe,poteze,frog_position,kljuc])
	
def povrni_game_state(game_state):
	if len(game_state) != 1:
		game_state.remove(game_state[-1])
	return game_state

def povrni_muhe(game_state):
	return game_state[-1][0]

def povrni_poteze(game_state):
	return game_state[-1][1]

def povrni_frog_position(game_state):
	return game_state[-1][2]

def povrni_kljuc(game_state):
	return game_state[-1][3]



game_state = []


prepovedano = naredi_polje(4,4)
frog_position = [6,3]

muhe = naredi_polje(3,7,1,6)


polje = naredi_polje(8,8)
		
	
polje = zmanjsaj_polje(polje, prepovedano)

print('Polje: ' ,polje)

print('Lovska poteza: ' , lovska_poteza(polje,frog_position))

print('Trdnjavska poteza: ' , trdnjavska_poteza(polje,frog_position))

print('Damina poteza: ' , damina_poteza(polje,frog_position))

print('Konjska poteza: ', konjska_poteza(polje,frog_position))

print('Muhe: ',muhe)

print('Trdnjavska pot: ' ,trdnjavska_pot([6,3],[6,7]))