# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # Registered device (your ESP32 ID)
# REGISTERED_DEVICES = {
#     "0123A4FF42005D32EE": True
# }

# @app.route("/auth", methods=["POST"])
# def auth():
#     data = request.json

#     device_id = data.get("device_id")
#     challenge = data.get("challenge")

#     print("\nReceived:")
#     print("Device ID:", device_id)
#     print("Challenge:", challenge)

#     if device_id in REGISTERED_DEVICES:
#         print("✅ VALID DEVICE")
#         return jsonify({"status": "VALID"})
#     else:
#         print("❌ INVALID DEVICE")
#         return jsonify({"status": "INVALID"})

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000




# from flask import Flask, request, jsonify
# from cryptography.hazmat.primitives.asymmetric import ec, utils
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.backends import default_backend

# app = Flask(__name__)

# # 🔐 Replace with YOUR real device ID + public key
# REGISTERED_DEVICES = {
#     "0123A4FF42005D32EE": {
#         "public_key": bytes.fromhex(
#             "050A9B225CE2845097F50D31109F944BCED48F3A6E600AF2E1751156D5750C77BA1A04E7CBFF34AA8E5F2B56F63CD0EDAC1641B27B155C564D9D63ABF95F7BF9"
#         )
#     }
# }

# def verify_signature(pubkey_bytes, hash_data, signature):
#     try:
#         # 🔹 Convert raw public key (64 bytes) → EC key
#         public_numbers = ec.EllipticCurvePublicNumbers(
#             int.from_bytes(pubkey_bytes[:32], "big"),
#             int.from_bytes(pubkey_bytes[32:], "big"),
#             ec.SECP256R1()
#         )
#         public_key = public_numbers.public_key(default_backend())

#         # 🔹 Split signature into r and s
#         r = int.from_bytes(signature[:32], "big")
#         s = int.from_bytes(signature[32:], "big")

#         # 🔹 Convert to DER format (required by cryptography lib)
#         der_signature = utils.encode_dss_signature(r, s)

#         # 🔹 Verify (IMPORTANT: using PREHASHED)
#         public_key.verify(
#             der_signature,
#             hash_data,
#             ec.ECDSA(utils.Prehashed(hashes.SHA256()))
#         )

#         return True

#     except Exception as e:
#         print("❌ Verification error:", e)
#         return False


# @app.route("/auth", methods=["POST"])
# def auth():
#     data = request.json

#     device_id = data.get("device_id")
#     hash_data = bytes.fromhex(data.get("challenge"))   # actually hash
#     signature = bytes.fromhex(data.get("signature"))

#     print("\n📥 Received:")
#     print("Device:", device_id)
#     if device_id not in REGISTERED_DEVICES:
#         print("❌ Unknown device")
#         return jsonify({"status": "INVALID"})

#     pubkey = REGISTERED_DEVICES[device_id]["public_key"]

#     if verify_signature(pubkey, hash_data, signature):
#         print("✅ AUTH SUCCESS")
#         return jsonify({"status": "VALID"})
#     else:
#         print("❌ AUTH FAILED")
#         return jsonify({"status": "INVALID"})


# if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=5000)





# import json
# import paho.mqtt.client as mqtt
# from cryptography.hazmat.primitives.asymmetric import ec, utils
# from cryptography.hazmat.primitives import hashes

# # 🔐 store real public key here
# REGISTERED_DEVICES = {
#     "0123A4FF42005D32EE": {
#         "public_key": bytes.fromhex("050A9B225CE2845097F50D31109F944BCED48F3A6E600AF2E1751156D5750C77BA1A04E7CBFF34AA8E5F2B56F63CD0EDAC1641B27B155C564D9D63ABF95F7BF9")
#     }
# }

# def verify_signature(pubkey_bytes, hash_data, signature):
#     try:
#         public_numbers = ec.EllipticCurvePublicNumbers(
#             int.from_bytes(pubkey_bytes[:32], "big"),
#             int.from_bytes(pubkey_bytes[32:], "big"),
#             ec.SECP256R1()
#         )
#         public_key = public_numbers.public_key()

#         r = int.from_bytes(signature[:32], "big")
#         s = int.from_bytes(signature[32:], "big")

#         der_signature = utils.encode_dss_signature(r, s)

#         public_key.verify(
#             der_signature,
#             hash_data,
#             ec.ECDSA(utils.Prehashed(hashes.SHA256()))
#         )

#         return True
#     except Exception as e:
#         print("❌ Verify error:", e)
#         return False

# def on_message(client, userdata, msg):
#     data = json.loads(msg.payload.decode())

#     device_id = data["device_id"]
#     hash_data = bytes.fromhex(data["challenge"])
#     signature = bytes.fromhex(data["signature"])

#     print("\n📥 Received:", data)

#     if device_id not in REGISTERED_DEVICES:
#         print("❌ Unknown device")
#         return

#     pubkey = REGISTERED_DEVICES[device_id]["public_key"]

#     if verify_signature(pubkey, hash_data, signature):
#         print("✅ AUTH SUCCESS")
#         print(f"🌡 Temp: {data['temperature']} °C")
#     else:
#         print("❌ AUTH FAILED")

# client = mqtt.Client()
# client.connect("localhost", 1883)
# client.subscribe("device/data")

# client.on_message = on_message

# print("🚀 Listening MQTT...")
# client.loop_forever()








# import json
# import paho.mqtt.client as mqtt
# from cryptography.hazmat.primitives.asymmetric import ec, utils
# from cryptography.hazmat.primitives import hashes

# # 🔐 REGISTER DEVICE
# REGISTERED_DEVICES = {
#     "0123A4FF42005D32EE": {
#         "public_key": bytes.fromhex(
#             "050A9B225CE2845097F50D31109F944BCED48F3A6E600AF2E1751156D5750C77BA1A04E7CBFF34AA8E5F2B56F63CD0EDAC1641B27B155C564D9D63ABF95F7BF9"
#         )
#     }
# }

# def verify_signature(pubkey_bytes, hash_data, signature):
#     try:
#         public_numbers = ec.EllipticCurvePublicNumbers(
#             int.from_bytes(pubkey_bytes[:32], "big"),
#             int.from_bytes(pubkey_bytes[32:], "big"),
#             ec.SECP256R1()
#         )
#         public_key = public_numbers.public_key()

#         r = int.from_bytes(signature[:32], "big")
#         s = int.from_bytes(signature[32:], "big")

#         der_signature = utils.encode_dss_signature(r, s)

#         public_key.verify(
#             der_signature,
#             hash_data,
#             ec.ECDSA(utils.Prehashed(hashes.SHA256()))
#         )

#         return True

#     except Exception as e:
#         print("❌ Verify error:", e)
#         return False


# def on_connect(client, userdata, flags, rc):
#     print("✅ Connected to broker with rc:", rc)
#     client.subscribe("rohith/device/data")   # 🔥 MUST MATCH ESP32


# def on_message(client, userdata, msg):
#     try:
#         data = json.loads(msg.payload.decode())

#         device_id = data["device_id"]
#         hash_data = bytes.fromhex(data["hash"])
#         signature = bytes.fromhex(data["signature"])

#         print("\n📥 Received:", data)

#         if device_id not in REGISTERED_DEVICES:
#             print("❌ Unknown device")
#             return

#         pubkey = REGISTERED_DEVICES[device_id]["public_key"]

#         if verify_signature(pubkey, hash_data, signature):
#             print("✅ AUTH SUCCESS")
#             print(f"🌡 Temp: {data['temperature']} °C")
#             print(f"💧 Hum: {data['humidity']} %")
#         else:
#             print("❌ AUTH FAILED")

#     except Exception as e:
#         print("❌ Error:", e)


# # 🔥 ONLY ONE CLIENT
# client = mqtt.Client()

# client.on_connect = on_connect
# client.on_message = on_message

# print("🚀 Connecting to MQTT...")

# client.connect("test.mosquitto.org", 1883)

# client.loop_forever()




# import json
# import paho.mqtt.client as mqtt
# from cryptography.hazmat.primitives.asymmetric import ec, utils
# from cryptography.hazmat.primitives import hashes

# # 🔐 YOUR DEVICE PUBLIC KEY (EXACT)
# PUBKEY_HEX = "050A9B225CE2845097F50D31109F944BCED48F3A6E600AF2E1751156D5750C77BA1A04E7CBFF34AA8E5F2B56F63CD0EDAC1641B27B155C564D9D63ABF95F7BF9"

# REGISTERED_DEVICES = {
#     "0123A4FF42005D32EE": {
#         "public_key": bytes.fromhex(PUBKEY_HEX)
#     }
# }


# def verify_signature(pubkey_bytes, hash_data, signature):
#     try:
#         # 🔹 Convert raw public key → EC key
#         x = int.from_bytes(pubkey_bytes[:32], "big")
#         y = int.from_bytes(pubkey_bytes[32:], "big")

#         public_numbers = ec.EllipticCurvePublicNumbers(x, y, ec.SECP256R1())
#         public_key = public_numbers.public_key()

#         # 🔹 Split signature
#         r = int.from_bytes(signature[:32], "big")
#         s = int.from_bytes(signature[32:], "big")

#         der_signature = utils.encode_dss_signature(r, s)

#         # 🔹 Verify (PREHASHED)
#         public_key.verify(
#             der_signature,
#             hash_data,
#             ec.ECDSA(utils.Prehashed(hashes.SHA256()))
#         )

#         return True

#     except Exception as e:
#         print("❌ Verify error:", e)
#         return False


# def on_connect(client, userdata, flags, rc):
#     print("✅ Connected to broker with rc:", rc)
#     client.subscribe("rohith/device/data")   # MUST MATCH ESP32


# def on_message(client, userdata, msg):
#     try:
#         # 🚫 Ignore other topics
#         if msg.topic != "rohith/device/data":
#             return

#         print("\n📥 Received RAW:", msg.payload)

#         data = json.loads(msg.payload.decode())

#         print("📦 Parsed JSON:", data)

#         device_id = data["device_id"]
#         hash_data = bytes.fromhex(data["hash"])
#         signature = bytes.fromhex(data["signature"])

#         if device_id not in REGISTERED_DEVICES:
#             print("❌ Unknown device")
#             return

#         pubkey = REGISTERED_DEVICES[device_id]["public_key"]

#         print("🔍 Verifying...")

#         if verify_signature(pubkey, hash_data, signature):
#             print("✅ AUTH SUCCESS")
#             print(f"🌡 Temp: {data['temperature']} °C")
#             print(f"💧 Hum: {data['humidity']} %")
#             client.publish("rohith/device/verified",json.dumps(data))  # 🔥 Send back to ESP32
#         else:
#             print("❌ AUTH FAILED")

#     except Exception as e:
#         print("❌ Error:", e)

# # 🔥 SINGLE CLIENT ONLY
# client = mqtt.Client()

# client.on_connect = on_connect
# client.on_message = on_message

# print("🚀 Connecting to MQTT...")

# client.connect("broker.hivemq.com", 1883)

# client.loop_forever()








# import json
# import threading
# from flask import Flask, jsonify, render_template
# import paho.mqtt.client as mqtt

# from cryptography.hazmat.primitives.asymmetric import ec, utils
# from cryptography.hazmat.primitives import hashes

# # ==============================
# # 🔐 DEVICE CONFIG
# # ==============================

# PUBKEY_HEX = "050A9B225CE2845097F50D31109F944BCED48F3A6E600AF2E1751156D5750C77BA1A04E7CBFF34AA8E5F2B56F63CD0EDAC1641B27B155C564D9D63ABF95F7BF9"

# REGISTERED_DEVICES = {
#     "0123A4FF42005D32EE": {
#         "public_key": bytes.fromhex(PUBKEY_HEX)
#     }
# }

# # ==============================
# # 🌡 LATEST DATA STORAGE
# # ==============================

# latest_data = {
#     "temperature": 0,
#     "humidity": 0
# }

# # ==============================
# # 🔐 VERIFY SIGNATURE
# # ==============================

# def verify_signature(pubkey_bytes, hash_data, signature):
#     try:
#         x = int.from_bytes(pubkey_bytes[:32], "big")
#         y = int.from_bytes(pubkey_bytes[32:], "big")

#         public_numbers = ec.EllipticCurvePublicNumbers(x, y, ec.SECP256R1())
#         public_key = public_numbers.public_key()

#         r = int.from_bytes(signature[:32], "big")
#         s = int.from_bytes(signature[32:], "big")

#         der_signature = utils.encode_dss_signature(r, s)

#         public_key.verify(
#             der_signature,
#             hash_data,
#             ec.ECDSA(utils.Prehashed(hashes.SHA256()))
#         )

#         return True

#     except Exception as e:
#         print("❌ Verify error:", e)
#         return False

# # ==============================
# # 📡 MQTT CALLBACKS
# # ==============================

# def on_connect(client, userdata, flags, rc):
#     print("✅ Connected to MQTT broker:", rc)
#     client.subscribe("rohith/device/data")   # MUST match ESP32

# def on_message(client, userdata, msg):
#     global latest_data

#     try:
#         if msg.topic != "rohith/device/data":
#             return

#         print("\n📥 Received RAW:", msg.payload)

#         data = json.loads(msg.payload.decode())
#         print("📦 Parsed JSON:", data)

#         device_id = data["device_id"]
#         hash_data = bytes.fromhex(data["hash"])
#         signature = bytes.fromhex(data["signature"])

#         if device_id not in REGISTERED_DEVICES:
#             print("❌ Unknown device")
#             return

#         pubkey = REGISTERED_DEVICES[device_id]["public_key"]

#         print("🔍 Verifying...")

#         if verify_signature(pubkey, hash_data, signature):
#             print("✅ AUTH SUCCESS")

#             print(f"🌡 Temp: {data['temperature']} °C")
#             print(f"💧 Hum: {data['humidity']} %")

#             # ✅ STORE VERIFIED DATA
#             latest_data["temperature"] = data["temperature"]
#             latest_data["humidity"] = data["humidity"]

#             # (optional MQTT forward)
#             client.publish("rohith/device/verified", json.dumps(data))

#         else:
#             print("❌ AUTH FAILED")

#     except Exception as e:
#         print("❌ Error:", e)

# # ==============================
# # 🌐 FLASK WEB SERVER
# # ==============================

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/data")
# def get_data():
#     return jsonify(latest_data)

# # ==============================
# # 🚀 RUN MQTT + FLASK TOGETHER
# # ==============================

# def run_mqtt():
#     client.loop_forever()

# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_message = on_message

# print("🚀 Connecting to MQTT...")
# client.connect("broker.hivemq.com", 1883)

# # Run MQTT in background thread
# threading.Thread(target=run_mqtt).start()

# # Run Flask
# app.run(host="0.0.0.0", port=5000, debug=True)




import json
import threading
import time
from flask import Flask, jsonify, render_template
import paho.mqtt.client as mqtt

from cryptography.hazmat.primitives.asymmetric import ec, utils
from cryptography.hazmat.primitives import hashes

# ==============================
# 🔐 DEVICE CONFIG
# ==============================

PUBKEY_HEX = "050A9B225CE2845097F50D31109F944BCED48F3A6E600AF2E1751156D5750C77BA1A04E7CBFF34AA8E5F2B56F63CD0EDAC1641B27B155C564D9D63ABF95F7BF9"

REGISTERED_DEVICES = {
    "0123A4FF42005D32EE": {
        "public_key": bytes.fromhex(PUBKEY_HEX)
    }
}

# ==============================
# 📊 SYSTEM STATE
# ==============================

latest_data = {"temperature": 0, "humidity": 0}

device_status = {
    "status": "offline",
    "last_seen": 0,
    "attacks": 0
}

stats = {
    "messages": 0,
    "valid": 0,
    "rejected": 0
}

last_timestamp = 0

# ==============================
# 🔐 SIGNATURE VERIFY
# ==============================

def verify_signature(pubkey_bytes, hash_data, signature):
    try:
        x = int.from_bytes(pubkey_bytes[:32], "big")
        y = int.from_bytes(pubkey_bytes[32:], "big")

        public_numbers = ec.EllipticCurvePublicNumbers(x, y, ec.SECP256R1())
        public_key = public_numbers.public_key()

        r = int.from_bytes(signature[:32], "big")
        s = int.from_bytes(signature[32:], "big")

        der_signature = utils.encode_dss_signature(r, s)

        public_key.verify(
            der_signature,
            hash_data,
            ec.ECDSA(utils.Prehashed(hashes.SHA256()))
        )

        return True
    except:
        return False

# ==============================
# 📡 MQTT CALLBACKS
# ==============================

def on_connect(client, userdata, flags, rc):
    print("✅ MQTT Connected:", rc)
    client.subscribe("rohith/device/data")

def on_message(client, userdata, msg):
    global last_timestamp

    try:
        data = json.loads(msg.payload.decode())
        stats["messages"] += 1

        device_id = data["device_id"]
        hash_data = bytes.fromhex(data["hash"])
        signature = bytes.fromhex(data["signature"])

        # ❌ Unknown device
        if device_id not in REGISTERED_DEVICES:
            print("🚨 UNKNOWN DEVICE")
            stats["rejected"] += 1
            device_status["attacks"] += 1
            return

        pubkey = REGISTERED_DEVICES[device_id]["public_key"]

        # ❌ Signature tamper
        if not verify_signature(pubkey, hash_data, signature):
            print("🚨 SIGNATURE TAMPER")
            stats["rejected"] += 1
            device_status["attacks"] += 1
            return

        # ❌ Replay attack
        if data["timestamp"] <= last_timestamp:
            print("🚨 REPLAY ATTACK")
            stats["rejected"] += 1
            device_status["attacks"] += 1
            return

        last_timestamp = data["timestamp"]

        # ❌ Sensor tamper
        if data["temperature"] > 80 or data["temperature"] < -10:
            print("🚨 SENSOR TAMPER")
            stats["rejected"] += 1
            device_status["attacks"] += 1
            return

        # ✅ VALID DATA
        latest_data["temperature"] = data["temperature"]
        latest_data["humidity"] = data["humidity"]

        stats["valid"] += 1

        device_status["status"] = "online"
        device_status["last_seen"] = time.time()

        print("✅ VALID DATA")

    except Exception as e:
        print("❌ Error:", e)

# ==============================
# 🔍 DEVICE OFFLINE CHECK
# ==============================

def monitor():
    while True:
        if time.time() - device_status["last_seen"] > 10:
            device_status["status"] = "offline"
        time.sleep(5)

# ==============================
# 🌐 FLASK APP
# ==============================

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():
    return jsonify(latest_data)

@app.route("/device")
def device():
    return jsonify(device_status)

@app.route("/stats")
def stats_api():
    return jsonify(stats)

# ==============================
# 🚀 RUN
# ==============================

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883)

threading.Thread(target=client.loop_forever).start()
threading.Thread(target=monitor).start()

app.run(host="0.0.0.0", port=5000)