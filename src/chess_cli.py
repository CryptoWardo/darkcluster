#!/usr/bin/env python3
"""
Interfaz de línea de comandos para un sencillo juego de ajedrez.
Usa `python-chess` para gestionar las reglas y permite jugar contra
un adversario aleatorio controlado por el ordenador.
"""

import random
import sys
from typing import Optional

import chess
import chess.svg

PROMPT = "Introduce tu jugada en SAN (p. ej. e4, Cc3, O-O) o UCI (p. ej. e2e4): "


def print_board(board: chess.Board) -> None:
    """Muestra el tablero en consola usando ASCII."""
    # python-chess imprime con piezas en unicode para mejor lectura
    print(board.unicode(borders=True))


def parse_move(board: chess.Board, move_text: str) -> Optional[chess.Move]:
    """Convierte una jugada en SAN o UCI en un objeto Move válido."""
    try:
        move = board.parse_san(move_text)
        return move
    except ValueError:
        pass

    try:
        move = chess.Move.from_uci(move_text)
        if move in board.legal_moves:
            return move
    except ValueError:
        pass

    return None


def ask_for_move(board: chess.Board) -> chess.Move:
    """Solicita al usuario una jugada válida."""
    while True:
        raw_move = input(PROMPT).strip()
        move = parse_move(board, raw_move)
        if move is None:
            print("Jugada inválida. Prueba de nuevo.")
            continue
        return move


def pick_ai_move(board: chess.Board) -> chess.Move:
    """Selecciona una jugada legal al azar para el oponente IA."""
    legal_moves = list(board.legal_moves)
    return random.choice(legal_moves)


def show_game_status(board: chess.Board) -> None:
    """Muestra el estado actual de la partida."""
    if board.is_checkmate():
        winner = "Negras" if board.turn == chess.WHITE else "Blancas"
        print(f"Jaque mate. Ganador: {winner}!")
    elif board.is_stalemate():
        print("Tablas por ahogado.")
    elif board.is_insufficient_material():
        print("Tablas por material insuficiente.")
    elif board.is_seventyfive_moves():
        print("Tablas por la regla de las 75 jugadas.")
    elif board.can_claim_threefold_repetition():
        print("Se puede reclamar tablas por triple repetición.")


def main() -> int:
    print("Bienvenido al mini juego de ajedrez para consola. Juegas con blancas.")
    board = chess.Board()

    while not board.is_game_over():
        print_board(board)
        print("Turno de las blancas" if board.turn == chess.WHITE else "Turno de las negras")

        if board.turn == chess.WHITE:
            move = ask_for_move(board)
        else:
            move = pick_ai_move(board)
            print(f"La IA juega: {board.san(move)}")

        board.push(move)
        show_game_status(board)

    print_board(board)
    print("Resultado final:", board.result(claim_draw=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
