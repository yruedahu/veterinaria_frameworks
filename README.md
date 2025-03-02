# 🏥 Veterinary Project

🚀 **Veterinary Project** es una aplicación web desarrollada en **Django** para gestionar información de clínicas veterinarias. Permite administrar usuarios, mascotas, facturación, inventarios y más.

---

## 📌 Características

✅ Gestión de clientes y sus mascotas.  
✅ Administración de citas y servicios veterinarios.  
✅ Módulo de facturación e inventario.  
✅ Interfaz moderna y responsive.  
✅ Base de datos con **MongoDB** usando **Djongo**.

---

## 🛠️ Instalación y Configuración

### **1️⃣ Clonar el Repositorio**
```bash
git clone https://github.com/yruedahu/Veterinary_project
cd Veterinary_project
```

### **2️⃣ Crear tu propia rama**
```bash
git checkout -b ["Tu nombre"]
```

### **3️⃣Crear y Activar un Entorno Virtual**
```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En macOS / Linux
source venv/bin/activate
```

### **4️⃣Instalar Dependencias**
```bash
pip install -r requirements.txt
```

### **4️⃣ Ejecutar el Servidor**
```bash
python manage.py runserver
```
📌 La aplicación estará disponible en **http://127.0.0.1:8000/**

---

## 📂 Estructura del Proyecto

```
📦 veterinary_project
├── 📂 apps
│   ├── 📂 veterinary_home
│   │   ├── 📂 templates
│   │   ├── 📂 static
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── ...
│   ├── 📂 veterinary_users
│   ├── 📂 veterinary_pets
│   ├── 📂 veterinary_clinic
│   ├── 📂 veterinary_billing
│   ├── 📂 veterinary_inventory
├── 📂 config
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
├── 📂 public
│   ├── 📂 images
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---

## 📢 Contribuir

1. **Forkea** el proyecto 🍴
2. **Crea una rama** (`git checkout -b feature/nueva-funcionalidad`)
3. **Sube tus cambios** (`git commit -m 'Añadida nueva funcionalidad'`)
4. **Envía un PR** ✅

---

## 📬 Contacto
📌 **Creador:** Mateo rueda hurtado  
📌 **Correo:** yruedahu@uninpahu.edu.com  

📢 ¡Si te gusta este proyecto, dale una ⭐ en GitHub! 🚀

