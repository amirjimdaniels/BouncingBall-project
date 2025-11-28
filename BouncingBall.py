import tkinter as tk
import math
import random

class Ball:
    def __init__(self, canvas, x, y, vx, vy, radius=20, color="white"):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.color = color

        self.id = canvas.create_oval(
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
            fill=self.color,
            outline=""
        )

    def update_position(self):
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        self.canvas.coords(
            self.id,
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius
        )


class BouncingBallsApp:
    def __init__(self, width=600, height=400):
        self.width = width
        self.height = height

        self.root = tk.Tk()
        self.root.title("Bouncing Balls with Collision")

        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="black")
        self.canvas.pack()

        # Press Esc to quit
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        # Create two balls
        self.balls = []
        self.create_balls()

        self.animate()

    def create_balls(self):
        # Ball 1
        b1 = Ball(
            self.canvas,
            x=self.width // 3,
            y=self.height // 2,
            vx=4,
            vy=3,
            radius=25,
            color="cyan"
        )

        # Ball 2
        b2 = Ball(
            self.canvas,
            x=2 * self.width // 3,
            y=self.height // 2,
            vx=-3,
            vy=-4,
            radius=25,
            color="magenta"
        )

        self.balls.append(b1)
        self.balls.append(b2)

    def animate(self):
        # Update positions
        for ball in self.balls:
            ball.update_position()
            self.handle_wall_collision(ball)

        # Handle ball-ball collision
        if len(self.balls) >= 2:
            self.handle_ball_collision(self.balls[0], self.balls[1])

        # Redraw
        for ball in self.balls:
            ball.draw()

        # Next frame
        self.root.after(16, self.animate)  # ~60 FPS

    def handle_wall_collision(self, ball: Ball):
        # Left / right walls
        if ball.x - ball.radius <= 0 and ball.vx < 0:
            ball.vx = -ball.vx
        if ball.x + ball.radius >= self.width and ball.vx > 0:
            ball.vx = -ball.vx

        # Top / bottom walls
        if ball.y - ball.radius <= 0 and ball.vy < 0:
            ball.vy = -ball.vy
        if ball.y + ball.radius >= self.height and ball.vy > 0:
            ball.vy = -ball.vy

    def handle_ball_collision(self, b1: Ball, b2: Ball):
        dx = b2.x - b1.x
        dy = b2.y - b1.y
        dist = math.hypot(dx, dy)
        min_dist = b1.radius + b2.radius

        if dist == 0:
            # Prevent divide-by-zero if perfectly overlapping
            return

        if dist < min_dist:
            # Normalize the vector between centers
            nx = dx / dist
            ny = dy / dist

            # Relative velocity
            dvx = b1.vx - b2.vx
            dvy = b1.vy - b2.vy

            # Velocity component along the normal
            rel_vel_along_normal = dvx * nx + dvy * ny

            # If they're moving apart, skip
            if rel_vel_along_normal > 0:
                return

            # Elastic collision for equal masses:
            # We just swap the normal components of velocity
            impulse = -rel_vel_along_normal

            b1.vx += -impulse * nx
            b1.vy += -impulse * ny
            b2.vx += impulse * nx
            b2.vy += impulse * ny

            # Position correction so they don't stay stuck together:
            overlap = min_dist - dist
            correction = overlap / 2
            b1.x -= nx * correction
            b1.y -= ny * correction
            b2.x += nx * correction
            b2.y += ny * correction

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = BouncingBallsApp()
    app.run()
