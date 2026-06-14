import math
from random import randint
from typing import Any

class Vector:
    """A 2D vector class for game development with common vector operations."""
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    # Basic operations
    def __add__(self, other: 'Vector'|Any) -> Vector:
        """Add two vectors: v1 + v2"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return Vector(self.x + other, self.y + other)
    
    def __sub__(self, other: 'Vector'):
        """Subtract two vectors: v1 - v2"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return Vector(self.x - other, self.y - other)
    
    def __mul__(self, other: 'Vector'):
        """Multiply vector by scalar: v * scalar"""
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y)
        return Vector(self.x * other, self.y * other)
    
    def __rmul__(self, other: 'Vector'):
        """Scalar multiplication: scalar * v"""
        return self.__mul__(other)
    
    def __truediv__(self, scalar):
        """Divide vector by scalar: v / scalar"""
        if scalar != 0:
            return Vector(self.x / scalar, self.y / scalar)
        return Vector(0, 0)
    
    def __neg__(self):
        """Negate vector: -v"""
        return Vector(-self.x, -self.y)
    
    def __eq__(self, other: 'Vector'):
        """Check equality: v1 == v2"""
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __getitem__(self, index):
        """Allow indexing: v[0] for x, v[1] for y"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Vector index out of range")
    
    def __len__(self):
        return 2
    
    # Vector operations
    def magnitude(self):
        """Calculate the magnitude (length) of the vector."""
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def magnitude_squared(self):
        """Calculate squared magnitude (useful for comparisons to avoid sqrt)."""
        return self.x ** 2 + self.y ** 2
    
    def normalize(self):
        """Return a normalized unit vector (length = 1)."""
        mag = self.magnitude()
        if mag == 0:
            return Vector(0, 0)
        return Vector(self.x / mag, self.y / mag)
    
    def normalize_ip(self):
        """Normalize the vector in-place."""
        mag = self.magnitude()
        if mag != 0:
            self.x /= mag
            self.y /= mag
        return self
    
    def dot(self, other: 'Vector'):
        """Calculate dot product: v1 · v2"""
        return self.x * other.x + self.y * other.y
    
    def cross(self, other: 'Vector'):
        """Calculate cross product (2D scalar cross product)."""
        return self.x * other.y - self.y * other.x
    
    def distance_to(self, other: 'Vector'):
        """Calculate distance to another vector."""
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)
    
    def distance_squared_to(self, other: 'Vector'):
        """Calculate squared distance to another vector."""
        dx = self.x - other.x
        dy = self.y - other.y
        return dx * dx + dy * dy
    
    def angle_to(self, other: 'Vector'):
        """Calculate angle (in radians) between this vector and another."""
        dot_product = self.dot(other)
        mag_product = self.magnitude() * other.magnitude()
        if mag_product == 0:
            return 0
        cos_angle = dot_product / mag_product
        cos_angle = max(-1, min(1, cos_angle))  # Clamp to avoid floating point errors
        return math.acos(cos_angle)
    
    def angle(self):
        """Calculate angle of the vector in radians (from positive x-axis)."""
        return math.atan2(self.y, self.x)
    
    def rotate(self, angle):
        """Rotate vector by angle (in radians)."""
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        return Vector(
            self.x * cos_a - self.y * sin_a,
            self.x * sin_a + self.y * cos_a
        )
    
    def rotate_ip(self, angle):
        """Rotate vector in-place by angle (in radians)."""
        new = self.rotate(angle)
        self.x = new.x
        self.y = new.y
        return self
    
    def limit(self, max_magnitude):
        """Limit the vector magnitude to max_magnitude."""
        if self.magnitude_squared() > max_magnitude ** 2:
            return self.normalize() * max_magnitude
        return Vector(self.x, self.y)
    
    def limit_ip(self, max_magnitude):
        """Limit the vector magnitude in-place."""
        if self.magnitude_squared() > max_magnitude ** 2:
            norm = self.normalize()
            self.x = norm.x * max_magnitude
            self.y = norm.y * max_magnitude
        return self
    
    def lerp(self, target, t):
        """Linear interpolation between this vector and target (t between 0 and 1)."""
        t = max(0, min(1, t))
        return Vector(
            self.x + (target.x - self.x) * t,
            self.y + (target.y - self.y) * t
        )
    
    def project_onto(self, other: 'Vector'):
        """Project this vector onto another vector."""
        other_normalized = other.normalize()
        dot_product = self.dot(other_normalized)
        return other_normalized * dot_product
    
    def reflect(self, normal):
        """Reflect vector off a surface with given normal."""
        dot_product = self.dot(normal) * 2
        return Vector(
            self.x - normal.x * dot_product,
            self.y - normal.y * dot_product
        )
    
    # Class methods
    @classmethod
    def from_angle(cls, angle, magnitude=1):
        """Create a vector from an angle (in radians) and optional magnitude."""
        return cls(math.cos(angle) * magnitude, math.sin(angle) * magnitude)
    
    @classmethod
    def zero(cls):
        """Return a zero vector."""
        return cls(0, 0)
    
    @classmethod
    def one(cls):
        """Return a vector of ones."""
        return cls(1, 1)
    
    @classmethod
    def up(cls):
        """Return up direction vector."""
        return cls(0, -1)
    
    @classmethod
    def down(cls):
        """Return down direction vector."""
        return cls(0, 1)
    
    @classmethod
    def left(cls):
        """Return left direction vector."""
        return cls(-1, 0)
    
    @classmethod
    def right(cls):
        """Return right direction vector."""
        return cls(1, 0)
    
    @classmethod
    def random(cls, max_X, max_Y):
        """return a random vector"""
        return cls(randint(0, max_X), randint(0, max_Y))
        
    # Conversion methods
    def to_tuple(self):
        """Convert to tuple (x, y)."""
        return (self.x, self.y)
    
    def to_int_tuple(self):
        """Convert to integer tuple (int(x), int(y))."""
        return (int(self.x), int(self.y))
    
    def copy(self):
        """Create a copy of the vector."""
        return Vector(self.x, self.y)
    
    def set(self, x, y):
        """Set vector components."""
        self.x = x
        self.y = y
        return self


# Example usage with Pygame-CE
if __name__ == "__main__":
    # Test the vector class
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    
    print(f"v1: {v1}")
    print(f"v2: {v2}")
    print(f"v1 + v2: {v1 + v2}")
    print(f"v1 - v2: {v1 - v2}")
    print(f"v1 * 3: {v1 * 3}")
    print(f"Magnitude of v1: {v1.magnitude()}")
    print(f"Normalized v1: {v1.normalize()}")
    print(f"Dot product: {v1.dot(v2)}")
    print(f"Distance between v1 and v2: {v1.distance_to(v2)}")
    print(f"Angle of v1: {math.degrees(v1.angle())}°")
    print(f"v1 rotated by 90°: {v1.rotate(math.pi/2)}")
    
    # Pygame integration example
    import pygame
    import sys
    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    position = Vector(400, 300)
    velocity = Vector(0, 0)
    acceleration = Vector(0, 0.5)  # Gravity
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Simple movement with vectors
        keys = pygame.key.get_pressed()
        acceleration = Vector(0, 0.5)  # Reset acceleration
        
        if keys[pygame.K_LEFT]:
            acceleration.x = -5
        if keys[pygame.K_RIGHT]:
            acceleration.x = 5
        if keys[pygame.K_SPACE] and position.y > 550:
            velocity.y = -15
        
        # Update physics
        velocity += acceleration
        position += velocity
        
        # Bounce off walls
        if position.x < 0 or position.x > 800:
            velocity.x *= -0.8
            position.x = max(0, min(800, position.x))
        if position.y > 580:
            velocity.y *= -0.8
            position.y = 580
        
        # Draw
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), position.to_int_tuple(), 20)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()