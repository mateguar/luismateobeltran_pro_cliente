# Proyecto: pro_clientes

## Datos del estudiante
- Nombre: Luis Mateo Beltran Repizo
- Programa: Ingeniería y Desarrollo de Software
- Institución: SENA

## Descripción
API REST desarrollada con FastAPI que gestiona una lista de amigos.
Cuenta con endpoints para saludar, ver la hora, listar amigos y buscar uno por su ID.

## Tecnologías usadas
- Python 3.x
- FastAPI
- Uvicorn

## Pasos para ejecutar el proyecto

### 1. Clonar o descargar el proyecto
```
cd luismateobeltran_pro_cliente
```

### 2. Crear el entorno virtual
```
python -m venv venv
```

### 3. Activar el entorno virtual

Windows (PowerShell):
```
.\venv\Scripts\Activate.ps1
```
Windows (Git Bash):
```
source venv/Scripts/activate
```
Mac/Linux:
```
source venv/bin/activate
```

### 4. Instalar dependencias
```
pip install "fastapi[standard]"
```

### 5. Ejecutar el servidor
```
uvicorn main:app --reload
```

## Endpoints disponibles
| Método | Ruta                            | Descripción                        |
|--------|---------------------------------|------------------------------------|
| GET    | /                               | Mensaje de bienvenida              |
| GET    | /saludar                        | Saludo genérico                    |
| GET    | /hora                           | Hora actual del servidor           |
| GET    | /saludar/{nombre}/{apellido}/{edad} | Saludo personalizado           |
| GET    | /amigos                         | Lista todos los amigos             |
| GET    | /amigos/{id}                    | Busca un amigo por ID              |
