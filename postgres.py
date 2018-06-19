import psycopg2
try:
    con = psycopg2.connect(
        "host=127.0.0.1 dbname=projeto user=admin password=4linux")
    print('conexao efetuada com sucesso!')
    cur = con.cursor()
    cur.execute("insert into usuarios(nome, email, idade) values('maria', 'maria@maria.com.br', 74)")
    con.commit()
except Exception as e:
    print('Erro: {}'.format(e))