# Bouncing Balls (Python + Tkinter)

A simple little physics/animation project written in **pure Python** using **Tkinter**.  
Two colored balls bounce around inside a window, colliding with the walls and each other with basic elastic collision logic.

Great as:

- A starter GUI project
- A simple physics demo
- A portfolio/example of object-oriented Python + animation

---

## Features

- **Two balls** with independent positions and velocities
- Smooth animation using Tkinter’s `after()` callback (~60 FPS)
- **Wall collisions** on all four sides
- **Ball–ball collisions** using a simple elastic collision model for equal masses
- Clean, object-oriented structure:
  - `Ball` class for drawing & moving a ball
  - `BouncingBallsApp` for window, canvas, and game loop

---

## Requirements

- Python **3.x**
- Tkinter (bundled with most standard Python installs)

To check if Tkinter is available:

```bash
python -m tkinter
