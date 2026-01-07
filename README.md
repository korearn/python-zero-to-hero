# 🐍 Python Zero to Hero: From Scripting to Backend Engineering

Este repositorio documenta mi trayectoria intensiva de aprendizaje en Python, partiendo desde la sintaxis básica hasta la construcción de APIs RESTful conectadas a bases de datos y principios de ingeniería de software.

## 🎯 Objetivo
Dominar el ecosistema de Python aplicando principios **SOLID**, **Clean Code** y buenas prácticas de desarrollo Backend/DevOps.

## 📚 Estructura del Aprendizaje (Roadmap)

### 🟢 Fase 1: Fundamentos y Lógica
- **[Módulo 1: Fundamentos Críticos](./01_Fundamentos)**
  - *Conceptos:* Variables, Tipos de datos, Control Flow.
  - 🎲 **Proyecto:** `Adivina el Número`. Juego interactivo con lógica condicional.
  
- **[Módulo 2: Estructuras de Datos](./02_data_structures)**
  - *Conceptos:* Listas, Diccionarios, Tuplas, Sets y Funciones.
  - 🗃️ **Proyecto:** `Gestor de Tareas (CRUD en memoria)`. Manipulación eficiente de colecciones de datos.

- **[Módulo 3: Programación Orientada a Objetos (POO)](./03_oop)**
  - *Conceptos:* Clases, Herencia, Polimorfismo, Encapsulamiento.
  - ☁️ **Proyecto:** `Cloud Resource Manager`. Simulador de gestión de instancias EC2 y S3 buckets aplicando herencia.

### 🟡 Fase 2: Robustez e Integración
- **[Módulo 4: Manejo de Archivos y Errores](./04_file_handling)**
  - *Conceptos:* Persistencia en TXT/JSON, Context Managers, Try/Except.
  - 📦 **Proyecto:** `Inventario Persistente`. Sistema que guarda y carga stock automáticamente evitando crash por errores.

- **[Módulo 5: Módulos y APIs Externas](./05_modules_and_environments)**
  - *Conceptos:* Virtual Environments (venv), PIP, Requests, JSON parsing.
  - ⚡ **Proyecto:** `PokeInfo Downloader`. Herramienta de consola que consume la PokeAPI y guarda datos localmente.

- **[Módulo 6: Python Avanzado y Testing](./06_advanced_python_testing)**
  - *Conceptos:* List Comprehensions, Lambdas, Unit Testing (TDD).
  - 🧮 **Proyecto:** `Calculadora TDD`. Desarrollo guiado por pruebas unitarias automatizadas (`unittest`).

### 🔴 Fase 3: Desarrollo Web Backend (Flask & SQL)
- **[Módulo 7: Introducción a APIs REST](./07_web_api_flask)**
  - *Conceptos:* Protocolo HTTP, Rutas, Verbos (GET, POST), Flask Framework.
  - 🌐 **Proyecto:** `To-Do API`. Servicio web básico para gestión de tareas.

- **[Módulo 8: Bases de Datos y ORM](./08_databases_orm)**
  - *Conceptos:* SQLAlchemy, Modelos Relacionales, SQLite, Transacciones.
  - 💾 **Proyecto:** `API con Persistencia SQL`. Integración de base de datos relacional con Flask.

- **[Módulo 9: Proyecto Final - Expense Tracker](./09_final_project)**
  - *Conceptos:* Integración total, Lógica de negocio, Manejo de Fechas, Agregaciones SQL.
  - 💰 **Proyecto:** `API de Gastos Personales`. Sistema completo para registrar, categorizar y sumar gastos con validaciones reales.

---

## 🛠️ Stack Tecnológico

| Categoría | Tecnologías |
|-----------|-------------|
| **Lenguaje** | Python 3.x |
| **Backend Framework** | Flask |
| **Base de Datos** | SQLite, SQLAlchemy (ORM) |
| **Testing** | Unittest |
| **Herramientas** | Git, VS Code, Postman, Pip, Virtualenv |
| **DevOps Skills** | Estructura modular, Manejo de entornos, Git Flow |

## 🚀 Cómo ejecutar el Proyecto Final

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/korearn/python-zero-to-hero.git](https://github.com/korearn/python-zero-to-hero.git)
   cd python-zero-to-hero/09_final_project
2. Crear y activar entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
4. Ejecutar el servidor:
   ```bash
   python app.py

Hecho con 🐍 y disciplina por Leonardo León
