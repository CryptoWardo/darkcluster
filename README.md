# Darkcluster - Juego de ajedrez para consola

Este repositorio contiene un pequeño juego de ajedrez pensado como base para un proyecto Android o como herramienta de práctica en terminal. Está escrito en Python y usa [python-chess](https://python-chess.readthedocs.io/) para validar jugadas y gestionar el estado del tablero.

## Requisitos

- Python 3.10 o superior
- Dependencias del archivo `requirements.txt`

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

## Cómo jugar

Ejecuta el script principal desde la raíz del proyecto:

```bash
python src/chess_cli.py
```

- Siempre juegas con piezas blancas.
- La IA mueve piezas negras eligiendo al azar entre los movimientos legales.
- Introduce tus jugadas en notación SAN (por ejemplo `e4`, `Cc3`, `O-O`) o UCI (`e2e4`, `g1f3`).
- El juego termina automáticamente en jaque mate, tablas por ahogado, repetición, falta de material u otras condiciones oficiales.

## Próximos pasos sugeridos

- Empaquetar el núcleo de lógica en una librería para integrarlo en una app Android.
- Sustituir la IA aleatoria por un motor de evaluación heurística o por integración con Stockfish.
- Añadir persistencia de partidas y opción de deshacer jugadas.
