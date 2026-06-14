import pygame
from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional, List, Any, Dict, Set
from dataclasses import dataclass
from collections import defaultdict






# Example usage
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    # Create game object manager
    manager = GameObjectManager()
    
    # Create player object
    player = GameObject("Player", Vector(400, 300))
    
    # Add components
    sprite_renderer = SpriteRenderer(player, pygame.Surface((50, 50)))
    sprite_renderer.image.fill((0, 255, 0))  # Green square
    player.add_component(sprite_renderer)
    
    movement = MovementComponent(player, speed=200)
    player.add_component(movement)
    
    collider = CircleCollider(player, radius=25)
    player.add_component(collider)
    
    player.add_tag("player")
    player.add_tag("movable")
    
    # Create enemy object
    enemy = GameObject("Enemy", Vector(100, 100))
    enemy_sprite = SpriteRenderer(enemy, pygame.Surface((40, 40)))
    enemy_sprite.image.fill((255, 0, 0))  # Red square
    enemy.add_component(enemy_sprite)
    enemy.add_tag("enemy")
    
    # Add to manager
    manager.add(player)
    manager.add(enemy)
    
    # Game loop
    running = True
    while running:
        delta_time = clock.tick(60) / 1000.0  # Convert to seconds
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            manager.handle_event(event)
        
        # Handle input
        keys = pygame.key.get_pressed()
        movement.velocity = Vector(0, 0)
        if keys[pygame.K_LEFT]:
            movement.velocity.x = -movement.speed
        if keys[pygame.K_RIGHT]:
            movement.velocity.x = movement.speed
        if keys[pygame.K_UP]:
            movement.velocity.y = -movement.speed
        if keys[pygame.K_DOWN]:
            movement.velocity.y = movement.speed
        
        # Update
        manager.update(delta_time)
        
        # Render
        screen.fill((0, 0, 0))
        
        # Simple rendering (in real project, use a proper rendering system)
        for obj in manager._game_objects:
            renderer = obj.get_component(SpriteRenderer)
            if renderer:
                renderer.render(screen)
        
        pygame.display.flip()
    
    pygame.quit()