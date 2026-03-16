# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the Games

```bash
open shooter.html       # top-down shooter
open tictactoe.html     # browser tic-tac-toe
python3 tictactoe.py    # terminal tic-tac-toe
```

## Git Workflow

After every change, commit and push to GitHub:

```bash
git add <file>
git commit -m "descriptive message"
git push
```

Remote: https://github.com/RakshitM42/ClaudeCodeTest

## Project Structure

All games are self-contained single files — no build step, no dependencies, no package manager.

- **`shooter.html`** — Full game in one HTML file: CSS, canvas rendering, and all JS inline.
- **`tictactoe.html`** — Browser tic-tac-toe with score tracking, CSS animations, inline JS.
- **`tictactoe.py`** — Terminal tic-tac-toe, no dependencies.

## shooter.html Architecture

The game is structured around a state machine (`MENU → PLAYING → GAME_OVER`) and a `requestAnimationFrame` loop.

**Key globals:** `player`, `enemies[]`, `bullets[]`, `particles[]`, `waveManager`, `state`, `score`, `levelIdx`.

**Classes:** `Player`, `Enemy`, `Bullet`, `Particle`, `WaveManager` — all instantiated fresh on `startGame()`.

**Config:** All tunable constants live in the top-level `CFG` object (fire rate, speed, HP, radii). Level/wave definitions are in the `LEVELS` array — each level has 3 waves, each wave lists enemy types and counts.

**Enemy types** (`ENEMY_DEFS`): A=Chaser, B=Shooter (fires bullets), C=Tank (melee damage on contact), D=Swarm (flocking). Behavior is a `switch` on `this.type` inside `Enemy.update()`.

**Rendering:** Pure Canvas 2D, no images. `drawBackground()` draws the tile grid; sprites are built from `fillRect` calls. Particles handle both spark explosions and floating score text.

**dt normalization:** `dt` is capped at 50 ms per frame; all movement scales as `velocity * dt / 16` (normalized to ~60 fps). Animation uses raw `gameTick` counter.

## Conventions

- No external libraries, no CDN links — everything must work offline by opening the HTML file directly.
- Canvas size for shooter is fixed at `800×600` (`W`, `H` constants).
- Collision detection is circle vs circle for all entities.
