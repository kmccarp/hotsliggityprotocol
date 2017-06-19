# hotsliggityprotocol
Python library to parse .StormReplay files and upload to service model to HotSliggityService

Big thanks to [Blizzard's heroprotocol project](https://github.com/Blizzard/heroprotocol) for the inspiration.

## Getting Started

* Requires Python 2.7 to run
* If Windows, need to have `Python27` and `Python27/Scripts` on your PATH
* Currently, need to copy a .StormReplay file to the heroprotocol project directory
* May need to run `$pip install -r requirements.txt` to get dependencies requests and urllib3

## Example Usage

```python
python hotsliggityprotocol.py "Blackheart's Bay.StormReplay"
```


## Decoders Explained
`--details` = print player name and hero pick, map name, map time, which team each player is on, match results

`--trackerevents` = print pretty much everything that happens in the game (ScoreResultEvent, EndOfGameTalentChoices, lots more...)

`--initdata` = print player hero and hero loadouts, heroMasteryTiers, and if they are silenced

`--gameevents` = print all game events including coordinates

`--header` = print HotS build

`--messageevents` print message events such as ping events

`--attributeevents` = print attribute events, a table of attrid, namespace, and attribute values
