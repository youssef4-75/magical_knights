from pygame import Color, Rect, Surface
import pygame as pg
from screen import Window
from typing import Callable

pg.font.init()



class Displayer:
    def __init__(self, 
                 win: Window, 
                 bg_color: Color, 
                 color: Color, 
                 rect: Rect, 
                 /, 
                 observable_obj,
                 value_provider: Callable[[], int],  # Injected function that returns current value
                 max_provider: Callable[[], int] | None = None):
        """
        Args:
            value_provider: Function that returns the current value to display
            max_provider: Optional function that returns the max value (uses self.max if None)
        """
        self.color = color
        self.bg = bg_color
        self.rect = rect
        self.window = win
        self.max = max_provider() if max_provider else 100
        self._observable = observable_obj
        self._value_provider = value_provider
        self._max_provider = max_provider

        self._message = ""
        self._duration = 0
    
    @property
    def current_value(self) -> int:
        """Get current value from injected provider"""
        return self._value_provider(self._observable)
    
    @property
    def max_value(self) -> int:
        """Get max value from injected provider or fallback"""
        if self._max_provider:
            return self._max_provider()
        return self.max
    
    def display(self) -> None:
        """Display the current state without manual setting"""
        # Calculate percentage
        percentage = self.current_value / self.max_value if self.max_value > 0 else 0
        
        # Create background surface
        bg_surf = Surface((self.rect.width, self.rect.height))
        bg_surf.fill(self.bg)
        
        # Create foreground surface (filled portion)
        fill_width = int(self.rect.width * percentage)
        if fill_width > 0:
            fill_surf = Surface((fill_width, self.rect.height))
            fill_surf.fill(self.color)
            bg_surf.blit(fill_surf, (0, 0))
        
        # Draw to window
        self.window.draw(bg_surf, self.rect)

        self.display_text()

    def show_info(self, message: str, duration: int):
        self._message = message
        self._duration = duration
        
    def display_text(self):
        print(self._duration)
        if self._duration <= 0: return
        font = pg.font.Font(None, 24)
        text_surf = font.render(self._message, True, (255, 255, 255), bgcolor=(0, 0, 0))
        text_rect = text_surf.get_rect(midbottom=(self.rect.centerx , self.rect.centery))
        self.window.draw(text_surf, text_rect)
        self._duration -= 1
