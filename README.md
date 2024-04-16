# Elecciones 2023

## Enunciado

- En el archivo de `models.py` vas a encontrarte con dos modelos: **PoliticalParties** y **Voters**
- En el archivo de `utils.py` vas a encontrarte dos funciones:
  - **has_voted**
  - **has_voted_percentage**
- Contexto:
  - Este sistema contempla la votación para **balotaje**
  - El sitio de ejemplo de votaciones generales: [elecciones 2023](https://resultados.gob.ar/resultados/2023/3/1/2)
  - Reglas que podrías tener que utilizar: [clases-de-votos](https://www.argentina.gob.ar/dine/clases-de-votos)
- Requisitos:
  - Página para votación
    - Se ingresa el documento y en según si ya voto o no:
      - si no voto, puede votar las opciones posibles
      - si ya voto, no puede votar
  - Página administración (con permiso) para realizar el cierre de la votación
    - Botón de cierre
    - Confirmación
    - Muestra de resultados y ganador
  - Página de resultados (pública)
    - en caso de no estar cerrada la votación, muestra el % de votantes que ya votaron y el total de votantes
    - en caso de ya cerrada la votación, muestra los resultados y ganador
  - **Se espera poder tener la información suficiente para en caso de necesitarse se pueda obtener el % de votos a favor de cada partido en determinada zona**
  - **Se valora también las buenas prácticas y el uso y entendimiento del entorno del proyecto**
## Requisitos previos

### Python

Version 3.11

#### Instalar dependencias de python

```bash
poetry install
```

#### Iniciar el entorno virtual

```bash
poetry shell
```

#### Migrations

```bash
cd ballot

python manage.py migrate
```

#### Crear un superuser

```bash
python manage.py createsuperuser
```

#### Iniciar servidor

```bash
python manage.py runserver
```

## Entorno de proyecto

### Herramientas utilizadas

- blue
- flake8
- pre-commit
- pytest

### pre-commit

#### Instalar pre-commit

```bash
pre-commit install
```

## Entorno de testing

### Ejecutar los tests

```bash
pytest ballot
```
