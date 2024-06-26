from pathlib import Path

# this directory is the root directory of all sepal dashboard app.
# please make sure that any result that you produce is embeded inside this folder
# create a folder adapted to your need inside this folder to save anything in sepal
module_dir = Path.home() / "module_results"
module_dir.mkdir(exist_ok=True, parents=True)

weplan_dir = module_dir / "weplan"
weplan_dir.mkdir(exist_ok=True, parents=True)

tmp_dir = Path.home() / "tmp" / "weplan"
tmp_dir.mkdir(exist_ok=True, parents=True)
