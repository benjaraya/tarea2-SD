from kafka import KafkaConsumer, KafkaProducer
from json import loads, dumps
import time

servidores_bootstrap = 'localhost:9092'
topic_pedidos = 'pedidos'
topic_pedidos_procesados = 'pedidos.procesados'

consumer = KafkaConsumer(
    topic_pedidos,
    bootstrap_servers=[servidores_bootstrap],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='grupo_procesamiento',
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

producer = KafkaProducer(
    bootstrap_servers=[servidores_bootstrap],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

def procesar_pedidos():
    for message in consumer:
        pedido = loads(message.value)
        pedido_procesado = {
            "nombre": pedido["nombre"],
            "precio": pedido["precio"] + 20,  # Simula un procesamiento que aumenta el precio
            "timestamp": time.time()
        }
        producer.send(topic_pedidos_procesados, value=pedido_procesado)
        print(f"Pedido procesado y enviado: {pedido_procesado}")

if __name__ == "__main__":
    procesar_pedidos()
