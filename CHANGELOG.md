# Version - 1.2.2 - [afa3ad7](https://github.com/k8thekat/GarlandToolsAPI_wrapper/commit/afa3ad7)
### Update for Release.
- Version bump and updated `__version__`.

# Version - 1.2.1-dev - [348efe4](https://github.com/k8thekat/GarlandToolsAPI_wrapper/commit/348efe4)
### Updated pyproject.toml
- Added a description.
- Fixed ruff lint exclusions and keys.

# Version - 1.2.0-dev - [8bc2796](https://github.com/k8thekat/GarlandToolsAPI_wrapper/commit/8bc2796)
### Updated Error handling
- Added more information when an error is encountered.
- Relocated the `sample` code to a seperate file.

# Version - 1.1.0-dev - [029b3b9](https://github.com/k8thekat/GarlandToolsAPI_wrapper/commit/029b3b9)
### Fixed type's for session objects to include `CachedSession`.
- Fixed logic bug in the `node` function.
- Changed `Item.patch` type from `int` to `float`.

# Version - 1.0.0-dev - [3cedb59](https://github.com/k8thekat/GarlandToolsAPI_wrapper/commit/3cedb59)
### Overall
Merge remote-tracking branch 'refs/remotes/origin/development' into development
- Logic for data structure checking was incorrect, causing a key error.
- Updated `GarlandToolsKeyError` message to be more clear.
- Updated `ItemResponse` key types.

# Version - 0.2.1-dev - [4125129](https://github.com/k8thekat/GarlandToolsAPI_wrapper/commit/4125129)
### Minor type update for Searches.
- Updated `type` key for `SearchResponse` from `Any` to `str`.
	- Added a brief doc showcasing some of its possible values.

# Version - 0.2.0-dev - [248205f](https://github.com/k8thekat/GarlandToolsAPI_wrapper/commit/248205f)
### Bug fix for language var.
- Key error with `item()` endpoint fixed.
- Failure to setup language parameter during init fixed.
- Sorted classes in `_types` file.

# Version - 0.1.3-dev - [e8a9bf5](https://github.com/k8thekat/GarlandToolsAPI_wrapper/commit/e8a9bf5)
### Minor Type changing.
- Updated typecheckingMode for pyright to `strict`.
- Fixed typing for `InstanceData` and `LeveResponse`.
- Removed un-needed logic in `GarlandToolsAsync.close()` function.
- Removed an unused import from `_enums.py`.

# Version - 0.1.2-dev - [016e13a](https://github.com/k8thekat/GarlandToolsAPI_wrapper/commit/016e13a)
### Minor changes to Changelog structure.
- Fixed older changelog structure.

# Version - 0.1.1-dev - [e260452](https://github.com/k8thekat/GarlandToolsAPI_wrapper/commit/e260452)
### Fixed typo in gitHub actions.
- Removed extra "release_level" literals from lib.
- Added development files.

# Version - 0.0.2 - [ac6e652](https://github.com/k8thekat/GarlandToolsAPI_wrapper/commit/ac6e652)
### Organization and cleanup.
- Updated dependencies based upon feedback.
	- Updated `uv`.
- Added an `ISSUES` template.
- Added VScode `extensions.json`.
- Removed `Patch` Enum as it wasn't used.
- Updated docstrings and commenting for types.
	- Sorted types in alphabetical order.
- Misc documentation updates.

# Version - 0.0.1 - [7503bd5](https://github.com/k8thekat/GarlandToolsAPI_wrapper/commit/7503bd5)
### First commit.

# Version - 0.0.0 - [000000] 
### Init...
- Init of the changelog/Repo.