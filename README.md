# tarea2-SD
Entrega tarea 2 SD

Link vìdeo: https://www.youtube.com/watch?v=5sgnTWGUevk
1)Inicio Zookeeperbin/zookeeper-server-start.sh config/zookeeper.properties

/home/ubuntu/Documentos/kafka_2.12-3.7.0/bin/kafka-server-start.sh /home/ubuntu/Documentos/kafka_2.12-3.7.0/config/server.properties

/home/ubuntu/Documentos/kafka_2.12-3.7.0/bin/kafka-topics.sh --list --bootstrap-server localhost:9092


Una vez corriendo el zookeeper y el kafka procedemos a ejecutar los codigos del consumer y producer los ejecutamos y explicamos:
en maquina 1
python3 servicio_procesamiento_pedidos.py

en maquina 2
python3 servicio_entrega_pedidos.py
en maquina 3
python3 servicio_recepcion_pedidos.py

