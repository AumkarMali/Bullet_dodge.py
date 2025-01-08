# Block Dodge Game
A fast-paced arcade-style game where players must dodge and shoot various types of bullets while surviving as long as possible. Built with Pygame, this game features dynamic difficulty progression, multiple bullet types, and an engaging scoring system.

## Game Features
- **Dynamic Player Controls**: Smooth acceleration-based movement using arrow keys
- **Multiple Bullet Types**:
  - Normal Bullets: Basic projectiles that follow predictable patterns
  - Shotgun Bullets: Dual projectiles that approach from both directions
  - Sniper Bullets: High-speed projectiles with warning indicators
- **Combat System**: 
  - Player can shoot bullets using the 'F' key
  - Two-way shooting system with upper and lower bullet positions
  - Collision detection for bullet-to-bullet and bullet-to-player interactions
- **Progressive Difficulty**: 
  - Increasing bullet speeds over time
  - New bullet types unlock at specific score thresholds
  - Dynamic bullet patterns that adapt to player position
- **Health System**: 
  - Three lives represented by heart icons
  - Visual damage feedback when hit
  - Progressive score tracking

## Technical Implementation

### Core Components
- **Physics Engine**: Custom acceleration-based movement system with momentum
- **Collision System**: Rectangle-based collision detection for all game objects
- **Audio Integration**: 
  - Background music with fade-in effect
  - Sound effects for collisions, shots, and game events
  - Multiple audio channels for simultaneous sound playback

### Graphics
- **Real-time Rendering**: 60 FPS display update
- **Visual Effects**:
  - Air trail effects during movement
  - Damage state visualization
  - Warning indicators for sniper bullets
- **UI Elements**:
  - Score display
  - Lives counter with heart icons
  - Bullet type indicator
  - Game start countdown
  - Game over screen

## Dependencies
- Pygame
- Pygame Mixer (for audio)

## Installation
1. Ensure Python is installed on your system
2. Install Pygame:
```bash
pip install pygame
```
3. Place required assets in the game directory:
   - heart.png
   - Bullet.png
   - BackgroundMusic.mp3
   - Ricochet_sound.mp3
   - Bounce.mp3
   - BulletSFX.mp3
   - Explode sound effect.mp3
   - Count_down.mp3
   - Game_over.mp3

## Controls
- **Arrow Keys**: Move player
- **F**: Fire bullets
- Close window to exit game

## Game Mechanics
1. **Movement**: Player moves with momentum-based physics
2. **Survival**: Dodge incoming bullets and survive as long as possible
3. **Combat**: Shoot enemy bullets to earn extra points
4. **Progression**: Game difficulty increases with time:
   - Level 30: Unlocks shotgun bullets
   - Level 59: Unlocks sniper bullets

## Contributing
Feel free to fork the repository and submit pull requests with improvements or bug fixes.

## License
[Add your preferred license here]

## Acknowledgments
- Built with Pygame
- Sound effects and music attributions [Add sources if applicable]
