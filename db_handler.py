import os, sqlite3
from models import Concurso, Produtor


def saveConcurso(arq_name, concurso):
	arq_name += '.cl'
	os.remove(arq_name) if os.path.exists(arq_name) else None
	conn = sqlite3.connect(arq_name)
	c = conn.cursor()


	c.execute('CREATE TABLE info(numero INTEGER, localidade TEXT, categoria INTEGER, n_dias_ordenha INTEGER)')
	c.execute('INSERT INTO info(numero, localidade, categoria, n_dias_ordenha) VALUES '\
		'(? , ?, ?, ?)', (concurso.numero, concurso.localidade, concurso.categoria, concurso.n_dias_ordenha))


	ordenhas_string_aux = ''
	for i in range(concurso.n_dias_ordenha * 2):
		aux = 'ordenha' + str(i) + ' REAL'
		if i != ((concurso.n_dias_ordenha * 2) - 1): aux += ','
		ordenhas_string_aux += aux

	c.execute('CREATE TABLE produtores(id INTEGER PRIMARY KEY AUTOINCREMENT, numero INTEGER, nome TEXT, municipio TEXT, fazenda TEXT, '\
		'nome_vaca TEXT, perc_gordura INTEGER)')

	c.execute('CREATE TABLE ordenhas(id_produtor INTEGER, ' + ordenhas_string_aux + ')')


	for p in concurso.produtores:
		c.execute('INSERT INTO produtores(numero, nome, municipio, fazenda, nome_vaca, perc_gordura)'\
			' VALUES (?, ?, ?, ?, ?, ?)', (p.numero, p.nome, p.municipio, p.fazenda, p.nome_vaca, p.perc_gordura))


		produtor_id = c.lastrowid
		c.execute('INSERT INTO ordenhas(id_produtor) VALUES (?)', (produtor_id,))

		if(len(p.ordenhas) != 0):
			ordenhas_string_aux = ''
			interrogation_aux = ''
			for i in range(len(p.ordenhas)):
				aux = 'ordenha' + str(i)
				if i != len(p.ordenhas) - 1:
					aux += ','
					interrogation_aux += '?,'
				else:
					interrogation_aux += '?'
				ordenhas_string_aux += aux

			c.execute('INSERT INTO ordenhas(' + ordenhas_string_aux + ') VALUES ('\
				+ interrogation_aux + ')', tuple(p.ordenhas))
	

	conn.commit()



def testSave():
	o1 = [100,100,100,101,99,100]
	p1 = Produtor(1, 'Zequinha', 'BJI', 'roça da vovó', 'miranda', o1, 2.5)

	o2 = [99,99,99,99]
	p2 = Produtor(2, 'Juca', 'Calçado', 'pqp', 'mimosa', o2, 1)

	o3 = []
	p3 = Produtor(3, 'Mario César', 'Apiacá', 'sem criatividade irmão', 'alessandra', o3, 2)


	c = Concurso(21, 'Casa do caralho', '????', 3, [p1, p2, p3])


	saveConcurso('test', c)