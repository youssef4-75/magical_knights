from pygame import Color, Rect, Surface
from screen import Window
from typing import Callable, Any, Protocol

# Option 1: Using Protocol for type safety
class Observable(Protocol):
    def get_value(self) -> int: ...
    def get_max(self) -> int: ...

class Displayer:
    def __init__(self, 
                 win: Window, 
                 bg_color: Color, 
                 color: Color, 
                 rect: Rect, 
                 /, 
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
        self.max = max_provider()
        self._value_provider = value_provider
        self._max_provider = max_provider
    
    @property
    def current_value(self) -> int:
        """Get current value from injected provider"""
        return self._value_provider()
    
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
