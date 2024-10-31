from neo4j import GraphDatabase


class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        data = []
        with self.driver.session() as session:
            results = session.run(query, parameters)
            for record in results:
                data.append(record)
            return data

    def drop_all(self):
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")

    def buscar_professor_renzo(self):
        query = """
        MATCH (p:Teacher)
        WHERE p.name = 'Renzo'
        RETURN p.name, p.ano_nasc, p.cpf
        """
        return self.execute_query(query)

    def buscar_professores_m(self):
        query = """
        MATCH (p:Teacher)
        WHERE p.name STARTS WITH 'M'
        RETURN p.name, p.cpf
        """
        return self.execute_query(query)

    def buscar_todas_cidades(self):
        query = """
        MATCH (c:City)
        RETURN c.name
        """
        return self.execute_query(query)

    def buscar_escolas_por_numero(self):
        query = """
        MATCH (s:School)
        WHERE s.number >= 150 AND s.number <= 550
        RETURN s.name, s.address, s.number
        """
        return self.execute_query(query)

    def buscar_ano_nascimento_extremos(self):
        query = """
        MATCH (p:Teacher)
        RETURN min(p.ano_nasc) AS ano_mais_velho, max(p.ano_nasc) AS ano_mais_jovem
        """
        return self.execute_query(query)

    def calcular_media_habitantes(self):
        query = """
        MATCH (c:City)
        RETURN avg(c.population) AS media_habitantes
        """
        return self.execute_query(query)

    def buscar_cidade_cep_substituir_letra(self):
        query = """
        MATCH (c:City)
        WHERE c.cep = '37540-000'
        RETURN replace(c.name, 'a', 'A') AS nome_modificado
        """
        return self.execute_query(query)

    def buscar_caractere_terceira_letra_professores(self):
        query = """
        MATCH (p:Teacher)
        RETURN substring(p.name, 2, 1) AS caractere_terceira_letra
        """
        return self.execute_query(query)