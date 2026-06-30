# pygame_env

A personal Pygame extension library by **youssef4-75**. It sits on top of [Pygame](https://www.pygame.org/) and provides reusable classes and patterns so you can focus on game logic instead of rebuilding the same foundations every time.

The included demo **Magical Knights** is a four-player arena example — movement, spells, projectiles, and collisions are all handled through the library's object, interaction, and plugin systems.

## Why this exists

Starting a Pygame project from scratch means reimplementing the same pieces over and over: a game loop, entity management, input handling, collision response, HUD hooks, and animation loading. **pygame_env** packages those concerns into composable building blocks. You extend the library where your game differs; the boilerplate stays out of your way.

## Features

- **Composable game objects** — Build entities from essential mixins (motion, shape, life, interaction, consciousness) and synthetic mixins (projectiles, balls).
- **Interaction registry** — Type-pair dispatch for collisions (player vs player, energy vs material, etc.) with a spatial sweep algorithm that keeps interaction cost manageable as object count grows.
- **Plugin system** — Extend rendering and game logic without touching the core loop (backgrounds, HUD displayers, and more).
- **Action / grimoire system** — Bind keyboard combos to mana-cost actions with cooldowns and initial delays.
- **Animation support** — Load sprite sequences from directories and attach them to players.
- **Packaging** — PyInstaller spec included for building a standalone executable.

## Requirements

- Python 3.12+ (the codebase uses modern type syntax such as `class Lake[E]`)
- [Pygame](https://www.pygame.org/) (tested with pygame-ce 2.5.x)

```bash
pip install pygame
```

or if it did not work, try the community edition:

```bash
pip install pygame-ce
```

## Quick start

Clone the repository, install Pygame, then run from the project root:

```bash
# Recommended — modular example (players, actions, plugins in _test/game_1/)
python __test__.py

# Single-file demo — everything inline in main.py
python main.py
```

### Controls (default demo)


| Player | Move          | Actions (game_1 example)   |
| ------ | ------------- | -------------------------- |
| 1      | Arrow keys    | `I` spawn material block   |
| 2      | W / A / S / D | `O` jump, `P` shoot energy |
| 3      | Y / G / H / J | —                          |
| 4      | F / C / V / B | —                          |


Close the window to quit.

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                      GameManager                        │
│  (Window + Lake + Plugins)                              │
├─────────────────────────────────────────────────────────┤
│  loop():                                                │
│    1. activate plugins (background, HUD, …)             │
│    2. for each object in lake → draw + act (if conscious)│
│    3. lake.interaction()  — collision detection + dispatch│
│    4. lake.garbage_collect()                            │
│    5. window.display()                                  │
└─────────────────────────────────────────────────────────┘
         │                    │                    │
         ▼                    ▼                    ▼
    ┌─────────┐        ┌─────────────┐      ┌──────────────┐
    │ Plugins │        │    Lake     │      │    Window    │
    │ (render │        │ (objects +  │      │ (pygame      │
    │  hooks) │        │  spatial    │      │  display)    │
    └─────────┘        │  ordering)  │      └──────────────┘
                       └─────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │ Interaction      │
                    │ Registry         │
                    │ (type-pair map)  │
                    └──────────────────┘
```

### Core concepts

**Game objects** (`objects/`) inherit from `GameObject`, which composes motion, shape, life, and interaction behavior. Conscious entities (players) additionally mix in `ConsciousMixin` for movement and spell casting.

**Natures** (`objects/natures/`) are concrete entity types:


| Class      | Role                                                     |
| ---------- | -------------------------------------------------------- |
| `Player`   | Controllable character with HP, MP, and keyboard actions |
| `Energy`   | Projectile that damages on contact                       |
| `Material` | Static obstacle that absorbs energy hits                 |


**Mixins** (`objects/mixins/`):

- *Essence* — `MotionMixin`, `ShapeMixin`, `LifeMixin`, `InteractionMixin`, `ConsciousMixin`
- *Synthetic* — `ProjectileMM`, `BallSM` (crafted behaviors layered on top of essence mixins)

**Interaction registry** (`interaction_registry/`) maps pairs of type identifiers to handler functions. Handlers are registered with the `@register` decorator. When two objects collide, the registry dispatches the matching handler; if none exists, a default repulsion force is applied.

**Plugins** (`plugins/`) hook into the render phase each frame. Built-in plugins include `WithBackGround` and `WithPDisplayer` (HP bars for players).

**Lake** (`game/container/`) holds all live objects. `ObjectsContainer` extends a spatially ordered lake that sweeps along X and Y axes to find colliding pairs efficiently, then runs interaction handlers and removes dead objects.

## Creating a new game

To build a new game on top of pygame_env, you typically only need to modify or add code in these areas:


| Area                                            | Purpose                                                           |
| ----------------------------------------------- | ----------------------------------------------------------------- |
| `objects/natures/`                              | New entity types (subclass `GameObject`, define `typeIdentifier`) |
| `objects/mixins/synthetic/`                     | Reusable crafted behaviors (projectiles, special shapes, etc.)    |
| `interaction_registry/interactions_dictionary/` | Collision handlers between type pairs                             |
| `plugins/`                                      | Rendering and per-frame logic extensions                          |
| `_main/` or `main.py`                           | Game setup — window, players, plugins, game loop                  |
| `__main__.py`                                   | Entry point for running or packaging the game                     |


### Minimal setup pattern

```python
import pygame as pg
from game import GameManager
from objects import Player
from plugins import WithBackGround, WithPDisplayer
from utils import Animation, Vector, consolify, from_root, PLAYER_SIZE

win_size = (800, 600)
game = GameManager.init("My Game", win_size)

controls = consolify(pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT)
anim = Animation.from_directory(from_root("assets/anim_set01/0x1"), PLAYER_SIZE)

@game.add
def player():
    p = Player("hero", "red", Vector.random(*win_size).to_tuple(), controls)
    p.attach_animation(anim)
    return p

game.add_plugin(
    WithBackGround(from_root("assets/bg1.png")),
    WithPDisplayer(),
)

while game.running:
    for event in game.key_events():
        pass
    game.loop()
```

### Adding a custom action

```python
from utils import Vector

@player.my_action(pg.K_SPACE, mana=10, cooldown=60, initial_delay=0)
def dash(player, **ctx):
    player.add_accel(15 * Vector.up())
```

Or define actions in a shared grimoire dict using `actionify_deco` and attach them with `attach_grimoire` (see `_test/game_1/actions.py`).

### Registering a new interaction

```python
# interaction_registry/interactions_dictionary/my_handler.py
from .tools import register
from utils import MY_CLASS, OTHER_CLASS

@register(MY_CLASS, OTHER_CLASS)
def my_handler(obj_a, obj_b):
    ...
```

Then import the module in `interaction_registry/interactions_dictionary/__init__.py`.

## Project structure

```
pygame_env/
├── assets/                  # Sprites, backgrounds, animation tile sets
├── game/                    # Engine — GameManager, window, lake, plugins
├── objects/                 # GameObject, natures, mixins
├── interaction_registry/    # Collision dispatch system
├── plugins/                 # Built-in plugins (background, player HUD)
├── types_tools/             # Action and ObjectCreator type aliases
├── utils/                   # Vector, animation, path helpers, game constants
├── _test/game_1/            # Modular example game (recommended reference)
├── main.py                  # Single-file demo
├── __main__.py              # Entry point (demo + PyInstaller)
├── __test__.py              # Alternate launcher for the modular example
├── pygame_env.spec          # PyInstaller build configuration
└── current.md               # Notes on extension points for new games
```

## Building a standalone executable

```bash
pip install pyinstaller
pyinstaller pygame_env.spec
```

This bundles `assets/` and builds a windowed executable at `dist/pygame_env.exe`. The spec uses `__main__.py` as the entry script, which launches the modular `game_1` demo.

## Related documentation

- `current.md` — Which modules to touch when creating a new game.
- `sketch.md` — Early design notes on mixins and object hierarchy.

