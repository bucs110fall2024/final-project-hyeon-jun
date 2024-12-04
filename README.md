
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Project Title >>
## CS110 Final Project  << Semester, Year >>

CS110 Final Project Fall, 2024
## Team Members

Hyeon-Jun Cha

***

## Project Description

Platformer Game

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Player movement: left, right, and jumping.
2. Basic platform collision detection.
3. Modular codebase following the MVC design pattern.
4. Gravity simulation for realistic jumps.
5. Multiple levels with progressively harder platform layouts.

### Classes

- **Player**: Handles the player's movement, jumping, gravity, and collision detection.
- **Platform**: Represents static platforms the player can stand on.
- **Controller**: Manages the game loop, input handling, and overall game logic.
- **View**: Handles the rendering of all visual elements, including the background, player, and platforms.
- **Settings**: Stores global constants and configuration values for easy adjustments.

## ATP

|| Step                 | Procedure            | Expected Results                   |
|----------------------|:--------------------:|-----------------------------------:|
| 1                    | Run the Platformer Game program | The GUI window appears, showing the player and platforms |
| 2                    | Move left or right using arrow keys | The player moves left or right accordingly |
| 3                    | Press the spacebar to jump | The player jumps upwards and lands back on a platform |
| 4                    | Move the player off the edge of the platform | The player falls due to gravity |
| 5                    | Collision with platform | The player stops falling and stands on the platform |
| 6                    | Close the game window | The game closes without errors |