from kafka import KafkaProducer
from csv import DictReader
from json import dumps
import time

servidores_bootstrap = 'localhost:9092'
topic_pedidos = 'pedidos'

productor = KafkaProducer(
    bootstrap_servers=[servidores_bootstrap],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

def enviar_pedidos(csv_file):
    with open(csv_file, 'r') as file:
        reader = DictReader(file)
        for row in reader:
            mensaje = {
                "nombre": row["nombre"],
                "precio": int(row["precio"]),
                "timestamp": time.time()
            }
            productor.send(topic_pedidos, value=mensaje)
            print(f"Pedido enviado: {mensaje}")
            time.sleep(1)  # Para simular un pequeño retraso entre envíos

if __name__ == "__main__":
    enviar_pedidos('pedidos.csv')
