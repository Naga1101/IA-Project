import datetime

tempoActual = datetime.datetime.now()
dataActual = tempoActual.strftime('%Y-%m-%d %Hh') #pega no tempo actual, converte para string e retira minutos e segundos

entregasMiguel = ((123, 'rua sesamo', 'Santa Comba', 1, 2, '2023-4-24 12h'),(929, 'rua da moita', 'Coira', 12, 12, '2023-1-2 1h'))
listaAvalsMiguel = (5,5,4,5,5,5,5)
e1 = ('Miguel', entregasMiguel, listaAvalsMiguel, 'carro', 'centro de distribuicao')

entregasMaria = None
listaAvalsMaria = (0,1,0,2,1,0,0)
e2 = ('Maria', entregasMaria, listaAvalsMaria, 'bicicleta', 'centro de distribuicao')

entregasFernando = ((100, 'rua Diogo Barros', 'Arcozelo', 23, 19, '2023-11-11 19h'),(99, 'rua do chifre', 'Coira', 1, 10, '2023-12-2 5h'))
listaAvalsFernando = (3,2,3,5,3,1,0)
e3 = ('Fernando', entregasFernando, listaAvalsFernando, 'mota', 'centro de distribuicao')

entregasPedro = ((1, 'rua Guilherme Rego', 'Correlha', 6, 14, '2023-9-11 9h'),(237, 'rua Brandi Love', 'Angola', 13, 30 , '2023-5-3 13h'))
listaAvalsPedro = (5,2,4,5,5,1,2)
e4 = ('Pedro', entregasPedro, listaAvalsPedro, 'mota', 'centro de distribuicao')

entregasLuis = ((127, 'rua Rui Tijjy', 'Cepoes', 4, 9, '2023-8-16 17h'),(898, 'rua do moina', 'Barrio', 26, 33 , '2023-3-30 16h'))
listaAvalsLuis = (3,2,1,1,2,4,1)
e5 = ('Luis', entregasLuis, listaAvalsLuis, 'carro', 'centro de distribuicao')

entregasCarlos = ((567, 'rua insana', 'asilo', 5, 13, '2023-4-25 15h'),(23, 'rua do pirex', 'Setubal', 25, 44 , '2023-7-23 14h'))
listaAvalsCarlos = (1,3,4,0,2,3,0)
e6 = ('Carlos', entregasCarlos, listaAvalsCarlos, 'bicicleta', 'centro de distribuicao')

entregasManuel = ((58, 'rua Guilherme Rego', 'Correlha', 15, 14, '2023-11-2 9h'),(7, 'rua insana', 'asilo', 13, 30 , '2023-4-14 5h'))
listaAvalsManuel = (5,1,4,0,2,4,3)
e7 = ('Manuel', entregasManuel, listaAvalsManuel, 'carro', 'centro de distribuicao')

estafetas = {e1, e2, e3, e4, e5, e6, e7}
