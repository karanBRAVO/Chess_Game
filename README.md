# Chess_Game v2

- Create a chess game from `0 -> END` `#multiplayer`
- Using: `Pygame`, `Python`, `Node.js`, `Socket.io`

**_`note`_**: make sure you have installed the `colorama` library before running the script.

- to install the `colorama` library

  ```bash
  pip install colorama
  ```

- all the assets are provided in the `chessAssets` directory

## Usage

- clone the repository

  ```bash
  git clone https://github.com/karanBRAVO/Chess_Game.git
  ```

- move to the cloned directory

  ```bash
  cd Chess_Game
  ```

- move to the chess server directory

  ```bash
  cd chessServer
  ```

- install the dependencies and run the build command

  ```bash
  npm install && npm run build
  ```

- start the server

  ```bash
  npm run start
  ```

- run the script `(you have to run multiple terminals and run below command)`

  ```bash
  python chessEngine/main.py
  ```

## Preview of the Game

![image](https://github.com/karanBRAVO/Chess_Game/assets/77043443/f283403d-c224-4d7b-b38a-61fd14428a2f)

## File Structure

    chessAssets/
    |
    chessEngine/
    |-- assets/
    |   |-- army/
    |   |-- chessboard.py
    |   |-- logger.py
    |   |-- pieces.py
    |-- main.py
    |
    chessServer/

## Virtual Environment Setup (recommended)

1. Install the `python3-venv`

   ```bash
   sudo apt install python3-venv
   ```

2. Create the virtual env.

   ```bash
   python3 -m venv myenv
   ```

3. Activate the env.

   ```bash
   source myenv/bin/activate
   ```

**note**: to deactivate type _`deactivate`_ in terminal

## Create the desktop application

1. install the module

```bash
pip install pyinstaller
```

2. run the command

```bash
pyinstaller --onefile --icon=chessEngine/icon.ico --add-data "chessAssets;chessAssets" --hidden-import socketio --hidden-import colorama chessEngine/main.py
```

3. run the final output

```
./dist/main
```

### ©️ Karan Yadav 2023
