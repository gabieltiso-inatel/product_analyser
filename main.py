from database import Database
from product_analyzer import ProductAnalyzer

db = Database(database="mercado", collection="compras")
db.resetDatabase()

pa = ProductAnalyzer(db)

pa.total_de_vendas_por_dia()
pa.produto_mais_vendido_em_todas_as_compras()
pa.cliente_que_mais_gastou_em_uma_compra()
pa.listar_produtos_acima_de_uma_unidade_vendidos()

# 1.Média de gasto total:
# result = db.collection.aggregate([
#     {"$unwind": "$produtos"},
#     {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#     {"$group": {"_id": None, "media": {"$avg": "$total"}}}
# ])

# # Cliente que mais comprou em cada dia:
# result = db.collection.aggregate([
#     {"$unwind": "$produtos"},
#     {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#     {"$sort": {"_id.data": 1, "total": -1}},
#     {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
# ])

# # Produto mais vendido:
# result = db.collection.aggregate([
#     {"$unwind": "$produtos"},
#     {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
#     {"$sort": {"total": -1}},
#     {"$limit": 1}
# ])
