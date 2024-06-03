from kafka import KafkaConsumer
from json import loads

servidores_bootstrap = 'localhost:9092'
topic_pedidos_procesados = 'pedidos.procesados'

consumer = KafkaConsumer(
    topic_pedidos_procesados,
    bootstrap_servers=[servidores_bootstrap],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='grupo_entrega'
)

def entregar_pedidos():
    for message in consumer:
        pedido_procesado = loads(message.value)
        print(f"Pedido entregado: {pedido_procesado}")

if __name__ == "__main__":
    entregar_pedidos()
