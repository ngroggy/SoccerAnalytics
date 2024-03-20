# SoccerAnalytics
Repo for Group B9

<!---------------- HEADER SECTION -------------------->
<details><summary>Project Group</summary>

_Please fill in the following table._

| handle      | name               |
| ----------- | ------------------ |
| @dgregory   | Grégory de Meurichy|
| @ngrogg     | Nic Grogg          |
| @grloris    | Loris Griesbaum    |
| @ygoergen        | Yves Görgen             |
| @fcosta          | François Costa               |
</details>

<details>
<summary>TA Comments</summary>

Your teaching assistant is Ivana (@ismokovic) and can be reached at ismokovic@ethz.ch 

- [ ] when saving, please indicate what you changed in a meaningful commit messages
- [ ] draft due: **Monday, April 8**
- [ ] final version due: **Friday, May 24** 
</details>


# Match \#06 (SVN-DEN): preparing Denmark to play against Slovenia


<!------------ START YOUR REPORT BELOW THIS LINE --------------->

Example slide: https://www.fifatrainingcentre.com/media/native/world-cup-2022/report_133009.pdf

# Introduction to Slovenia

Introduce the context of the match, previous matches on Slovenia. Context of the game.....

# Formation & lineups

Basic components, what is the line up. Is it consistent. Suspension, injuries....

Do they play the same against all the differents teams?

- slide 3 example
- ball speed as a proxy for match speed
- possention
- Player heatmap
- Ball possession Analysis

# Possession

How to they like to play? Do they like long passes, long board, pass behind? How do they create goals? Do they play left side because one player is good? Are they direct when they attack?

- slide 4 example
- in possesion line height
- line break
- passing network (use their script)
- attempt at goal
- crosses 
- create heatmaps and trajectories
- filter for types of runs, compare to SkillCorner
- passes
- pass completion
- Player heatmap
- trajectory smoothing, simplification, classification
- analyze run frequency, location, utilization
- create pitch control maps
- space control and creation through movement
- third end analysis 
- ball heatmap

# Out of possesion

Same but when the team is not on possession? Do they press? Are they aggressive when they don't have the ball? 

- slide 4 example
- total pressures
- direct pressures
- avg pressure duration
- forced turnovers
- ball recovery time
- puhsing on into pressing
- aerial game
- how does the goalkeeper plays
- Player heatmap
- check and analyze offsides and near-offsides
- third end analysis 
- ball heatmap
# Set plays

Corners (inswing vs outswing), penalty, long throws,.... What kind of set plays are dangerous?

Example: If the teams scores a lot with corners ==> Notify it

- corners
- penalties
- free kicks (direct vs indirect - create visualisation map)
- who shots
- trajectory smoothing, simplification, classification
- Type of goal

# Individual players

Characteristics of each individual player.

- possesion
- distribution
- offers & receptions
- physical data sprints / avg runs / top speed and so on
- estimate velocity, acceleration, curvature- estimate velocity, acceleration, curvature
- Endurance check 
- Player possession Analysis

# Strengths of Slovenia

What are they doing well?


# Weaknesses of Slovenia

What are they doing less well?

# Match tactics we can use

Suggestions of tactics that can work very well.

# Conclusion

Conclusion

# Things to brainstorm












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

### Qualifier Games Denmark

| wyscout | skillcorner | date | home | away | Score Home | Score Away | Notes |
|--------:|------------:|------|------|------|------------|------------|-------|
| 5414106 |  | 2023-03-23 | Denmark | Finland | 3 | 1 |  |
| 5414126 |  | 2023-03-26 | Kazakhstan | Denmark | 3 | 2 |  |
| 5414155 |  | 2023-06-16 | Denmark | Northern Ireland | 1 | 0 |  |
| 5414180 | | 2023-06-19 | Slovenia | Denmark | 1 | 1 |  |
| 5414202 |  | 2023-09-07 | Denmark| San Marino| 4 | 0 |  |
| 5414221 | 1381405 | 2023-09-10 | Finland | Denmark | 0 | 1|  |
| 5414263 | 1381448 | 2023-10-14 | Denmark | Kazakhstan | 3 | 1 |  |
| 5414286 | 1385733| 2023-10-17 | San Marino | Denmark | 1 | 2 |  |
| 5414302 | 1381485 | 2023-11-17 | Denmark | Slovenia | 2 | 1 |  |
| 5414323 | 1381506 | 2023-11-20 | Northern Ireland | Denmark | 2 | 0 |  |

### Add ideas on what we could analyse

| Idea | Type | Data Provider | Dataset | Effort | Priority | Notes | Status |
|-----:|-----:|--------------:|--------:|-------:|---------:|------:|------:|
| Ball possession Analysis | Descriptive | Skillcorner | match_id_dynamic_events.csv | Low | High | calculate which team had how much ball possession in percentage | Done |
| Player possession Analysis | Descriptive | Skillcorner | match_id_dynamic_events.csv | Low | High | calculate which player had the most ball possession per game | Done |
| third end analysis | Descriptive | Skillcorner | match_id_dynamic_events.csv | Low | High | calculate in which third the ball was most of the time | Done |
| Type of goal | Descriptive | skillcorner | match_id_dynamic_events.csv | Low | High | Show what the preceding play action was before a goal (penatly, free kick, corner, in game) | TODO |
| ball heatmap | Descriptive | Wyscout | match_id.json | Mid | High | Make a heatmap for the ball per game | TODO | 
| Player heatmap | Descriptive | Wyscout | match_id.json | High | Low | Make heatmaps for key players | TODO  |
| Analyse squad depth | Descriptive | \- | \- | Low | High | Make descriptive analytics on how many players were subbed during games to show options | TODO |
| Endurance check | Descriptive | Wyscout | match_id.json | High | High | Show which player ran how much and thus show endurance of a team | TODO |
| Post-Match Rest Time | Descriptive | \- | \- | Mid | High | Analyse whether there are correlations with endurance for example when there were long travels after a game and little rest time | TODO |
| Sentiment Analysis | Descriptive | Social Media? | \- | High | Low | Include a sentiment analysis for post-match interviews | TODO |
| Type of Goal (in depth) | Descriptive | Wyscout / Skillcorner |  | Mid | High | Analyse from which position the goals were shot, analyse how many passes there were before a goal, how much time there was since first ball possesion and then goal | TODO |


### Hints (delete after reading)

Your task is to populate this page with an opposition analysis.
You have been assigned an opponent, and you have access to data from the European Qualifiers and from friendlies of the hosts.

Based on an analysis of the opponent team's behaviors, you are asked to formulate expectations about the players they are likely to field, the formations they might use, their strategies for set pieces, and so on. Ideally, you would conclude with recommendations for the coaching staff of your team, informing them about key aspects of the opponent's behaviors and possible measures to counter them.

Please start by 

- [ ] entering your @handles and names in the Project Group section at the top of the page


You are welcome to focus on whatever analyses resonate with you or may be interesting about this opponent. 
Be creative, look around what other groups are doing, and offer any code examples of general interest in the [snippet repository](https://gitlab.ethz.ch/socceranalytics/uefa-euro-2024/-/snippets).

For each figure, chart, or analysis you include, please link to the source of information and the code you used for it. This can be external libraries or some of the snippets provided by yourself or others. 
You may also want to create additional wiki pages to provide more extensive background on an idea.


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

## To-Do's:
- Skripte verstehen und zum laufen bringen (Github, Jupyter-Notebook, Python)
- Daten verstehen
- Erste Ideen, welche Dataen zu analysieren
