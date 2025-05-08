# Django MQTT Integration Test

This project is a Django-based application that subscribes to an MQTT topic, processes incoming sensor data, stores it in a database, and displays it on a web dashboard with optional filtering. It also exposes a REST API using Django REST Framework.

---

## Features

- MQTT integration with `test.mosquitto.org`
- Stores real-time sensor data in a PostgreSQL/SQLite DB
- Dashboard with filters (device ID, timestamp ordering)
- Django REST Framework API with filtering support
- HTMX-powered frontend (live updates without page reload)

---

##  Technologies Used

- Python 3.10+
- Django 4+
- Django REST Framework
- paho-mqtt
- HTMX
- MQTT Explorer
- django-filter

---

##  Setup Instructions

### 1. extract the zip file 

### 2. Create Virtual Environment & Install Dependencies

    python -m venv venv

    source venv/bin/activate  

    pip install -r requirements.txt

### 3. Apply Migrations

    python manage.py makemigrations
    python manage.py migrate


# 4. Run the Django Server

    python manage.py runserver
    Access: http://localhost:8000

### 5. Start MQTT Client (in separate terminal)

python mqtt_client.py (inside env itself)

## 6.  📡 MQTT Explorer Setup

        Download: https://mqtt-explorer.com

            Connect:

            Host: test.mosquitto.org

            Port: 1883

            Encryption (TLS): OFF

            Go to Publish tab and enter:

            Topic: iot/sensors/data

            Payload:
                    {
                "device_id": "sensor_001",
                "timestamp": "2025-05-07T10:15:30Z",
                "temperature": 23.5,
                "humidity": 60.2,
                "status": "active"
                }

<img width="312" alt="{C53A3487-6CA3-49D5-96D0-1181FA7881A2}" src="https://github.com/user-attachments/assets/99280de3-5e00-4edd-ac99-85c1edc8c807" />

<img width="668" alt="{345481BE-7773-48D6-8832-D2A6232ABE19}" src="https://github.com/user-attachments/assets/57319e86-89a2-4940-9fb4-d2e5749fb430" />

<img width="665" alt="{93BD2F38-DA8E-4FD3-A4D2-A40134CF1B2C}" src="https://github.com/user-attachments/assets/6dc9e020-c981-49ba-a8ef-abcb8d1f69d7" />



