from query import Database
from teacher_crud import TeacherCRUD

def main():
    db = Database("bolt://3.239.169.181", "neo4j", "model-cloud-jig")
    teacher_crud = TeacherCRUD(db)

    print("1. Criando professor 'Chris Lima'")
    teacher_crud.create(name="Chris Lima", ano_nasc=1956, cpf="189.052.396-66")

    print("\n2. Lendo dados do professor 'Chris Lima'")
    result = teacher_crud.read(name="Chris Lima")
    print(f"Dados do professor: {result}")

    print("\n3. Atualizando CPF do professor 'Chris Lima'")
    teacher_crud.update(name="Chris Lima", newCpf="162.052.777-77")

    # Funções adicionais do Database
    print("\n5. Buscando o professor 'Renzo'")
    result = db.buscar_professor_renzo()
    print(result)

    print("\n6. Buscando professores com nomes que começam com 'M'")
    result = db.buscar_professores_m()
    print(result)

    print("\n7. Buscando todas as cidades")
    result = db.buscar_todas_cidades()
    print(result)

    print("\n8. Buscando escolas com número entre 150 e 550")
    result = db.buscar_escolas_por_numero()
    print(result)

    print("\n9. Encontrando o ano de nascimento do professor mais jovem e do mais velho")
    result = db.buscar_ano_nascimento_extremos()
    print(result)

    print("\n10. Calculando média de habitantes de todas as cidades")
    result = db.calcular_media_habitantes()
    print(result)

    print("\n11. Buscando cidade com CEP '37540-000' e substituindo 'a' por 'A'")
    result = db.buscar_cidade_cep_substituir_letra()
    print(result)

    print("\n12. Buscando o caractere a partir da 3ª letra do nome de cada professor")
    result = db.buscar_caractere_terceira_letra_professores()
    print(result)

    # Fechar a conexão com o banco de dados
    db.close()


if __name__ == "__main__":
    main()
