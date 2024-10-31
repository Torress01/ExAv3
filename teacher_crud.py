from query import Database


class TeacherCRUD:
    def __init__(self, db):
        self.db = db

    def create(self, name, ano_nasc, cpf):
        query = """
        CREATE (t:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})
        """
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)
        print(f"Teacher '{name}' criado com sucesso.")

    def read(self, name):
        query = """
        MATCH (t:Teacher {name: $name})
        RETURN t.name AS name, t.ano_nasc AS ano_nasc, t.cpf AS cpf
        """
        parameters = {"name": name}
        result = self.db.execute_query(query, parameters)
        return result

    def delete(self, name):
        query = """
        MATCH (t:Teacher {name: $name})
        DELETE t
        """
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
        print(f"Teacher '{name}' deletado com sucesso.")

    def update(self, name, newCpf):
        query = """
        MATCH (t:Teacher {name: $name})
        SET t.cpf = $newCpf
        """
        parameters = {"name": name, "newCpf": newCpf}
        self.db.execute_query(query, parameters)
        print(f"CPF do Teacher '{name}' atualizado para '{newCpf}'.")
