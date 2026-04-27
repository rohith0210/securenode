// #include <WiFi.h>
// #include <PubSubClient.h>
// #include <Wire.h>
// #include <ArduinoECCX08.h>
// #include "mbedtls/sha256.h"
// #include <DHT.h>

// #define DHTPIN 4
// #define DHTTYPE DHT11

// DHT dht(DHTPIN, DHTTYPE);

// // WiFi
// const char* ssid = "hostel";
// const char* password = "snk@4321";

// // MQTT (public broker)
// const char* mqtt_server = "test.mosquitto.org";

// WiFiClient espClient;
// PubSubClient client(espClient);

// // 🔧 HEX helper
// void toHex(uint8_t *data, int len, String &out) {
//   char buf[3];
//   for (int i = 0; i < len; i++) {
//     sprintf(buf, "%02X", data[i]);
//     out += buf;
//   }
// }

// // 📡 WiFi
// void setup_wifi() {
//   WiFi.begin(ssid, password);
//   Serial.print("Connecting WiFi");

//   while (WiFi.status() != WL_CONNECTED) {
//     delay(500);
//     Serial.print(".");
//   }

//   Serial.println("\n✅ WiFi Connected");
// }

// // 🔌 MQTT reconnect
// void reconnect() {
//   while (!client.connected()) {
//     Serial.print("Connecting MQTT...");

//     if (client.connect("ESP32_SECURE_NODE")) {
//       Serial.println("✅ Connected");
//     } else {
//       Serial.print("❌ rc=");
//       Serial.println(client.state());
//       delay(2000);
//     }
//   }
// }

// void setup() {
//   Serial.begin(115200);
//   delay(1000);

//   Serial.println("\n===== SECURE MQTT NODE =====");

//   Wire.begin(21, 22);

//   if (!ECCX08.begin()) {
//     Serial.println("❌ ATECC not detected");
//     while (1);
//   }

//   Serial.println("✅ ATECC detected");

//   dht.begin();

//   setup_wifi();

//   client.setServer(mqtt_server, 1883);
// }

// void loop() {
//   if (!client.connected()) {
//     reconnect();
//   }
//   client.loop();

//   // 🌡 Read sensor
//   float temp = dht.readTemperature();
//   float hum = dht.readHumidity();

//   if (isnan(temp) || isnan(hum)) {
//     Serial.println("❌ Sensor error");
//     delay(2000);
//     return;
//   }

//   // 🔐 Get device ID
//   byte serial[9];
//   ECCX08.serialNumber(serial);

//   String device_id = "";
//   toHex(serial, 9, device_id);

//   // 📦 Create data string
//   String data = String(temp) + "," + String(hum);

//   // 🔹 HASH
//   uint8_t hash[32];
//   mbedtls_sha256((const unsigned char*)data.c_str(), data.length(), hash, 0);

//   // 🔐 SIGN
//   uint8_t signature[64];
//   if (!ECCX08.ecSign(0, hash, signature)) {
//     Serial.println("❌ Signing failed");
//     return;
//   }

//   // 🔄 Convert to HEX
//   String hash_hex = "";
//   String sig_hex = "";

//   toHex(hash, 32, hash_hex);
//   toHex(signature, 64, sig_hex);

//   // 📤 JSON payload
//   String payload = "{";
//   payload += "\"device_id\":\"" + device_id + "\",";
//   payload += "\"temperature\":" + String(temp) + ",";
//   payload += "\"humidity\":" + String(hum) + ",";
//   payload += "\"hash\":\"" + hash_hex + "\",";
//   payload += "\"signature\":\"" + sig_hex + "\"";
//   payload += "}";

//   Serial.println("\n📤 Publishing:");
//   Serial.println(payload);

//   client.publish("rohith/device/data", payload.c_str());

//   delay(8000);
// }



// #define MQTT_MAX_PACKET_SIZE 512
// #include <WiFi.h>
// #include <PubSubClient.h>
// #include <Wire.h>
// #include <ArduinoECCX08.h>
// #include "mbedtls/sha256.h"
// #include <DHT.h>

// #define DHTPIN 4
// #define DHTTYPE DHT11


// DHT dht(DHTPIN, DHTTYPE);

// // WiFi
// const char* ssid = "hostel";
// const char* password = "snk@4321";

// // MQTT
// const char* mqtt_server = "broker.hivemq.com";

// WiFiClient espClient;
// PubSubClient client(espClient);

// // 🔧 HEX helper
// void toHex(uint8_t *data, int len, String &out) {
//   char buf[3];
//   for (int i = 0; i < len; i++) {
//     sprintf(buf, "%02X", data[i]);
//     out += buf;
//   }
// }

// // 📡 WiFi
// void setup_wifi() {
//   WiFi.begin(ssid, password);
//   Serial.print("Connecting WiFi");

//   while (WiFi.status() != WL_CONNECTED) {
//     delay(500);
//     Serial.print(".");
//   }

//   Serial.println("\n✅ WiFi Connected");
// }

// // 🔌 MQTT reconnect
// void reconnect() {
//   while (!client.connected()) {
//     Serial.print("Connecting MQTT...");

//     if (client.connect("ESP32_SECURE_NODE")) {
//       Serial.println("✅ Connected to MQTT");
//     } else {
//       Serial.print("❌ Failed, rc=");
//       Serial.print(client.state());
//       Serial.println(" → retry in 3 sec");
//       delay(3000);
//     }
//   }
// }

// void setup() {
//   Serial.begin(115200);
//   delay(1000);

//   Serial.println("\n===== SECURE MQTT NODE =====");

//   Wire.begin(21, 22);

//   if (!ECCX08.begin()) {
//     Serial.println("❌ ATECC not detected");
//     while (1);
//   }

//   Serial.println("✅ ATECC detected");

//   dht.begin();
//   setup_wifi();

//   client.setServer(mqtt_server, 1883);

//   // 🔐 PRINT PUBLIC KEY ONCE (VERY IMPORTANT)
//   uint8_t pubkey[64];

//   if (!ECCX08.generatePublicKey(0, pubkey)) {
//     Serial.println("❌ Failed to get public key");
//   } else {
//     String pub_hex = "";
//     toHex(pubkey, 64, pub_hex);

//     Serial.println("\n🔑 PUBLIC KEY (COPY THIS EXACTLY):");
//     Serial.println(pub_hex);
//   }
// }

// void loop() {

//   if (!client.connected()) {
//     reconnect();
//   }
//   client.loop();

//   // 🌡 SENSOR
//   float temp = dht.readTemperature();
//   float hum = dht.readHumidity();

//   if (isnan(temp) || isnan(hum)) {
//     Serial.println("❌ Sensor error");
//     delay(2000);
//     return;
//   }

//   // 🔐 DEVICE ID
//   byte serial[9];
//   ECCX08.serialNumber(serial);

//   String device_id = "";
//   toHex(serial, 9, device_id);

//   // 🔥 FIXED DATA FORMAT (VERY IMPORTANT)
//   String data = String(temp, 2) + "," + String(hum, 2);

//   Serial.println("\n📦 DATA:");
//   Serial.println(data);

//   // 🔹 HASH
//   uint8_t hash[32];
//   mbedtls_sha256((const unsigned char*)data.c_str(), data.length(), hash, 0);

//   String hash_hex = "";
//   toHex(hash, 32, hash_hex);

//   Serial.println("🔹 HASH:");
//   Serial.println(hash_hex);

//   // 🔐 SIGN
//   uint8_t signature[64];
//   if (!ECCX08.ecSign(0, hash, signature)) {
//     Serial.println("❌ Signing failed");
//     return;
//   }

//   String sig_hex = "";
//   toHex(signature, 64, sig_hex);

//   Serial.println("🔐 SIGN:");
//   Serial.println(sig_hex);

//   // 📤 JSON PAYLOAD
//   String payload = "{";
//   payload += "\"device_id\":\"" + device_id + "\",";
//   payload += "\"temperature\":" + String(temp, 2) + ",";
//   payload += "\"humidity\":" + String(hum, 2) + ",";
//   payload += "\"hash\":\"" + hash_hex + "\",";
//   payload += "\"signature\":\"" + sig_hex + "\"";
//   payload += "}";

//   Serial.println("\n📤 Publishing:");
//   Serial.println(payload);
//   Serial.print("MQTT state: ");
//   Serial.println(client.state());
//   bool status = client.publish("rohith/device/data", payload.c_str());

//   if (status) {
//   Serial.println("✅ MQTT Publish Success");
//   } else {
//   Serial.println("❌ MQTT Publish Failed");
//   }

//   delay(8000);
// }




//before final draft...
// #define MQTT_MAX_PACKET_SIZE 512

// #include <WiFi.h>
// #include <PubSubClient.h>
// #include <WiFiClientSecure.h>
// #include <Wire.h>
// #include <ArduinoECCX08.h>
// #include "mbedtls/sha256.h"
// #include <DHT.h>

// #define DHTPIN 4
// #define DHTTYPE DHT11

// DHT dht(DHTPIN, DHTTYPE);

// // WiFi
// const char* ssid = "hostel";
// const char* password = "snk@4321";

// // MQTT TLS
// const char* mqtt_server = "broker.hivemq.com";
// const int mqtt_port = 8883;

// WiFiClientSecure espClient;
// PubSubClient client(espClient);

// // 🔧 HEX helper
// void toHex(uint8_t *data, int len, String &out) {
//   char buf[3];
//   for (int i = 0; i < len; i++) {
//     sprintf(buf, "%02X", data[i]);
//     out += buf;
//   }
// }

// // 📡 WiFi
// void setup_wifi() {
//   WiFi.begin(ssid, password);
//   Serial.print("Connecting WiFi");

//   while (WiFi.status() != WL_CONNECTED) {
//     delay(500);
//     Serial.print(".");
//   }

//   Serial.println("\n✅ WiFi Connected");
//   Serial.print("IP: ");
//   Serial.println(WiFi.localIP());
// }

// // 🔌 MQTT reconnect
// void reconnect() {
//   while (!client.connected()) {
//     Serial.print("Connecting MQTT TLS...");

//     if (client.connect("ESP32_SECURE_NODE_TLS")) {
//       Serial.println("✅ Connected to MQTT (TLS)");
//     } else {
//       Serial.print("❌ Failed, rc=");
//       Serial.print(client.state());
//       Serial.println(" → retry");
//       delay(3000);
//     }
//   }
// }


// void setup() {
//   Serial.begin(115200);
//   delay(1000);

//   Serial.println("\n===== SECURE MQTT TLS NODE =====");

//   Wire.begin(21, 22);

//   if (!ECCX08.begin()) {
//     Serial.println("❌ ATECC not detected");
//     while (1);
//   }

//   Serial.println("✅ ATECC detected");

//   dht.begin();
//   setup_wifi();

//   // 🔥 TLS DEBUG MODE
//   espClient.setInsecure();  

//   Serial.println("⚠️ TLS: Insecure mode (no cert validation)");

//   client.setServer(mqtt_server, mqtt_port);

//   Serial.println("🔐 MQTT TLS configured (port 8883)");
// }


// void loop() {

//   if (!client.connected()) {
//     reconnect();
//   }
//   client.loop();

//   Serial.print("MQTT state: ");
//   Serial.println(client.state());

//   // 🌡 SENSOR
//   float temp = dht.readTemperature();
//   float hum = dht.readHumidity();

//   if (isnan(temp) || isnan(hum)) {
//     Serial.println("❌ Sensor error");
//     delay(2000);
//     return;
//   }

//   // 🔐 DEVICE ID
//   byte serial[9];
//   ECCX08.serialNumber(serial);

//   String device_id = "";
//   toHex(serial, 9, device_id);

//   // DATA
//   String data = String(temp, 2) + "," + String(hum, 2);

//   Serial.println("\n📦 DATA:");
//   Serial.println(data);

//   // 🔹 HASH
//   uint8_t hash[32];
//   mbedtls_sha256((const unsigned char*)data.c_str(), data.length(), hash, 0);

//   String hash_hex = "";
//   toHex(hash, 32, hash_hex);

//   Serial.println("🔹 HASH:");
//   Serial.println(hash_hex);

//   // 🔐 SIGN
//   uint8_t signature[64];
//   if (!ECCX08.ecSign(0, hash, signature)) {
//     Serial.println("❌ Signing failed");
//     return;
//   }

//   String sig_hex = "";
//   toHex(signature, 64, sig_hex);

//   Serial.println("🔐 SIGN:");
//   Serial.println(sig_hex);

//   // 📤 JSON
//   String payload = "{";
//   payload += "\"device_id\":\"" + device_id + "\",";
//   payload += "\"temperature\":" + String(temp, 2) + ",";
//   payload += "\"humidity\":" + String(hum, 2) + ",";
//   payload += "\"hash\":\"" + hash_hex + "\",";
//   payload += "\"signature\":\"" + sig_hex + "\"";
//   payload += "}";

//   Serial.println("\n📤 Publishing (TLS):");
//   Serial.println(payload);

//   bool status = client.publish("rohith/device/data", payload.c_str());

//   if (status) {
//     Serial.println("✅ MQTT Publish Success (TLS)");
//   } else {
//     Serial.println("❌ MQTT Publish Failed (TLS)");
//   }

//   delay(8000);
// }



//THE FINAL ONE::::


#define MQTT_MAX_PACKET_SIZE 512

#include <WiFi.h>
#include <PubSubClient.h>
#include <WiFiClientSecure.h>
#include <Wire.h>
#include <ArduinoECCX08.h>
#include "mbedtls/sha256.h"
#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

// WiFi
const char* ssid = "hostel";
const char* password = "snk@4321";

// MQTT TLS
const char* mqtt_server = "broker.hivemq.com";
const int mqtt_port = 8883;

WiFiClientSecure espClient;
PubSubClient client(espClient);

// HEX helper
void toHex(uint8_t *data, int len, String &out) {
  char buf[3];
  for (int i = 0; i < len; i++) {
    sprintf(buf, "%02X", data[i]);
    out += buf;
  }
}

// WiFi
void setup_wifi() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
}

// MQTT reconnect
void reconnect() {
  while (!client.connected()) {
    if (client.connect("ESP32_SECURE_NODE_TLS")) {
      Serial.println("MQTT Connected");
    } else {
      delay(2000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);

  if (!ECCX08.begin()) {
    Serial.println("ATECC ERROR");
    while (1);
  }

  dht.begin();
  setup_wifi();

  espClient.setInsecure();  // for testing

  client.setServer(mqtt_server, mqtt_port);
}

void loop() {

  if (!client.connected()) reconnect();
  client.loop();

  float temp = dht.readTemperature();
  float hum = dht.readHumidity();

  if (isnan(temp) || isnan(hum)) return;

  // DEVICE ID
  byte serial[9];
  ECCX08.serialNumber(serial);

  String device_id = "";
  toHex(serial, 9, device_id);

  // 🔥 SECURITY DATA
  unsigned long timestamp = millis();
  uint32_t nonce = esp_random();

  // 🔐 DATA STRING (VERY IMPORTANT)
  String data = String(temp,2) + "," + String(hum,2) + "," + String(timestamp) + "," + String(nonce);

  // HASH
  uint8_t hash[32];
  mbedtls_sha256((const unsigned char*)data.c_str(), data.length(), hash, 0);

  String hash_hex = "";
  toHex(hash, 32, hash_hex);

  // SIGN
  uint8_t signature[64];
  if (!ECCX08.ecSign(0, hash, signature)) return;

  String sig_hex = "";
  toHex(signature, 64, sig_hex);

  // JSON
  String payload = "{";
  payload += "\"device_id\":\"" + device_id + "\",";
  payload += "\"temperature\":" + String(temp,2) + ",";
  payload += "\"humidity\":" + String(hum,2) + ",";
  payload += "\"timestamp\":" + String(timestamp) + ",";
  payload += "\"nonce\":" + String(nonce) + ",";
  payload += "\"hash\":\"" + hash_hex + "\",";
  payload += "\"signature\":\"" + sig_hex + "\"";
  payload += "}";

  client.publish("rohith/device/data", payload.c_str());

  delay(5000);
}