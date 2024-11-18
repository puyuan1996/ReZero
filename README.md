
# ReZero Algorithm Implementation

This guide outlines the implementation of the ReZero algorithm based on the open-source [LightZero](https://github.com/opendilab/LightZero) repository.

## 1. Install LightZero

First, install the LightZero framework using the following command:

```bash
pip install git+https://github.com/opendilab/LightZero.git
```

## 2. Compile ReZero's Cython Extension

Before training the ReZero algorithm, you need to compile the Cython extension. Follow the steps below:

### 2.1 Navigate to the `ctree_rezero` Directory

Navigate to the `ctree_rezero` directory, which is located at `lzero/mcts/ctree/ctree_rezero`:

```bash
cd ./lzero/mcts/ctree/ctree_rezero
```

### 2.2 Build the Cython Extension

In this directory, run the following command to build the Cython extension and generate the `.so` file:

```bash
bash make.sh
```

This command will:

- Convert the `mz_tree.pyx` file into C++ code.
- Compile the C++ code to generate a shared object file (`.so`).
- Place the resulting `.so` file in the same directory as `setup.py`.

## 3. Train the ReZero Agent in Atari Environments

After successfully building the Cython extension, you can quickly train a ReZero agent in Atari environments like [Pong](https://gymnasium.farama.org/environments/atari/pong/). Start training with the following command:

```bash
python3 zoo/atari/config/atari_rezero_mz_config.py
```

## 4. Train the ReZero Agent in Board Game Environments

You can also train a ReZero agent in board game environments. Start training with the following command:

```bash
python3 zoo/board_games/gomoku/config/gomoku_rezero_mz_bot_mode_config.py
```


