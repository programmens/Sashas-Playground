import random
import math
import time
import os

# ===============================
# 1️⃣ GRAVITY SIMULATION
# ===============================

class Body:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass
        self.vx = 0
        self.vy = 0

class GravitySimulation:
    def __init__(self, width=60, height=20, bodies=5):
        self.width = width
        self.height = height
        self.G = 0.1
        self.bodies = [
            Body(random.uniform(0, width),
                 random.uniform(0, height),
                 random.uniform(5, 20))
            for _ in range(bodies)
        ]

    def update(self):
        for body in self.bodies:
            ax, ay = 0, 0
            for other in self.bodies:
                if body != other:
                    dx = other.x - body.x
                    dy = other.y - body.y
                    dist = math.sqrt(dx**2 + dy**2) + 0.1
                    force = self.G * body.mass * other.mass / (dist**2)
                    ax += force * dx / dist
                    ay += force * dy / dist

            body.vx += ax / body.mass
            body.vy += ay / body.mass
            body.x += body.vx
            body.y += body.vy

            body.x %= self.width
            body.y %= self.height

    def display(self):
        grid = [[" " for _ in range(self.width)] for _ in range(self.height)]
        for body in self.bodies:
            x = int(body.x)
            y = int(body.y)
            grid[y][x] = "O"
        print("\n".join("".join(row) for row in grid))


# ===============================
# 2️⃣ EPIDEMIC SIMULATION
# ===============================

class EpidemicSimulation:
    def __init__(self, size=20, infection_rate=0.25, recovery_rate=0.05):
        self.size = size
        self.grid = [["S" for _ in range(size)] for _ in range(size)]
        self.infection_rate = infection_rate
        self.recovery_rate = recovery_rate

        mid = size // 2
        self.grid[mid][mid] = "I"

    def update(self):
        new_grid = [row[:] for row in self.grid]

        for y in range(self.size):
            for x in range(self.size):
                if self.grid[y][x] == "I":
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < self.size and 0 <= ny < self.size:
                                if self.grid[ny][nx] == "S":
                                    if random.random() < self.infection_rate:
                                        new_grid[ny][nx] = "I"

                    if random.random() < self.recovery_rate:
                        new_grid[y][x] = "R"

        self.grid = new_grid

    def display(self):
        print("\n".join(" ".join(row) for row in self.grid))


# ===============================
# 3️⃣ TRAFFIC FLOW SIMULATION
# ===============================

class TrafficSimulation:
    def __init__(self, length=50, density=0.3):
        self.length = length
        self.road = ["." for _ in range(length)]
        for i in range(length):
            if random.random() < density:
                self.road[i] = "C"

    def update(self):
        new_road = ["." for _ in range(self.length)]

        for i in range(self.length):
            if self.road[i] == "C":
                next_pos = (i + 1) % self.length
                if self.road[next_pos] == ".":
                    new_road[next_pos] = "C"
                else:
                    new_road[i] = "C"

        self.road = new_road

    def display(self):
        print("".join(self.road))


# ===============================
# 4️⃣ ECOSYSTEM SIMULATION
# ===============================

class EcosystemSimulation:
    def __init__(self, size=20):
        self.size = size
        self.grid = [["." for _ in range(size)] for _ in range(size)]

        for _ in range(40):
            x = random.randint(0, size-1)
            y = random.randint(0, size-1)
            self.grid[y][x] = "R"  # Rabbit

        for _ in range(10):
            x = random.randint(0, size-1)
            y = random.randint(0, size-1)
            self.grid[y][x] = "F"  # Fox

    def update(self):
        new_grid = [row[:] for row in self.grid]

        for y in range(self.size):
            for x in range(self.size):
                if self.grid[y][x] == "F":
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < self.size and 0 <= ny < self.size:
                                if self.grid[ny][nx] == "R":
                                    new_grid[ny][nx] = "F"

        self.grid = new_grid

    def display(self):
        print("\n".join(" ".join(row) for row in self.grid))


# ===============================
# MAIN MENU
# ===============================

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def run_simulation(sim):
    for _ in range(100):
        clear()
        sim.display()
        sim.update()
        time.sleep(0.1)

def main():
    while True:
        print("\n🪐 Simulation Playground")
        print("1. Gravity Simulation")
        print("2. Epidemic Spread")
        print("3. Traffic Flow")
        print("4. Ecosystem Evolution")
        print("5. Quit")

        choice = input("Select simulation: ")

        if choice == "1":
            run_simulation(GravitySimulation())
        elif choice == "2":
            run_simulation(EpidemicSimulation())
        elif choice == "3":
            run_simulation(TrafficSimulation())
        elif choice == "4":
            run_simulation(EcosystemSimulation())
        elif choice == "5":
            break


if __name__ == "__main__":
    main()
