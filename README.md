# 🔎 Python Port Scanner

Un escáner de puertos TCP multihilo desarrollado en Python para fines educativos y de aprendizaje en redes, programación y ciberseguridad.

## 🚀 Características

- Escaneo de puertos TCP
- Soporte para dominios e IPs
- Multithreading para mayor velocidad
- Detección de servicios comunes
- Generación automática de reportes
- Integración continua con GitHub Actions
- Análisis de seguridad con CodeQL
- Compatible con Python 3.12

---

## 📋 Tecnologías utilizadas

- Python
- Socket Programming
- Threading
- Git
- GitHub
- GitHub Actions
- CodeQL

---

## 📂 Estructura del proyecto

```text
port-scanner/
│
├── scanner.py
├── README.md
├── requirements.txt
│
└── .github/
    └── workflows/
        ├── python-app.yml
        └── codeql.yml
```

---

## ⚙️ Instalación

Clonar el repositorio:

```bash
git clone https://github.com/carlosarauz578-source/port-scanner.git
```

Entrar al directorio:

```bash
cd port-scanner
```

Actualizar pip:

```bash
python -m pip install --upgrade pip
```

Instalar dependencias (si existen):

```bash
pip install -r requirements.txt
```

---

## ▶️ Uso

Escanear un dominio:

```bash
python scanner.py google.com 20 100
```

Escanear una dirección IP:

```bash
python scanner.py 192.168.1.1 1 1024
```

---

## 🖥️ Ejemplo de salida

```text
==================================================
         PYTHON PORT SCANNER
        Carlos Rodriguez
==================================================

Target : google.com
IP     : 142.250.xxx.xxx
Ports  : 20-100

Scan Results
--------------------------------------------------
80/tcp   OPEN   HTTP
443/tcp  OPEN   HTTPS

Scan completed in 1.24 seconds

[+] Report saved: report_google_com.txt
```

---

## 📄 Reportes

Después de cada escaneo se genera automáticamente un archivo:

```text
report_google_com.txt
```

Ejemplo:

```text
PORT SCANNER REPORT
==================================================
Target: google.com
IP: 142.250.xxx.xxx

OPEN PORTS
--------------------------------------------------
80/tcp    OPEN    HTTP
443/tcp   OPEN    HTTPS
```

---

## 🔒 Seguridad y Calidad

Este proyecto utiliza:

### GitHub Actions

Automatiza la validación del código en cada push y pull request.

### CodeQL

Analiza automáticamente el código en busca de:

- Vulnerabilidades
- Errores comunes
- Problemas de calidad

---

## 🎯 Objetivos del proyecto

Este proyecto fue desarrollado con fines educativos para reforzar conocimientos en:

- Redes TCP/IP
- Programación en Python
- Automatización CI/CD
- Git y GitHub
- Ciberseguridad
- Desarrollo de herramientas de análisis de red

---

## ⚠️ Aviso Legal

Esta herramienta está destinada exclusivamente a fines educativos y de laboratorio.

No utilices este software para escanear sistemas o redes sin autorización explícita.

---

## 👨‍💻 Autor

**Carlos Enrique Rodríguez Arauz**

- GitHub: https://github.com/carlosarauz578-source

---

## ⭐ Apoya el proyecto

Si este proyecto te resulta útil:

- Dale una ⭐ al repositorio
- Comparte sugerencias y mejoras
- Realiza contribuciones mediante Pull Requests



