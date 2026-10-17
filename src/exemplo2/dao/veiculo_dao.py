
import sqlite3
from contextlib import closing
from typing import Optional

from database.connection_factory import ConnectionFactory
from model.veiculo import Veiculo


class VeiculoDAO:

    def __init__(self, connection_factory: Optional[ConnectionFactory] = None):
        self.connection_factory = connection_factory or ConnectionFactory()

    def create_table(self):
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS veiculo (
                marca VARCHAR(100) NOT NULL,
                modelo VARCHAR(100) NOT NULL,
                chassi VARCHAR(17) PRIMARY KEY,
                placa VARCHAR(20) NOT NULL,
                cor VARCHAR(50) NOT NULL
            )
        """

        with closing(self.connection_factory.create_connection()) as connection:
            with connection:
                connection.execute(create_table_sql)

        print("Tabela 'veiculo' criada ou já existe!")

    def create(self, veiculo: Veiculo):
        insert_sql = """
            INSERT INTO veiculo (marca, modelo, chassi, placa, cor)
            VALUES (?, ?, ?, ?, ?)
        """

        with closing(self.connection_factory.create_connection()) as connection:
            with connection:
                cursor = connection.execute(
                    insert_sql,
                    (veiculo.marca, veiculo.modelo, veiculo.chassi,
                     veiculo.placa, veiculo.cor)
                )
                veiculo.id = cursor.lastrowid

        print("Veículo cadastrado com sucesso!")
        return veiculo

    def read(self, veiculo_id: int) -> Optional[Veiculo]:
        select_sql = """
            SELECT id, marca, modelo, chassi, placa, cor
            FROM veiculo
            WHERE id = ?
        """

        with closing(self.connection_factory.create_connection()) as connection:
            connection.row_factory = sqlite3.Row
            row = connection.execute(select_sql, (veiculo_id,)).fetchone()

        if row is None:
            print("Veículo não encontrado!")
            return None

        veiculo = Veiculo(
            id=row["id"],
            marca=row["marca"],
            modelo=row["modelo"],
            chassi=row["chassi"],
            placa=row["placa"],
            cor=row["cor"]
        )

        return veiculo

    def read_all(self):
        select_sql = """
            SELECT id, marca, modelo, chassi, placa, cor
            FROM veiculo
            ORDER BY id
        """

        with closing(self.connection_factory.create_connection()) as connection:
            connection.row_factory = sqlite3.Row
            rows = connection.execute(select_sql).fetchall()

        veiculos = []

        for row in rows:
            veiculo = Veiculo(
                id=row["id"],
                marca=row["marca"],
                modelo=row["modelo"],
                chassi=row["chassi"],
                placa=row["placa"],
                cor=row["cor"]
            )
            veiculos.append(veiculo)

        return veiculos

    def update(self, veiculo: Veiculo):
        update_sql = """
            UPDATE veiculo
            SET marca = ?, modelo = ?, chassi = ?, placa = ?, cor = ?
            WHERE id = ?
        """

        with closing(self.connection_factory.create_connection()) as connection:
            with connection:
                cursor = connection.execute(
                    update_sql,
                    (veiculo.marca, veiculo.modelo, veiculo.chassi,
                     veiculo.placa, veiculo.cor, veiculo.id)
                )

        if cursor.rowcount > 0:
            print("Veículo atualizado com sucesso!")
        else:
            print("Veículo não encontrado!")

    def delete(self, veiculo_id: int):
        delete_sql = "DELETE FROM veiculo WHERE id = ?"

        with closing(self.connection_factory.create_connection()) as connection:
            with connection:
                cursor = connection.execute(delete_sql, (veiculo_id,))

        if cursor.rowcount > 0:
            print("Veículo removido do banco de dados!")
        else:
            print("Veículo não encontrado!")
