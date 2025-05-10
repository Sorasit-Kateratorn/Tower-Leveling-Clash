# Tower Leveling Clash

## 1.Project Overview
**Tower Leveling Clash** is a PVE (Player vs. Environment) turn-based card game where players ascend a multi-floor tower, battling enemies that grow stronger with each floor. The game follows a roguelike elimination rule: if a character dies, the game is over for that run.

## Mechanics & Functionality

- **Floor-based Progression**  
  Each floor contains 3 enemies with increasing strength.

- **Turn-based Combat**  
  The player and enemies take turns using cards to attack, defend, or apply special effects.

- **Shop & Economy System**  
  - Players earn 15 coins per floor.  
  - A shop is available where players can buy items.  
  - The shop contains 5 items at a time.  
  - If a player buys an item, it will be replaced with a new one to maintain 5 items in stock.

- **Inventory System**  
  - Players can collect and store many items.  
  - Before each enemy battle, the player selects one item from their inventory to use in combat.

- **Victory Condition**  
  - The game ends when the player clears all floors or when the character dies during a run.




## 2. Project Review

This project was inspired by **Mizuno Duel** (a Discord bot), a turn-based card battle game implemented as a Discord bot. In Mizuno Duel, players engage in PvP battles using text-based commands, and they can choose from three characters to play. Additionally, it features a shop system where players can purchase new characters if one is lost.

## Key Enhancements in Tower Leveling Clash

### Graphical User Interface (GUI) Instead of Text-Based Commands

- **Mizuno Duel** operates entirely through Discord text commands, which can make gameplay slower and harder to visualize.
- **Tower Leveling Clash** will use **Pygame** to provide a graphical UI, making characters more realistic, gameplay easier to understand, and interactions more intuitive.

### Single Character Selection & Permanent Death Mechanic

- In **Mizuno Duel**, the player has access to three characters and can switch between them during battles.
- In **Tower Leveling Clash**, players select **only one character** and play until they clear all floors.
- If the character's health reaches 0, they are **permanently lost**, and the game is over for that run.
- This adds a higher level of **strategy and risk management** compared to Mizuno Duel.

### Expanded Shop System with Items

- In **Mizuno Duel**, the shop only sells new characters, allowing players to replace lost ones.
- In **Tower Leveling Clash**, the shop introduces a more dynamic and strategic system by offering **various items** instead of characters, making **economy management** a key part of the gameplay.

  Includes:
  - **Power-ups** that enhance characters (e.g., health boosts, attack buffs).
  - **Consumable items** that can be used in battle. This adds more depth to the economy system, giving players **strategic choices** between saving coins or purchasing useful items.


## 3. Programming Development

### 3.1 Game Concept

**Game Flow:**

1. **Start Game** → The player selects a character.  
2. **Battle Phase** → The player battles one of three enemies on the current floor.  
   - If the player wins, they move on to the next enemy or advance to the next floor.  
3. **Earn 15 Coins per Floor** → Players can spend them in the shop for new items.  
4. **Cycle Repeats** until the player clears all floors or their character dies.

**Selling Points:**

- **Roguelike Gameplay** → Each run is unique due to randomized enemies and shop items.  
- **Strategic Turn-Based Combat** → Players must choose attacks, use items wisely, and adapt to enemy strategies.

---

### 3.2 Object-Oriented Programming Implementation

**Key OOP Improvements:**

- Separation of concerns through dedicated classes:
  - `Character`, `Inventory`, `Item`, `Shop`, `GameStats`, `GamePlay`, and `GamePlayUI`
- Improved game state management.
- Easier to expand features (e.g., new enemies, shop items) without modifying core logic.

---

#### `Class Shop`: Stores 5 items in the shop. When a user buys one, a new item is generated to refill the slot.

#### `Class Character`: Manages character stats and actions in battle.

#### `Class Item`: Stores all details for usable items in the game.

#### `Class GamePlay`: Manages the main game loop, floor progression, and win/loss conditions.  Save data for each round into a `GameStats` class, enabling easy expansion for features like inventory or achievements tracking.

#### `Class Inventory`: Manages the player’s coins and items available for use in battle.

#### `Class GamePlayUI`: Renders all graphical components and interfaces for user interaction.

#### `Class GameStats` : Collects gameplay data and exports it to a CSV file for analysis or visualization.

#### `Class AvgAttackPerFloorChart, ReachPercentChart,EarnPerFloorChart, KillChart, SpendDistributionChart, TimeSpentPerFloorChart, FloorStatsTable`  : Each class generates a specific graph or summary table using Matplotlib. Used to visualize game statistics after multiple sessions.

#### `Class Sound` : Manages background music and sound effects throughout the game.

#### `Class Config` : Stores global configuration constants such as screen size, grid size, and color themes.

#### `Class Background` : Handles loading and drawing background images for each screen

## 3.3 Algorithms Involved

- **Turn-Based Strategy Algorithm**  
  Controls when the player and enemy take turns, and determines which action is executed based on the current state.

- **Enemy Scaling Algorithm**  
  As the player progresses through floors, enemies increase in strength by gaining more health and attack power.

- **Shop Reroll Algorithm**  
  Randomly generates new items to refill any empty slots in the shop inventory. The shop must always display exactly 5 items.

- **Enemy Selection Algorithm**  
  Randomly selects 3 enemies from the enemy pool for each new floor, ensuring variety and unpredictability in each run.



## 4. Statistical Data (Prop Stats)

### 4.1 Data Features

- **Total Floors Cleared**  
  How far the player progressed before losing.  
  **Table Fields**: `play_id`, `start_time`,`end_time`, `kill_count`, `floor`, `character`

- **Damage Dealt Per Game**  
  Tracks attack points each floor per game session.  
  **Table Fields**: `play_id`, `floor`, `damage`

- **Total Earn**  
  Tracks all coins earned per round and per floor.  
  **Table Fields**: `play_id`, `floor`, `coin_earned`

- **Total Spend**  
  Tracks coins spent and the items purchased.  
  **Table Fields**: `play_id`, `item_bought`, `floor`, `coin_spent`

- **Total Time**  
  Tracks time spent on each floor.  
  **Table Fields**: `play_id`, `start_time`,`end_time`, `kill_count`, `floor`, `character`

---

### 4.2 Data Recording Method

- Each round's data will be saved in a **CSV file**.  
- Each feature will have its **own CSV table** for better clarity in processing and visualization.

---

### 4.3 Data Analysis Report

- **Statistical Measures:**
  - **Mean (Average)**: Average number of floors cleared.
  - **Median**: Median damage dealt per game.
  - **Mean (Average)**: Average time per floor (calculated as total time / total floors).

- **Visualization:**
  - Graphs will be used to analyze:
    - Distribution of floors cleared.
    - Damage dealt per round.
    - Average time spent per floor.


## Feature Data Summary Table

| **Feature**              | **Why it is good to have this data?**                                  | **What can it be used for?**                          | **How will you obtain 50 values of this feature data?**       | **Which variable (and class) will you collect this from?** | **How will you display this feature data?**                |
|--------------------------|------------------------------------------------------------------------|--------------------------------------------------------|----------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| **Total Floors Cleared** | Shows how far players get before failing, useful for game balancing     | Adjust difficulty curve based on average performance   | Run the game 50 rounds and record floors reached               | `total_floors` in `GameStats`                               | Summary statistics + Bar graph                             |
| **Damage Dealt Per Game**| Measures how effective players are in combat, analyze power balance     | Balance character power, tweak enemy strength          | Record `total_damage_dealt` per session over 50 rounds         | `total_damage_dealt` in `GameStats`                         | Average line graph                                          |
| **Total Earn**           | Helps balance the coin economy                                          | Determine if rewards are too little or too much        | Record `total_earned` after each round over 50 games           | `total_earned` in `GameStats`                               | Bar chart                                                   |
| **Total Spend**          | Tracks player spending, useful for pricing items                       | Identify popular price ranges, adjust shop values      | Sum `total_spent` after each game session over 50 rounds       | `total_spent` in `GameStats`                                | Bar chart or average coins spent per game                  |
| **Total Time**           | Measures time spent per game                                            | Analyze pacing, improve UI or animation delays         | Use timer (start/stop), collect for 50 sessions                | `total_time` in `GameStats`                                 | Line graph                                                  |



## Feature to Show in a Table: Total Floors Cleared

This table will summarize the player's performance in terms of how many floors they successfully cleared before the game ended. It is useful for analyzing game difficulty and player progression.

### Statistical Values Shown in Table (Example)

| **Character** | **Average Kills** | **Max Floor Reached** | **Average Floor** | **Total Games** |
|---------------|-------------------|------------------------|-------------------|-----------------|
| Wizard        | 9.8               | 3                     | 10.1              | 10              |




## Graph Overview Table

| **Graph** | **Feature Name**        | **Objective**                               | **Graph Type** | **X-axis**        | **Y-axis**            | 
|-----------|--------------------------|---------------------------------------------|----------------|-------------------|------------------------|
| Graph 1   | Total Floors Cleared     | Show average kill count per character       | Bar Graph      | Character Name     | Avg Kills              |
| Graph 2   | Total Floors Cleared     | Show % of characters reaching floor N       | Pie Chart      | Character Name     | % Reach Floor N        |
| Graph 3   | Total Earn               | Show money earned per floor per player      | Bar Graph      | Floor Number       | Coins Earned           |
| Graph 4   | Total Spend              | Show item spending distribution             | Bar Graph      | Item Name          | Coins Spent            |
| Graph 5   | Total Time               | Track time spent on each floor              | Line Graph     | Floor Number       | Time Spent             |



## UML Diagram

Below is the UML diagram for the project structure

<img src="https://raw.githubusercontent.com/Sorasit-Kateratorn/Tower-Leveling-Clash/main/uml_class_diagram.svg" alt="UML Diagram" width="600">

---

## 🔗 Resources

* 🎥 YouTube Presentation Video: [Gameplay](https://youtu.be/L6LfT4Vwb1E)

---






## Reference

### Pictures

- **Character**: [Combat RPG 2000k Characters, Animations, Backgrounds, and More](https://bkx1.itch.io/combat-rpg-2000k-characters-animations-backgrounds-and-more)
- **Potion**: [Pixel Potion Pack](https://esavvy.itch.io/pixel-posion-pack)
- **Button (Play and Quit)**: [Manuscript Game Buttons Pixel Art Set - Getty Images](https://www.gettyimages.com/detail/illustration/manuscript-game-buttons-pixel-art-set-royalty-free-illustration/1412663898)
- **Button (Game Control)**: [Markeus B UI Buttons - OpenGameArt](https://opengameart.org/content/markeus-b-ui-buttons)

### Font

- **Pixelify Sans**: [Adobe Fonts](https://fonts.adobe.com/fonts/pixelify-sans)

### Sound

- **Gameplay Music**: [Epidemic Sound - Adventure Genre](https://www.epidemicsound.com/music/genres/adventure/?_us=adwords&_usx=11304420166_&utm_source=google&utm_medium=paidsearch&utm_campaign=11304420166&utm_term=&gad_source=1&gclid=CjwKCAjwnPS-BhBxEiwAZjMF0vvtnjd5Lb1m7SWlghCRpa5waQTECPPwE4s1pFSuQWsbBCugnhFQ1hoCt84QAvD_BwE)

---
[🔗 View on GitHub](https://github.com/Sorasit-Kateratorn/Tower-Leveling-Clash)
