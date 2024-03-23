# SoccerAnalytics
Repo for Group B9

## To-Do's:
- Skripte verstehen und zum laufen bringen (Github, Jupyter-Notebook, Python)
- Daten verstehen
- Erste Ideen, welche Dataen zu analysieren

# Preparation Denmark to play against Slovenia !

## Introduction

Despite Denmark holding the 21st position in the FIFA rankings, and Slovenia being ranked at 55, overlooking a theoretically weaker opponent is never advisable. During the last game against Slovenia (Qualifiers Euro 23) we won with 2-1 in a complicated game while we got a draw 6 month earlier with 1-1 (Qualifiers Euro 23). In this analysis, we'll provide you with all the essential keys to ensure success against Slovenia in the upcoming match. 

Based on information from multiple sources, it's seems evident that Slovenia's team possesses notable strengths at some positions. Specifically, their goalkeeper, currently playing for Atlético, stands out, alongside midfielders Benjamin Sesko and Jaka Bijol. Given their midfield/attack roles, it's reasonable to anticipate Slovenia boasting a strong midfield/attack presence.

![alt text](composition.png)

After analyzing their recent match against Malta, it's evident that Slovenia employed a traditional 4-4-2 formation with no unexpected variations in player selection. Additionally, one of the standout players we identified, Sesko, managed to score a goal during the game. We should keep in mind that the 4-4-2 formation brings a central presence that enables counter-attacks. 

### Qualifier Games Slovenia

| wyscout | skillcorner | date | home | away | Score Home | Score Away | Notes |
|--------:|------------:|------|------|------|------------|------------|-------|
| 5414103 |  | 2023-03-23 | Kazakhstan | Slovenia  | 1 | 2 |  |
| 5414128 |  | 2023-03-26 | Slovenia | San Marino | 2 | 0 |  |
| 5414156 |  | 2023-06-16| Finland | Slovenia | 2 | 0 |  |
| 5414180 | | 2023-06-19 | Slovenia | Denmark | 1 | 1 |  |
| 5414203 |  | 2023-09-07 | Slovenia | Northern Ireland | 4 | 2 |  |
| 5414226 | 1385659 | 2023-09-10 | San Marino | Slovenia | 0 | 4 |  |
| 5414260| 1381446 | 2023-10-14 | Slovenia | Finland | 1 | 3 |  |
| 5414284 | 1381466 | 2023-10-17 | Northern Ireland | Slovenia | 0 | 1 |  |
| 5414302 | 1381485 | 2023-11-17 | Denmark | Slovenia | 2 | 1 |  |
| 5414324 | 1381505 | 2023-11-20 | Slovenia | Kazakhstan | 2 | 1 |  |

#### Injured & suspended players

TODO: Have a look at who is injured

## Statistics of Slovenia's recent games 

### Formation and line up 

We start first by analysing the common composition of Slovenia. In the last 9 games against Malta, USA, Kazakhstan, Denamrk, North Ireland and Finland, Slovenia used 8 times a 4-4-2 composition and the only modified composition was when Benjamin Sesko wasn't available. Therefore we can excpect the composition to be probably the same. Here is a quick recap of pro ans cons of the 4-4-2 composition.

Here is a quick refresh of the pros and cons of 4-4-2:

**Pros :** With a strong defense, wide attack, and quick movement into the opponent's territory, the 4-4-2 excels in counter-attacks. Defensively, it allows for a compact setup with two lines of four players, while the forwards remain poised for quick offensive opportunities. The presence of two strikers presents a unique challenge for defenders, as it reduces time and space on the ball and increases the threat of one-on-one situations. Additionally, passing out from the back becomes more challenging with constant pressure from two attackers.

**Cons :** In a 4-4-2 formation, teams may struggle to control the midfield, especially against opponents using a midfield trio, leading to less possession. Additionally, the 4-4-2 lacks defensive depth, as players within the same line may leave gaps. Despite being compact, this formation is vulnerable to line-breaking passes, making it easier for opponents to bypass multiple players at once. Defensive setups like the 4-1-4-1 offer better coverage between the lines.When attacking, the midfield and defensive lines align closely, restricting forward passing options. This setup can limit the team's ability to create passing opportunities compared to formations with players spread across different lines.

### Key statistics

TODO: Add statistics on the picture - aggregate from previous matches 

![alt text](statistics.png)

TODO: Write small analysis with the values

##### Ball possession

```python
# add script here
def compute_value():
  reuturn 1
```

##### Attemps at Goal (on target)

```python
# add script here
def compute_value():
  reuturn 1
```

##### Total passes

```python
# add script here
def compute_value():
  reuturn 1
```

##### Pass completion

```python
# add script here
def compute_value():
  reuturn 1
```

##### Completed line breks

```python
# add script here
def compute_value():
  reuturn 1
```

##### Reception in the final third

```python
# add script here
def compute_value():
  reuturn 1
```

##### Crosses

```python
# add script here
def compute_value():
  reuturn 1
```

##### Ball progressions

```python
# add script here
def compute_value():
  reuturn 1
```

##### Defensive pressures - direct pressures

```python
# add script here
def compute_value():
  reuturn 1
```

##### Forced turnover

```python
# add script here
def compute_value():
  reuturn 1
```

##### Total distance covered

```python
# add script here
def compute_value():
  reuturn 1
```

##### High speed distance covered

```python
# add script here
def compute_value():
  reuturn 1
```

### Player heatmaps 

```python
# Add script to generate player heatmap
```



## In possesion - attack of Slovenia

#### Attacking formation & style:

TODO: Add same distribution like in the picture

![alt text](in.png)

```python
# Add script to type of play in possession
```

#### Passing network

```python
# Add script for generating the passing network 
```

#### Line breaks

#### Attemps at goal

#### Crosses

#### Key players involved in chances and goals

- analyze run frequency, location, utilization
- analyse type of runs

#### Shots & shots on target

## Out of possesion - defense of Slovenia

#### Typical defensive formation & style

TODO: Add same distribution like in the picture

![alt text](in.png)

```python
# Add script to type of play out of possesion
```


#### Pressing

#### Duel performance of the players

#### Help from other players




## Set plays

##### Corners

TODO: Who shots, any danger? (inswing vs outswing)

##### Penalties

TODO: Who shots, which direction statistically?

##### Free kicks

TODO: Who shots, who does what. Any Danger? How do they shot normally?




## Statistics of the players - sorted by value (in dollars) according to find website : 

- possesion
- distribution
- offers & receptions
- physical data sprints / avg runs / top speed and so on
- Endurance check


```python
# Skillcorner
print(physical_df[['player_name','Distance', 'Count High Acceleration','Sprinting Distance','PSV-99']])
```

- Dangerous runs & types of runs

```python
# Example to see all supports runs
print(dynamic_events['event_subtype'].unique())
print(dynamic_events[dynamic_events['event_subtype'] == 'support'][['player_name', 'time_start']])
```


## Weaknesses & Tactic to adopt

## Conclusion



# Appendix

## Good resources
- [Soccermatics](https://soccermatics.readthedocs.io/en/latest/gallery/lesson1/plot_PlottingPasses.html) 
- [Soccer Analytics Handbook ](https://github.com/devinpleuler/analytics-handbook)https://github.com/devinpleuler/analytics-handbook
- [Edd Webster Football Analytics](https://github.com/eddwebster/football_analytics?tab=readme-ov-file#-python): Overview of many resources
- [Example slides](https://www.fifatrainingcentre.com/media/native/world-cup-2022/report_133009.pdf)



#### Appendix

## Best practices GIT:

See [freecodecamp](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/) for more detailed instructions.

The commit type can include the following:

```feat``` – a new feature is introduced with the changes  
```fix``` – a bug fix has occurred  
```chore``` – changes that do not relate to a fix or feature and don't modify src or test files (for example updating dependencies)  
```refactor``` – refactored code that neither fixes a bug nor adds a feature  
```docs``` – updates to documentation such as a the README or other markdown files  
```style``` – changes that do not affect the meaning of the code, likely related to code formatting such as white-space, missing semi-colons, and so on.  
```test``` – including new or correcting previous tests  
```perf``` – performance improvements  
```ci``` – continuous integration related  
```build``` – changes that affect the build system or external   dependencies
```revert``` – reverts a previous commit  
