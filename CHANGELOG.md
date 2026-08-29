# Version - 1.5.2 - [a4a2168](https://github.com/k8thekat/GarlandToolsAPI_wrapper/commit/a4a2168)
### Overall
Dev tooling, local.py refactor and linting config updates

### .github/scripts/gen_changelog.py
- Searches for first `# Version -` line instead of assuming line 0
	- Handles missing version header gracefully (treats as initial commit)

### .gitignore
- Added `*local_data/` pattern

### .vscode/launch.json
- Added variables reference URL comment

### .vscode/tasks.json (NEW)
- VSCode tasks for docstring attribute generation via numpy_template

### NOTES.md
- Rewrote with version bump instructions and updated commit message structure

### TODO.md
- Added icon try/except TODO and marked template update complete

### async_garlandtools/__init__.py
- Version bump 1.5.1 -> 1.5.2

### async_garlandtools/modules.py
- Added TODO comment for icon endpoint higher-res fallback

### async_garlandtools/_extension.py (NEW)
- Scaffolding for extension classes (Snowflake, Object, Item)

### local.py
- Refactored into a `Local` class with typed methods
- Added `SQLHandler` class wrapping asqlite pool operations
- Added `DumpParameters` and `WriteDataParameters` TypedDicts
- Updated `LogHandler` with sentry placeholder and webhook stub
- Fixed `subprocess.run` to use list args instead of string
- Fixed argparse namespace handling

### numpy_template/docstring_attrs.py (NEW)
- Script to scan Python classes and insert NumPy-style Attributes sections
- Supports preview diff, in-place write, class/line targeting

### pyproject.toml
- Added ruff ignore rules (RUF003, SLF001, TD002, TRY400, T201, ASYNC240, C901, FBT001, FBT002)
- Expanded pyright exclude paths
- Added `asqlite` dev dependency group

### uv.lock
- Updated lockfile for asqlite and corrected package name
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01AfyaxmmRUiEj4vHs2Gn7fa

# Version - 1.5.1 - [84395c2](https://github.com/k8thekat/GarlandToolsAPI_wrapper/commit/84395c2)
### Minor type change to returned Request errors.
- Changed from `GarlandToolsTypeError` to `GarlandToolsRequestError` to better facilitate the reason behind the error also containing more useful information for debugging.
	- Updated all docs related to the change.

# Version - 1.5.0 - [e509d0e](https://github.com/k8thekat/GarlandToolsAPI_wrapper/commit/e509d0e)
### Overall
Merge remote-tracking branch 'refs/remotes/origin/development' into development
- Added `Raises` field to function docstrings for any Errors to help usage.
- Added a `try, except` for when attempting to call `.json()` on our data response.

# Version - 1.4.2 - [adf97a4](https://github.com/k8thekat/GarlandToolsAPI_wrapper/commit/adf97a4)
### Minor update for Icon Type
- Added a `item_custom` field to handle a special item ID case called `fccredit`.

# Version - 1.4.1 - [9ff411c](https://github.com/k8thekat/GarlandToolsAPI_wrapper/commit/9ff411c)
### Overall
Merge branch 'development' of https://github.com/k8thekat/GarlandToolsAPI_wrapper into development
- There is an item that is not obtained via an id, instead it uses the a string name. eg. `fccredit`.

# Version - 1.4.0 - [ca1f464](https://github.com/k8thekat/GarlandToolsAPI_wrapper/commit/ca1f464)
### Additional args, kwargs to update `icon` endpoint.
- Added a positional parameter to `icon` called `thumbnail` to force return lower resolution Icon data by default. As higher resolution Icon data can fail to resolve.
- Added additional parameters to `icon` related to `aiohttp.ClientResponse` and a `content_only` flag to force return raw bytes over JSON.

# Version - 1.3.0 - [f7f7021](https://github.com/k8thekat/GarlandToolsAPI_wrapper/commit/f7f7021)
### Updated data returns
- Added missing key values for `NPC`
- Added missing "partials" key to `NPCResponse`.
- Added two new data types, `Shop` and `Equipment`.
- Doubled `CachedSession` expire_after parameter value. (86400 -> 172800).

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