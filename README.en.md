# Ballistic Duel | [Баллистическая Дуэль](https://github.com/ArtemisYur/BallisticPixelDuel/blob/main/README.md)
This is Ballistic Duel, pixel-styled game featuring mechanic of duel between two ballistas.
Set speed, mass and angle of shoot to destroy your opponent!

![Screenshot 2025-05-30 071333](https://github.com/user-attachments/assets/89f6f36a-fba9-4035-897a-475493a550cf)
![Screenshot 2025-05-30 071417](https://github.com/user-attachments/assets/f57b1d91-4535-4b66-b6b0-ac5f6772a45c)
![Screenshot 2025-05-30 071459](https://github.com/user-attachments/assets/41367258-7b77-4080-9760-19251bacfd8f)

# Possible improvements

## 🎮 GAME MODES

### 1. PvP (two players on one device)
- Two profiles: drop-down list + the ability to create a new one.
- All settings: names, background, language, music, weather, planet, chaos level.
- Tracking matches between players (log in their profiles).
🔧 Comment: Fully implementable. It is worth providing confirmation before creating a new profile to avoid garbage.

### 2. Campaign
- One player → one profile.
- List of levels (visualized list of buttons).
- Each level sets fixed conditions: planet, weather, difficulty.
- Player progress is recorded in the profile.
🔧 Supplement:
- Add a star rating system (1–3), passing with minimal errors.
- You can introduce scenarios/missions (for example: "shoot three times to win").

### 3. Single battle (with AI)
- One player.
- Manual selection of all settings.
- Based on the selected parameters (gravity, chaos, weather, etc.), the difficulty is assessed: Normal / Hard / Nightmare
🔧 Idea: Introduce the calculation of "difficulty points" and display before the start of the game. For example: Difficulty: 4.3/5 (Nightmare)
📌 Criticism: It is necessary to clearly define how the AI ​​will shoot (simplified bot? simulation?). You can start with random + minimum zoom.

## ⚙️ SETTINGS (universal for all modes)

| Setting | Type | Influence |
| ------------- | -------------------------- | ------------------------------- |
| Player Name | Text / Profile | Save Progress |
| Planet | List | Changes Gravity |
| Weather | List | Visual and Physical Effects |
| Time of Day | Toggle | Background and Atmosphere |
| Language | Toggle (RU/EN) | Interface Texts |
| Music | List of Themes or Toggle | Background Accompaniment |
| Chaos Level | List (None / Angle / All) | Pseudo-Randomness |

## 🧠 PROFILES AND SAVES

Format:
.player encrypted or archived .txt or .json
Profile name = file name (e.g. Alex.player)
Inside:

{
"name": "Alex",
"campaign": {"1": "completed", "2": "locked"},
"battles": [{"mode": "PvP", "opponent": "Mira", "result": "win"}],
"settings": {...}
}

🔧 Recommendations:
- Store files in a separate folder /profiles/.
- Automatically scan and display profiles on startup.
- Add a garbage filter (e.g. when creating, require name confirmation + at least 3 characters).

## 🛠️ WEAPONS AND SHELLS

| Weapon type | Parameters | Control mechanics |
| ---------- | -------------------------- | --------------------------- |
| Catapult | mass, angle | as is now |
| Cannon | charge, angle | force = press duration |
| Railgun | voltage, induction, angle | several scales or 2D panel |

🔧 Idea development:
- Each weapon is unlocked as you progress.
- You can give the player a random/limited weapon in the campaign.
📌 Implementation: You will need an abstract Weapon class, inheritors with get_trajectory().

## 🪜 IMPLEMENTATION PLAN (by stages)

| Stage | Function | Complexity | Dependencies |
| ---- | ---------------------------------------- | --------- | ------------------------- |
| 1 | Add profile support | ⭐⭐⭐ | UI + file system |
| 2 | Mode screen: PvP / Campaign / Solo | ⭐⭐ | UI transitions |
| 3 | Campaign with levels | ⭐⭐⭐ | Reading levels, saving |
| 4 | Single-player AI battle | ⭐⭐⭐⭐ | Basic bot |
| 5 | Weather effects and influence | ⭐⭐⭐⭐ | Physics and visualization |
| 6 | Chaos level (random) | ⭐⭐ | Randomness generator |
| 7 | Language switcher | ⭐⭐ | Translation tables |
| 8 | Weapons/shells | ⭐⭐⭐⭐ | Classes, interface |

## 🔍 Problems and Prospects
### Strengths:
- Good modular structure of ideas
- Linking functionality to gameplay meaning
- Scaling support

### Potential difficulties:
- The number of saves in a folder can grow quickly → either a centralized DB (for example, profiles.json) or automatic cleaning / grouping is needed
- Balancing weapon parameters and randomness is an important issue

## 💡 Additional
- Add rewards to campaigns (skins, animations, new levels).
- Support for cheat codes (as a developer option - for testing).
- Multilingual translation with the ability to automatically connect new languages ​​(via .lang files).
