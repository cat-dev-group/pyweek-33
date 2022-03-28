# pyweek-33
The official repo for Cat Dev PyWeek 33 shenanigans!

## Setup (simplified)
1. Clone the repo: `git clone https://github.com/cat-dev-group/pyweek-33.git`
2. Install dependencies from `poetry` via: `poetry install`
3. Set up pre-commit hooks: `pre-commit install`
4. Add commit message template: `git config --local commit.template .gitmessage`

## Contributing
For contributing instructions and guidelines, as well as more detailed setup steps, see `CONTRIBUTING.md`.

## Running the game
1. Clone the repository
2. `cd` to `pyweek-33`
3. `poetry install`
4. `poetry shell`
5. `py -m src`
6. Currently, in order to run the next level, you must uncomment the next and comment out the previous level in `game.py`. E.g. to go from tutorial to level one:
    ```py
    # exec(levels["tutorial"])  # comment out tutorial level
    exec(levels["level1"])  # uncomment level 1
    # exec(levels["level2"])
    # exec(levels["level3"])
    # exec(levels["level4"])
    ```
    The module will then need to be run again with `py -m src`
