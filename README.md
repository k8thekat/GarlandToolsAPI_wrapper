# GarlandTools PIP

Unofficial Python wrapper for [GarlandTools] API.  

> ⚠️ This is a public API.  
> ⚠️ Please do not spam or abuse it in any shape or form.

Special thanks to [GarlandTools] for providing this API and keeping it updated.

## Table of Contents

- [GarlandTools PIP](#garlandtools-pip)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Credits](#credits)
  - [Versions](#versions)

## Installation

```bash
pip install garlandtools
```

## Usage

All [GarlandTools] Endpoints are implemented in this API.  
Below is a table showing all endpoints and whether they have an _id_ and/or _all_ endpoint.  
An _id_ endpoint means there is a unique identifier that can be used to query information.
Commonly an integer. However, there is also a `Job` enum and string endpoints.  
An _all_ endpoint simply returns all data of that endpoint in a massive JSON file, no id needed but requires more filtering.

All endpoints return JSON which is parsed into **unstructured** `dict`.
This is true for all, but two endpoints: Map and Icon, which return a **binary PNG** instead.
Additionally, the Search endpoint returns a `list`.  
A full overview is below:

| Endpoint Name | Has id endpoint | Has 'all' endpoint | Returns       |
| ------------- | --------------- | ------------------ | ------------- |
| Achievement   | ✅               | ✅                  | JSON (`dict`) |
| Data          | ❌               | ✅                  | JSON (`dict`) |
| Endgame Gear  | ❌ (`Job`)       | ❌                  | JSON (`dict`) |
| Fate          | ✅               | ✅                  | JSON (`dict`) |
| Fishing       | ❌               | ✅                  | JSON (`dict`) |
| Icon          | ✅ (`str`)       | ❌                  | Binary PNG           |
| Instance      | ✅               | ✅                  | JSON (`dict`) |
| Item          | ✅               | ❌                  | JSON (`dict`) |
| Leve          | ✅               | ✅                  | JSON (`dict`) |
| Leveling Gear | ❌ (`Job`)       | ❌                  | JSON (`dict`) |
| Map           | ✅ (`str`)       | ❌                  | Binary PNG           |
| Mob           | ✅               | ✅                  | JSON (`dict`) |
| Node          | ✅               | ✅                  | JSON (`dict`) |
| NPC           | ✅               | ✅                  | JSON (`dict`) |
| Quest         | ✅               | ✅                  | JSON (`dict`) |
| Search        | ✅ (`str`)       | ❌                  | JSON (`list`) |
| Status        | ✅               | ✅                  | JSON (`dict`) |

To use the API, first initialize the `GarlandTools` class:

```python
api = GarlandTools()

# Optionally you can change the parameters:
api = GarlandTools(cache_location=cache_location, cache_expire_after=cache_expire_after, language=language)
# `cache_location` defines where the cache will be stored
# `cache_expire_after` defines when the cache is expired (please don't disable `0` this or set it to some short amount of time. Item data is usually only updated on patches!)
# `language` defines the language GarlandTools is returning the names and descriptions in
```

Each endpoint has it's own function implemented in the `GarlandTools` class.  
Simply call them and supply parameters if needed (_id_ endpoints, not on _all_ endpoints).  
For example: Say we want to query a specific item and we know the item id is `2`.  
All we need to do is:

```python
# 1. Initialize API
api = GarlandTools()

# 2. Query item
item_id = 2
response = api.item(item_id)

# 3. Check if successful and retrieve JSON
if response.ok:
    item_json = response.json()
else:
    print(f'Failed querying item id '{item_id}' ({response.url}): [{response.status_code}] {response.reason}')
```

Alternatively, you can also try using `Response::json()` and catch exceptions:

```python
# 1. Initialize API
api = GarlandTools()

# 2. Query item
item_id = 2
response = api.item(item_id)

# 3. Check if successful and retrieve JSON
try:
    item_json = response.json()
except:
    print(f'Failed querying item id '{item_id}' ({response.url}): [{response.status_code}] {response.reason}')
```

The resulting JSON is in most cases a `dict` in Python.  
We can simply query it as an array: `item_json['query goes here']`.  
It may also be helpful to use `print(item_json)` to see all the values.  

> Tip: You can use `print(response.url)` to print out the query URL and open this in your browser.
> Most browsers have a much better than JSON viewer than most IDEs/Editors.

However, please keep in mind that select endpoints do not return JSON (or not `dict`, but `list`).
In these cases the `Response::json()` will fail. Use `Response::text` or `Response::content` instead.

There is an additional `search(query: str)` function to submit a search query.
**However, please use this endpoint only if absolutely necessary and you don't know a certain ID.**

All functions utilize a request caching package ([Requests-Cache]) which will create a local database of requests and only refresh after the cache is expired (default setting: 24h).  
[GarlandTools] only updates after patches usually.

## Credits

I want to credit [GarlandTools] and [GarlandTools NodeJS project](https://github.com/karashiiro/garlandtools-api) without which this wouldn't be possible.

[GarlandTools]: garlandtools.org/
[Requests-Cache]: https://pypi.org/project/requests-cache/

## Versions

| Version | Supported | Description                                           |
| ------- | --------- | ----------------------------------------------------- |
| v2.0.0  | ✅         | Major rewrite, simpler to use and more organized now. |
| v1.0.1  | ✅         | Minor bug fixes for v1.0.0.                           |
| v1.0.0  | ❌         | Official first version.                               |
| v0.1.0  | ❌         | Initial package. **DO NOT USE.**                      |
