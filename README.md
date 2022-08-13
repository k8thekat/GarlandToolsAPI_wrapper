# GarlandTools PIP

Unofficial Python wrapper for [GarlandTools] API.  

> ⚠️ This is a public API.  
> ⚠️ Please do not spam or abuse it in any shape or form.

Special thanks to [GarlandTools] for providing this API and keeping it updated.

## Installation

```bash
pip install garlandtools
```

## Usage

All [GarlandTools] Endpoints are implemented in this API.
Simply call them by their function name.
Everything will be done for you: building the request, submitting the request, retrieving the answer and returning it to your call.

Most endpoints return a JSON which can be used as a `dict` in Python.  
In some cases a JSON of the `list` form or even a PNG is returned.  
A full overview is below:

| Endpoint Name | Has id endpoint | Has 'all' endpoint | Returns       |
| ------------- | --------------- | ------------------ | ------------- |
| Achievement   | ✅               | ✅                  | JSON (`dict`) |
| Data          | ❌               | ✅                  | JSON (`dict`) |
| Endgame Gear  | ❌ (`Job`)       | ❌                  | JSON (`dict`) |
| Fate          | ✅               | ✅                  | JSON (`dict`) |
| Fishing       | ❌               | ✅                  | JSON (`dict`) |
| Icon          | ✅ (`str`)       | ❌                  | PNG           |
| Instance      | ✅               | ✅                  | JSON (`dict`) |
| Item          | ✅               | ❌                  | JSON (`dict`) |
| Leve          | ✅               | ✅                  | JSON (`dict`) |
| Leveling Gear | ❌ (`Job`)       | ❌                  | JSON (`dict`) |
| Map           | ✅ (`str`)       | ❌                  | PNG           |
| Mob           | ✅               | ✅                  | JSON (`dict`) |
| Node          | ✅               | ✅                  | JSON (`dict`) |
| NPC           | ✅               | ✅                  | JSON (`dict`) |
| Quest         | ✅               | ✅                  | JSON (`dict`) |
| Search        | ✅ (`str`)       | ❌                  | JSON (`list`) |
| Status        | ✅               | ✅                  | JSON (`dict`) |

Each endpoint has it's own function.  
E.g. "Achievement" will have a `achievement(id: int)` function.

Additionally, if an endpoint is able to return **all** entries of that type an id-less function will be present.  
E.g. "Achievement" will not only have a `achievement(id: int)`, but also an `achievements()` function.

Most functions use an id (integer) to query.
However, said ids rarely start a 0 or 1.  
In some cases, like icons, map or search, a string is instead used.  
Furthermore, the endgame gear and leveling gear endpoints are using the `Job` enum instead.

There is an additional `search(query: str)` function to submit a search query.
**However, please use this endpoint only if absolutely necessary and you don't know a certain ID.**

All functions utilize a caching request package ([Requests-Cache]) which will create a local database of requests and refresh every > 60m.  
[GarlandTools] only update rarely and after patches.

### Credits

I want to credit [GarlandTools] and [GarlandTools NodeJS project](https://github.com/karashiiro/garlandtools-api) without which this wouldn't be possible.

[GarlandTools]: garlandtools.org/
[Requests-Cache]: https://pypi.org/project/requests-cache/
