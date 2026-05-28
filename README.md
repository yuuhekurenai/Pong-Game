# 🏓 Pong Game — Classic Arcade Remake

**A two-player Pong remake built with Python's Turtle graphics library.**

![Python](https://img.shields.io/badge/python-3.x-blue)
![Library](https://img.shields.io/badge/library-turtle-green)
![Players](https://img.shields.io/badge/players-2-orange)
![Status](https://img.shields.io/badge/status-complete-brightgreen)

---

## Description

A faithful recreation of the 1972 Atari classic **Pong**, implemented in Python using the built-in `turtle` module. Two players control paddles on opposite sides of an 800×600 black canvas, bouncing a ball back and forth. Each time a player misses, the opponent scores a point. The ball speeds up slightly with each paddle hit, increasing the challenge over time.

---

## Gameplay

- Two players face off on the **same keyboard**
- The ball bounces off the top and bottom walls automatically
- Missing the ball gives the **opponent a point**
- The ball **speeds up** after each paddle hit — rallies get harder the longer they last
- Scores are displayed in large numbers at the top center of the screen

---

## Project Structure

```
Pong-Game/
├── main.py        # Screen setup, game loop, collision detection
├── paddle.py      # Paddle class: positioning and movement
├── bola.py        # Ball class: movement, bouncing, speed and reset
└── pontuacao.py   # Scoreboard class: tracks and displays both players' scores
```

---

## How it works

### `main.py`
Sets up the 800×600 black screen and initializes both paddles, the ball and the scoreboard. Runs the game loop continuously, handling four types of events each frame:

- **Wall collision** — if the ball's Y coordinate exceeds ±280, it bounces vertically.
- **Paddle collision** — if the ball is within 50 units of a paddle and past the ±320 X threshold, it bounces horizontally and accelerates.
- **Right miss** — ball goes past X = 380, left player scores and ball resets to center.
- **Left miss** — ball goes past X = -380, right player scores and ball resets to center.

### `bola.py`
The `Ball` class moves by adding `x_move` and `y_move` to its position each frame. On paddle bounce (`bounce_x`), the X direction inverts and `move_speed` is multiplied by `0.9` — making the ball progressively faster. On a miss, `reset_position` sends the ball back to center and restores base speed.

### `paddle.py`
The `Paddle` class is a 1×5 white rectangle positioned at a given coordinate. `go_up` and `go_down` shift it 20 units along the Y axis per keypress. There are no boundary limits — paddles can move off-screen.

### `pontuacao.py`
The `Placar` class maintains separate `l_score` and `r_score` counters, re-rendering both to the screen on every update. Scores are displayed in size-80 Courier font on the left and right sides of the top area.

---

## Instructions

### Requirements

- Python 3.x
- No external dependencies — `turtle` is part of the Python standard library

### Running the game

```bash
python main.py
```

### Controls

| Key | Player | Action |
|---|---|---|
| `↑` Arrow Up | Right player | Move paddle up |
| `↓` Arrow Down | Right player | Move paddle down |
| `W` | Left player | Move paddle up |
| `S` | Left player | Move paddle down |

---

## Known limitations

- **No winning condition** — the game runs indefinitely; there is no score limit or end screen.
- **Paddles have no boundary** — they can be moved off the visible canvas.
- **Single machine only** — both players share the same keyboard; no network play.
- The ball's `move_speed` attribute is set but not used to control the `time.sleep` delay (which was removed from the loop), so speed is tied directly to the `x_move`/`y_move` increment values.

---

## Author

**Gabriel Celestino** — [@gcelesti](https://github.com/gcelesti)
