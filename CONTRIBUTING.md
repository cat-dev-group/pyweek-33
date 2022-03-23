# Contributing
To contribute to our Pyweek project, make sure you follow these instructions and guidelines.

[Git](https://git-scm.com/), [Poetry](https://python-poetry.org/), and [Pyglet](http://pyglet.org/) are needed for development. Commands are to be executed in a command-line interface.

Do not hesitate to ask us in the Discord server if you have any questions!

### Instructions
To set up your working environment:

1. Clone the GitHub repository at your desired directory: `git clone https://github.com/cat-dev-group/pyweek-33.git`
2. Enter the repo directory: `cd pyweek-33`
3. Install project dependencies from Poetry: `poetry install`
4. Set up pre-commit hooks: `pre-commit install`
5. Add the commit message template to Git: `git config --local commit.template .gitmessage`

To change code safely using Git:

1. In your repo directory, create and switch to a new branch: `git checkout -b "cool-branch-for-your-feature"`
2. Implement your feature/patch a bug/do work
3. When finished, stage the changes: `git add <files-to-stage>` (`git add .` to stage all modified files)
4. Commit changes: `git commit` (if commit message template does not work, use `git commit -m "commit-message"`)
5. Push the branch to GitHub repository: `git push origin cool-branch-for-your-feature`

You can then go on GitHub, create a pull request (PR), and your branch will be merged with main when the PR is approved.

### Guidelines
- Commit messages should be concise and meaningful, and follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
- Follow [PEP 8](https://pep8.org/) to write readable Python code.
