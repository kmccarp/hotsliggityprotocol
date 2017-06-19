# hotsliggityprotocol
Python library to parse .StormReplay files and upload to service model to HotSliggityService

Big thanks to [Blizzard's heroprotocol project](https://github.com/Blizzard/heroprotocol) for the inspiration.


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


## #TODO: Complete Current Model
* **matchType** - _init data, derived_
* **mapName** - _details_
* **matchLength** - _not sure_
* **heroName** - _details_
* **heroLevel** - _not sure_
* **matchmakingRating** - _calculated_
* **ratingAdjustmentPoints** - _calculated_
* **matchDateTime** - _details_


## #TODO: Changes for Future Model
* **matchOutcome** - _details or init data_
* **talent choices** - _tracker events_
* **score result screen stats** - _tracker events_
* **teammates and enemy team player names and hero picks** - _details_
* **season** - _derived_
