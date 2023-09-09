from database import Database
from writeAJson import writeAJson

class ProductAnalyzer:
    def __init__(self, db: Database):
        self.database = db;

    def total_de_vendas_por_dia(self):
        result = self.database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total_de_vendas": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"_id": 1}},
        ])

        writeAJson(result, "Total de vendas por dia")

    def produto_mais_vendido_em_todas_as_compras(self):
        result = self.database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "qtde": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"qtde": -1}},
            {"$limit": 1}
        ])

        writeAJson(result, "Produto mais vendido em todas as compras")

    def cliente_que_mais_gastou_em_uma_compra(self):
        result = self.database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "valor_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"valor_gasto": -1}},
            {"$limit": 1}
        ])

        writeAJson(result, "Cliente que mais gastou em uma compra")

    def listar_produtos_acima_de_uma_unidade_vendidos(self):
        result = self.database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "qtd_vendida": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"qtd_vendida": {"$gt": 1}}},
        ])

        writeAJson(result, "Listar produtos acima de uma unidade vendidos")
