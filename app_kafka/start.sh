#!/bin/bash

cd /opt/kafka_2.13-2.8.1/bin
sh kafka-console-producer.sh --bootstrap-server kafka:9092  --topic topic1