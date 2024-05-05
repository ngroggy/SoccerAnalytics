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
<summary>TA Comments :warning: April 19 </summary>

Your teaching assistant is Ivana (@ismokovic) and can be reached at ismokovic@ethz.ch 

- [ ] when saving, please indicate what you changed in a meaningful commit messages
- [x] draft due: **Monday, April 8**
- Good start! Overall you have implemented some nice ideas – would be great if you could extend to include data from other matches to get a feeling of Slovenia’s patterns of play and how Denmark could exploit weaknesses. I see from your message you are already planning to do this, so keep it up!
- You make some claims about 442 formations but it is not clear where you are taking this from.
- Attacking style: you say that Slovenia’s attack is mainly characterized by long balls and counter attacks, but seems that 35% of their attacking style is attributed to build up?
- Passing network: nice interpretation (difficulty linking defense and midfield… is this a pattern across games or did Denmark do something special last time?)
- Interesting that you look into the centralities of the passing networks, but it is not clear what the centralities can tell us about the passing networks / how we can interpret the results. 
- Some heatmaps have some interesting features: concentrations on two opposite sides of the pitch – would be interesting to understand what that means… is it real or consequence of skillcorner’s player detection?
- You have a lot of maps showing where certain actions happened, but not clear what we can take from these in terms of preparing Denmark for the match. If you compare across the other qualifying matches, perhaps you see some trends / patterns which can give us a hint of what to expect more concretely?
- Some of your set piece analysis might be more informative when including other matches (see comment above).
- Nice that you have a summary at the end of the report with weaknesses and suggested tactics
- Please remember that details of how each piece of analysis / visualization was produced (either by linking to the relevant snippets, online sources, or providing your own source code directly) **MUST** be provided, and we expect each visualization to be accompanied by a meaningful interpretation.
- [ ] final version due: **Friday, May 24** 
</details>




### Comments for the TA

Hello Ivana,

In our preliminary draft, we've chosen to consolidate statistics from a specific previous game in Slovenia, with our main focus on extracting and elucidating the data.

For the final version, we plan to:

1. Gather statistics for all previous matches.
2. Potentially include more advanced metrics like pitch control.
3. Not only describe the statistics but also analyze them, illustrating situations in which Slovenia could be strong or expose weaknesses.


### TODOs:

- [ ] Good start! Overall you have implemented some nice ideas – would be great if you could extend to include data from other matches to get a feeling of Slovenia’s patterns of play and how Denmark could exploit weaknesses. I see from your message you are already planning to do this, so keep it up!
- [x] You make some claims about 442 formations but it is not clear where you are taking this from.
- [ ] Attacking style: you say that Slovenia’s attack is mainly characterized by long balls and counter attacks, but seems that 35% of their attacking style is attributed to build up?
- [ ] Passing network: nice interpretation (difficulty linking defense and midfield… is this a pattern across games or did Denmark do something special last time?)
- [ ] Interesting that you look into the centralities of the passing networks, but it is not clear what the centralities can tell us about the passing networks / how we can interpret the results. 
- [ ] Some heatmaps have some interesting features: concentrations on two opposite sides of the pitch – would be interesting to understand what that means… is it real or consequence of skillcorner’s player detection?
- [ ] You have a lot of maps showing where certain actions happened, but not clear what we can take from these in terms of preparing Denmark for the match. If you compare across the other qualifying matches, perhaps you see some trends / patterns which can give us a hint of what to expect more concretely?
- [ ] Some of your set piece analysis might be more informative when including other matches (see comment above).
- [ ] Nice that you have a summary at the end of the report with weaknesses and suggested tactics
- [x] Please remember that details of how each piece of analysis / visualization was produced (either by linking to the relevant snippets, online sources, or providing your own source code directly) **MUST** be provided, and we expect each visualization to be accompanied by a meaningful interpretation.

# Match \#06 (SVN-DEN): preparing Denmark to play against Slovenia


<!------------ START YOUR REPORT BELOW THIS LINE --------------->
# Preparation Denmark 🇩🇰 to play against Slovenia 🇸🇮 !
<p align="center">
![Teamphoto](uploads/dcb4d4858962b5f92e6d2296b9d8bb79/Teamphoto.png)
</p>




## 1. Introduction

### 1.1 General comments

Despite Denmark holding the 21st position in the FIFA rankings, and Slovenia being ranked at 55, overlooking a theoretically weaker opponent is never advisable. During the last game against Slovenia (Qualifiers Euro 23) we won with 2-1 in a complicated game while we got a draw 6 month earlier with 1-1 (Qualifiers Euro 23). In this analysis, we'll provide you with all the essential keys to ensure success against Slovenia in the upcoming match.

Our preparation for the group match of the European Championship consists in a first step of the analysis of the direct encounter between Denmark and Slovenia in the European Championship qualification which took place on 17.11.23. In a further analysis in the next draft, additional meshes will be added to support our statements.

Based on information from multiple sources, it's seems evident that Slovenia's team possesses notable strengths at some positions. Specifically, their goalkeeper, currently playing for Atlético, stands out, alongside midfielders Benjamin Sesko and Jaka Bijol. Given their midfield/attack roles, it's reasonable to anticipate Slovenia boasting a strong midfield/attack presence.

After analyzing their recent matches, it's evident that Slovenia employed a traditional 4-4-2 formation with no unexpected variations in player selection. Additionally, one of the standout players we identified, Sesko, managed to score a goal during the game. We should keep in mind that the 4-4-2 formation brings a central presence that enables counter-attacks.

### 1.2 Last 5 qualifier games slovenia

| wyscout | skillcorner | date       | home             | away       | Score Home | Score Away |
| ------: | ----------: | ---------- | ---------------- | ---------- | ---------- | ---------- |
| 5414226 |     1385659 | 2023-09-10 | San Marino       | Slovenia   | 0          | 4          |
| 5414260 |     1381446 | 2023-10-14 | Slovenia         | Finland    | 1          | 3          |
| 5414284 |     1381466 | 2023-10-17 | Northern Ireland | Slovenia   | 0          | 1          |
| 5414302 |     1381485 | 2023-11-17 | Denmark          | Slovenia   | 2          | 1          |
| 5414324 |     1381505 | 2023-11-20 | Slovenia         | Kazakhstan | 2          | 1          |

### 1.3 Injured & suspended players

Currently Benjamin Verbič is injured and doesn't have an official return date. No suspension need to be taken into account at this point.

## 2. Statistics of Slovenia's recent games

### 2.1 Formation and line up

We start first by analysing the common composition of Slovenia. In the last 10 games against Portugal, Malta, USA, Kazakhstan, Denamrk, North Ireland and Finland, Slovenia used 9 times a 4-4-2 composition and the only modified composition was when Benjamin Sesko wasn't available. Therefore we can excpect the composition to be probably the same. Here is a quick recap of pro ans cons of the 4-4-2 composition.

| 26 Mar vs Portugal | 21 Mar vs Malta | 20 Jan vs USA | 20 Nov vs Kazakhstan | 17 Nov vs Denmark |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| ![vs_portugal](uploads/a0f20c331963edf02f6298edc7fd9744/vs_portugal.png) | ![vs_malta](uploads/0343977259e92b21fc9084a2b899c27b/vs_malta.png)|![vs_usa](uploads/c7cef98b8e18248667adee6c0cfb168e/vs_usa.png) | ![vs_khazakhtan](uploads/4e8a07126922117730e2f33efeb3aaf3/vs_khazakhtan.png)|![vs_denmark](uploads/eebe07a8839e6b121098b6a9b537adfe/vs_denmark.png) |

|17 Oct vs N. Ireland | 14 Oct vs Finland | 10 Sep vs San Marino | 7 Sep vs N. Ireland | 19 Jun vs Denmark |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| ![vs_portugal](uploads/a0f20c331963edf02f6298edc7fd9744/vs_portugal.png) | ![vs_malta](uploads/0343977259e92b21fc9084a2b899c27b/vs_malta.png)|![vs_usa](uploads/c7cef98b8e18248667adee6c0cfb168e/vs_usa.png) | ![vs_khazakhtan](uploads/4e8a07126922117730e2f33efeb3aaf3/vs_khazakhtan.png)|![vs_denmark](uploads/eebe07a8839e6b121098b6a9b537adfe/vs_denmark.png) |

Here is a quick refresh of the pros and cons of 4-4-2:

**Pros :** With a strong defense, wide attack, and quick movement into the opponent's territory, the 4-4-2 excels in counter-attacks. Defensively, it allows for a compact setup with two lines of four players, while the forwards remain poised for quick offensive opportunities. The presence of two strikers presents a unique challenge for defenders, as it reduces time and space on the ball and increases the threat of one-on-one situations. Additionally, passing out from the back becomes more challenging with constant pressure from two attackers.

**Cons :** In a 4-4-2 formation, teams may struggle to control the midfield, especially against opponents using a midfield trio, leading to less possession. Additionally, the 4-4-2 lacks defensive depth, as players within the same line may leave gaps. Despite being compact, this formation is vulnerable to line-breaking passes, making it easier for opponents to bypass multiple players at once. Defensive setups like the 4-1-4-1 offer better coverage between the lines.When attacking, the midfield and defensive lines align closely, restricting forward passing options. This setup can limit the team's ability to create passing opportunities compared to formations with players spread across different lines.

<details><summary>Sources</summary>

Images: They are screenshot of Google Chrome output when we type : Last games of slovenia

1. [Coachesvoice](https://www.coachesvoice.com/cv/4-4-2-football-tactics-ferguson-simeone-hasenhuttl-dyche/#:~:text=There%20can%20also%20be%20a,out%20four%20players%20at%20once.)
2. [Jobs in football](https://jobsinfootball.com/blog/tactics/4-4-2-formation/)
3. [Build line up](https://www.buildlineup.com/articles/1/football-formation-4-4-2)
4. [Coachesvoice](https://www.coachesvoice.com/cv/4-4-2-diamond-football-tactics-explained-klopp-potter-allegri/)
5. [Comment jouer le 4-4-2 (in french)](https://www.entrainement-foot.fr/blog/tactique-comment-jouer-en-4-4-2-guide-complet#)

</details>

### 2.2 Key statistics


We start by analyzing the direct qualifier match between Denmark and Slovenia on November 17, 2023. The game was largely dominated by Denmark, as evidenced by their 70% possession and a significant advantage in passes, which was double that of Slovenia's. The dominance was further highlighted by the shots on target, with Denmark having 8 compared to Slovenia's 1.

Despite the apparent control over the game by Denmark, the margin of victory was narrow, with Denmark winning by just one goal. This outcome is further clarified upon examining the expected goals metric. Denmark's expected goals stood at 1.33, indicating that despite their dominance, they struggled to create substantial scoring opportunities. On the other hand, Slovenia's expected goals were at 0.13, suggesting their goal could be attributed to a fortunate strike rather than a consistent offensive effort.

![key_statistics](uploads/ad439dbaebe9cea015aefcd5e2bc5c75/key_statistics.png)

<details>
  <summary> code </summary>

```python
# load data
match_id = "5414302"
df_events = pd.read_csv(f"./results/wyscout/{match_id}_df_events.csv", index_col=0)

team_type_counts = df_events.groupby(['team.name', 'type.primary']).size().unstack(fill_value=0)
shots_dnk = df_events[(~df_events["shot.isGoal"].isnull()) & (df_events["team.name"] == "Denmark")]
shots_svn = df_events[(~df_events["shot.isGoal"].isnull()) & (df_events["team.name"] == "Slovenia")]
passes_completed = df_events[df_events["type.primary"] == "pass"].groupby(['team.name'])['pass.accurate'].sum()
possession = df_events.groupby("team.name")["possession.duration"].sum() / df_events["possession.duration"].sum()

team2 = 'Denmark'
dnk_data = {'Goals': shots_dnk['shot.isGoal'].sum(),
            'Shots': shots_dnk.shape[0],
            'Shots on target': shots_dnk['shot.onTarget'].sum(),
            'Exp. goals': shots_dnk['shot.xg'].sum().round(2),
            'Possession': (possession.loc[team2]).round(2), # in percent
            'Passes': team_type_counts.loc[team2, 'pass'],
            'Pass accuracy': (passes_completed.loc[team2] / team_type_counts.loc[team2, 'pass']).round(2),
            'Freekicks': team_type_counts.loc[team2, 'free_kick'],
            'Corners': team_type_counts.loc[team2, 'corner'],
            'Infractions': team_type_counts.loc[team2, 'infraction'],
            'Yellow cards': df_events[(df_events["team.name"] == team2) & (df_events["infraction.yellowCard"] == True)].shape[0],
            'Red cards': df_events[(df_events["team.name"] == team2) & (df_events["infraction.redCard"] == True)].shape[0],
            }

team1 = 'Slovenia'
svn_data = {'Goals': shots_svn['shot.isGoal'].sum(),
            'Shots': shots_svn.shape[0],
            'Shots on target': shots_svn['shot.onTarget'].sum(),
            'Exp. goals': shots_svn['shot.xg'].sum().round(2),
            'Possession': (possession.loc[team1]).round(2), # in percent
            'Passes': team_type_counts.loc[team1, 'pass'],
            'Pass accuracy': (passes_completed.loc[team1] / team_type_counts.loc[team1, 'pass']).round(2),
            'Freekicks': team_type_counts.loc[team1, 'free_kick'],
            'Corners': team_type_counts.loc[team1, 'corner'],
            'Infractions': team_type_counts.loc[team1, 'infraction'],
            'Yellow cards': df_events[(df_events["team.name"] == team1) & (df_events["infraction.yellowCard"] == True)].shape[0],
            'Red cards': df_events[(df_events["team.name"] == team1) & (df_events["infraction.redCard"] == True)].shape[0],
            }

# if category % do not normalize
perc_categories = ['Possession', 'Pass accuracy']


def normalize_value(key, value, compare_value, perc_categories=None):
    """ Normalize or pass the value through based on category """
    if key not in perc_categories and max(value, compare_value) >= 0.001:
        return value / max(value, compare_value)
    return value


def add_value_labels(ax, values, labels, y_pos, is_left=True):
    """ Add value labels to the bars """
    for i, (value, label) in enumerate(zip(values, labels)):
        if is_left:
            ax.text(min(value - 0.05, -0.2), y_pos[i], str(label),
                    va='center', ha='right', color='black', fontsize=10)
        else:
            ax.text(max(value + 0.05, 0.2), y_pos[i], str(label),
                    va='center', ha='left', color='black', fontsize=10)


def plot_stats_barchart(team1_stats, team2_stats, team1_name=None, team2_name=None, perc_categories=None, title="", subtitle="",
                        team1_color='red', team2_color='blue', saveplt=False, savepath=None):
    """ Display a bar chart comparing the match statistics between two teams"""

    # Normalizing values within each category between the teams, except for percentage categories
    normalized_dnk_data = {key: normalize_value(
        key, value, team2_stats[key], perc_categories) for key, value in team1_stats.items()}
    normalized_svn_data = {key: normalize_value(
        key, value, team1_stats[key], perc_categories) for key, value in team2_stats.items()}
    team_1_values = list(normalized_dnk_data.values())[::-1]
    team_2_values = list(normalized_svn_data.values())[::-1]

    # Original values for displaying at the end of bars
    original_team_1_values = list(team1_stats.values())[::-1]
    original_team_2_values = list(team2_stats.values())[::-1]

    # Categories for the y-axis
    categories = list(team1_stats.keys())[::-1]

    # The y position for the bars
    y_pos = np.arange(len(categories))

    # Create the figure and the axes
    fig, ax = plt.subplots(figsize=(10, len(categories) * 0.5))
    fig.patch.set_facecolor('white')

    # Draw bars for team 1 and team 2

    # Fix for bar centering issue
    if 1.0 not in team_1_values:
        hval_idx = np.argmax(np.asarray(original_team_1_values))
        team_1_values[hval_idx] = 1.0
    if 1.0 not in team_2_values:
        hval_idx = np.argmax(np.asarray(original_team_2_values))
        team_2_values[hval_idx] = 1.0
        
    ax.barh(y_pos, team_1_values, color=team1_color, alpha=0.6)
    ax.barh(y_pos, [-value for value in team_2_values],
            color=team2_color, alpha=0.6)

    # Add data labels inside the bars (categories)
    for y, category in zip(y_pos, categories):
        ax.text(0, y, category, va='center',
                ha='center', color='black', fontsize=10)

    # Add value labels to the bars (team values)
    add_value_labels(ax, team_1_values, original_team_1_values,
                     y_pos, is_left=False)
    add_value_labels(ax, [-v for v in team_2_values],
                     original_team_2_values, y_pos, is_left=True)

    ax.text(1, 1.1, team1_name, transform=ax.transAxes, ha='right',
            va='bottom', color=team1_color, fontsize=16, fontweight='bold')
    ax.text(0, 1.1, team2_name, transform=ax.transAxes, ha='left',
            va='bottom', color=team2_color, fontsize=16, fontweight='bold')

    # Set the labels and title (if needed)
    ax.set_title(f"{title}", fontsize=18, fontweight='bold', pad=40)
    ax.text(0.5, 1.02, f"{subtitle}", fontsize=16, fontweight='bold',
            ha='center', va='bottom', transform=ax.transAxes)

    # Remove the spines and ticks, and add gridlines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    plt.axvline(0, color='grey', linewidth=0.8)
    ax.xaxis.grid(False)
    ax.legend().set_visible(False)

    plt.tight_layout()

    if saveplt is True and savepath is not None:
        plt.savefig(savepath, dpi=400)

    plt.show()

# plot statistics
plot_stats_barchart(svn_data, dnk_data, team1_name='Slovenia', team2_name='Denmark', perc_categories=perc_categories, title='EM Qualifier: 2023-11-17',
                    subtitle='2:1', team1_color='blue', team2_color='red', saveplt=True, savepath='plots/2-statistics/key_statistics.png')
```

</details>

## 3. In possesion - attack of Slovenia

Our analysis of Slovenia's attacking performance in the European Championship qualifier against Denmark on November 17, 2023, serves as the initial basis for evaluating their offensive strategy. Future analyses will encompass a broader range of matches to provide a more comprehensive assessment.

### 3.1 Attacking style:

Slovenia's approach to attacking was markedly different from Denmark's, particularly in their avoidance of prolonged build-up plays. Instead, Slovenia's offensive strategy was predominantly characterized by quick counter-attacks and the utilization of long balls to advance up the field swiftly when in possession.

![attacking_style](uploads/5f9291eff54bbfe0fbf6c9cb803f6803/attacking_style.png)

<details>
  <summary> code </summary>
  
  ```python
# load data
match_id = "5414302"
df_events = pd.read_csv(f"./results/wyscout/{match_id}_df_events.csv", index_col=0)


team_category_perc = (team_category_counts.div(team_category_counts.sum(axis=1), axis=0)).round(2)

dnk_data = {'Build Up': team_category_perc.loc['Denmark', 'build_up'].round(2),
            'Progression': team_category_perc.loc['Denmark', 'progression'].round(2),
            'Final Third': team_category_perc.loc['Denmark', 'final_third_play'].round(2),
            'Long Ball': team_category_perc.loc['Denmark', 'long_ball'],
            'Counter Attack': team_category_perc.loc['Denmark', 'counter_attack'],
            'Set Piece': team_category_perc.loc['Denmark', 'set_piece'],
}

svn_data = {'Build Up': team_category_perc.loc['Slovenia', 'build_up'],
            'Progression': team_category_perc.loc['Slovenia', 'progression'],
            'Final Third': team_category_perc.loc['Slovenia', 'final_third_play'],
            'Long Ball': team_category_perc.loc['Slovenia', 'long_ball'],
            'Counter Attack': team_category_perc.loc['Slovenia', 'counter_attack'],
            'Set Piece': team_category_perc.loc['Slovenia', 'set_piece'],
}

# if category % do not normalize
perc_categories = ['Build Up', 'Progression', 'Final Third', 'Long Ball', 'Counter Attack', 'Set Piece']

# use functions from 2.2
plot_stats_barchart(svn_data, dnk_data, team1_name='Slovenia', team2_name='Denmark', perc_categories=perc_categories, title='EM Qualifier: 2023-11-7 (2:1)',
                    subtitle='Attacking style', team1_color='blue', team2_color='red', saveplt=True, savepath='plots/3-attack/attacking_style.png')
```
</details>


### 3.2 Attacking efficiency

The effectiveness of Slovenia's attacking maneuvers was notably lacking. A mere 1% of their attacking efforts resulted in a shot, with none of these attempts being on target. The sole goal they managed to score originated from a free kick taken approximately 35 meters from the goal. Additionally, Slovenia's performance in offensive duels and dribbling was significantly inferior to that of Denmark, further highlighting the inefficacies in their attacking play.

![attacking_efficiency](uploads/c016c0038385df6ea41ffa43fa14274d/attacking_efficiency.png)

<details>
  <summary> code </summary>

```python
# load data
match_id = "5414302"
df_events = pd.read_csv(f"./results/wyscout/{match_id}_df_events.csv", index_col=0)

def calculate_attacking_efficiency(team_name):

  team_events = df_events[df_events["possession.team.name"] == team_name]

  # Attacks
  with_flank = team_events[(~team_events["possession.attack.flank"].isna())]['possession.id'].nunique()
  with_shot = team_events[(team_events["possession.attack.withShot"] == True)]['possession.id'].nunique()
  with_shot_on_target = team_events[(team_events["possession.attack.withShotOnGoal"] == True)]['possession.id'].nunique()
  with_goal = team_events[(team_events["possession.attack.withGoal"] == True)]['possession.id'].nunique()
  total_events = team_events["possession.id"].nunique()

  # Offensive Duels
  offensive_duels = team_events[(team_events["groundDuel.duelType"] == "offensive_duel")]
  offensive_duels_won = offensive_duels[offensive_duels["groundDuel.keptPossession"] == True]

  # Dribbles
  dribbles = team_events[(team_events["groundDuel.duelType"] == "dribble")]
  dribbles_won = dribbles[dribbles["groundDuel.keptPossession"] == True]


  return {
      'Attack With Flank': round(with_flank / total_events, 2),
      'Attack With Shot': round(with_shot / total_events, 2),
      'Attack With Shot on Goal': round(with_shot_on_target / total_events, 2),
      'Attack With Goal': round(with_goal / total_events, 2),
      'Offensive Duels': round(offensive_duels.shape[0], 2),
      'Offensive Duels Won': round(offensive_duels_won.shape[0] / offensive_duels.shape[0], 2),
      'Dribbles': round(dribbles.shape[0], 2),
      'Dribbles Won': round(dribbles_won.shape[0] / dribbles.shape[0], 2),
  }
  
# Use the function to calculate stats for Denmark and Slovenia
dnk_data = calculate_attacking_efficiency("Denmark")
svn_data = calculate_attacking_efficiency("Slovenia")

# if category % do not normalize
perc_categories = ["Attack With Flank", "Attack With Shot", "Attack With Shot on Goal", "Attack With Goal", "Offensive Duels Won", "Dribbles Won"]

# use functions from 2.2
plot_stats_barchart(svn_data, dnk_data, team1_name='Slovenia', team2_name='Denmark', perc_categories=perc_categories, title='EM Qualifier: 2023-11-17 (2:1)',
                subtitle='Attacking efficiency', team1_color='blue', team2_color='red', saveplt=True, savepath='plots/3-attack/attacking_efficiency.png')
```
</details>


### 3.3 Passing network & Player Heatmap

### Passing network

In the picture you can see the more passes have been played by a player. The bigger his name circle. The position of the circle was determined by taking the average position of all the passes made by a player. 

A look at Slovenia's passing network mirrors the statistics from chapter 2. Slovenia were pushed in behind and were rarely able to create a successful build-up between defence and midfield, which points to the many passes between the two centre-backs (Bijol and Blazic) and Oblak. Denmark managed to isolate the midfield and attack from the game, leaving the defence with only the pass to the centre-back or goalkeeper.

Kranicnik takes on an exciting position in the network. His high pass rate could indicate an inverted right-back. However, it also suggests that the build-up was often attempted via the right flank with Karnicnik and Cerin as the main figures.


|Kazakhstan|Denmark|N_Ireland|
|---|---|---|
|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-network/passing_network_Kazakhstan.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-network/passing_network_Denmark.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-network/passing_network_N_Ireland.png?raw=true" align="center" height="350" width="600"/>|

|Finland|San_Marino|N_Ireland_2|
|---|---|---|
|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-network/passing_network_Finland.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-network/passing_network_San_Marino.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-network/passing_network_N_Ireland_2.png?raw=true" align="center" height="350" width="600"/>|

<details>
  <summary> code </summary>

``` python
import pandas as pd
import numpy as np

from mplsoccer import Pitch, Sbopen
from mplsoccer import VerticalPitch,Pitch
from mplsoccer import Pitch

pitch_length = 120
pitch_width = 80

data = pd.read_csv(f"results/wyscout/5414302_df_events.csv")

data = data[['location.x', 'location.y', 'pass.endLocation.x', 'pass.endLocation.y', "player.name", "pass.recipient.name","team.name","minute",'player.id']]

df_merged = data.rename(columns={
'location.x':'x',
'location.y':'y',
'pass.endLocation.x':'end_x',
'pass.endLocation.y':'end_y',
"player.name":"player_name",
"pass.recipient.name":"pass_recipient_name",
"team.name":"team_name",
"minute":"minute",
"player.id":'player_id'
})


df_home_pass = df_merged[df_merged.team_name != 'Denmark']

# Check player play time
home_player_df = df_merged[df_merged.team_name != 'Denmark'].groupby('player_name').agg({'minute': [min, max]}).reset_index()
home_player_df = pd.concat([home_player_df['player_name'], home_player_df['minute']], axis=1)
home_player_df['minutes_played'] = home_player_df['max'] - home_player_df['min']
home_player_df = home_player_df.sort_values('minutes_played', ascending=False)

home_player_name = home_player_df.player_name[:11].tolist()
df_home_pass = df_home_pass[df_home_pass.player_name.isin(home_player_name)]
df_home_pass = df_home_pass[df_home_pass.pass_recipient_name.isin(home_player_name)]

scatter_df = pd.DataFrame()
for i, name in enumerate(df_home_pass["player_name"].unique()):
    passx = df_home_pass.loc[df_home_pass["player_name"] == name]["x"].to_numpy()
    recx = df_home_pass.loc[df_home_pass["pass_recipient_name"] == name]["end_x"].to_numpy()
    passy = df_home_pass.loc[df_home_pass["player_name"] == name]["y"].to_numpy()
    recy = df_home_pass.loc[df_home_pass["pass_recipient_name"] == name]["end_y"].to_numpy()
    scatter_df.at[i, "player_name"] = name

    #make sure that x and y location for each circle representing the player is the average of passes and receptions
    scatter_df.at[i, "x"] = np.mean(np.concatenate([passx, recx]))
    scatter_df.at[i, "y"] = np.mean(np.concatenate([passy, recy]))

    #calculate number of passes
    scatter_df.at[i, "no"] = df_home_pass.loc[df_home_pass["player_name"] == name].count().iloc[0]
    
#adjust the size of a circle so that the player who made more passes
scatter_df['marker_size'] = (scatter_df['no'] / scatter_df['no'].max() * 900)

#Calculate edge width
df_home_pass["pair_key"] = df_home_pass.apply(lambda x: "_".join(sorted([x["player_name"], x["pass_recipient_name"]])), axis=1)
lines_df = df_home_pass.groupby(["pair_key"]).x.count().reset_index()
lines_df.rename({'x':'pass_count'}, axis='columns', inplace=True)
#setting a treshold
lines_df = lines_df[lines_df['pass_count']> 0]


import matplotlib.pyplot as plt
pitch = Pitch(pitch_color='grass', line_color='white', stripe=True)

fig, ax = pitch.draw()

pitch.scatter(scatter_df.x / 100 * pitch_length, scatter_df.y / 100 * pitch_width, s=scatter_df.marker_size, color='#272822', edgecolors='#EDBB00', linewidth=3, alpha=1, ax=ax, zorder = 3)

for i, row in scatter_df.iterrows():
    pitch.annotate(row.player_name, xy=(row.x/100 * pitch_length +6, row.y/100 * pitch_width), c='white', va='center',
                   ha='center', size=6, weight = "bold", ax=ax, zorder = 4, 
                   bbox=dict(facecolor='#272822', alpha=1, edgecolor='#272822', boxstyle='round,pad=0.4'))
    

for i, row in lines_df.iterrows():
        player1 = row["pair_key"].split("_")[0]
        player2 = row['pair_key'].split("_")[1]
        #take the average location of players to plot a line between them
        player1_x = scatter_df.loc[scatter_df["player_name"] == player1]['x'] / 100 * pitch_length
        player1_y = scatter_df.loc[scatter_df["player_name"] == player1]['y'] / 100 * pitch_width
        player2_x = scatter_df.loc[scatter_df["player_name"] == player2]['x'] / 100 * pitch_length
        player2_y = scatter_df.loc[scatter_df["player_name"] == player2]['y'] / 100 * pitch_width
        num_passes = row["pass_count"]
        #adjust the line width so that the more passes, the wider the line
        line_width = (num_passes / lines_df['pass_count'].max() * 8)
        # adjust the alpha of the lines based on number of passes and set minimum alpha for a fewer pass
        alpha = 0.5 * num_passes / lines_df['pass_count'].max() + 0.5
        #plot lines on the pitch
        pitch.lines(player1_x, player1_y, player2_x, player2_y,
                        alpha=alpha, lw=line_width, zorder=2, color="#EDBB00", ax = ax)

plt.savefig('plots/passing_network.png', dpi=400)
plt.show()

```
</details>

### Centrality metrics

We analyze key centrality metrics and output the 3 strongest players for each metrics:

#### Degree Centrality

Quantifies received passes relative to total players. $`C_D(v) = \frac{\text{Number of passes received by } v}{\text{Total number of players}} = \sum_{u \neq v} A_{uv}`$

| Player  | Value |
| ------------- | ------------- |
| A. Čerin  | 1.5333  |
| J. Bijol | 1.4667  |
| Ž. Karničnik  | 1.3333  |


#### Betweenness Centrality

Identifies players crucial for ball circulation, calculated by their role in shortest paths between others. $`C_B(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}}`$

| Player  | Value |
| ------------- | ------------- |
| V. Drkušić|  0.1163  |
| A. Čerin| 0.0945 |
| Ž. Karničnik| 0.0827  |


#### Closeness Centrality

Evaluates proximity to others in the network for efficient pass reception. $`C_C(v) = \frac{1}{\sum_{u} d(u, v)}`$

| Player  | Value |
| ------------- | ------------- |
| J. Bijol|  0.7500  |
| A. Čerin|  0.7500 |
|B. Šeško| 0.7500 |

#### PageRank Centrality

Assesses a player's influence, considering both connection quantity and quality, akin to Google's PageRank algorithm. $`C_E(v) = \frac{1}{\lambda} \sum_{u} A_{uv} C_E(u)`$


| Player  | Value |
| ------------- | ------------- |
| Ž. Karničnik|  0.1125  |
| J. Bijol|  0.0986 |
|A. Čerin| 0.0949 |

<details>
  <summary> code </summary>

``` python
import pandas as pd
import json
from IPython.display import display
import networkx as nx
import matplotlib.pyplot as plt
from mplsoccer import VerticalPitch, Pitch

def preprocess_team_pass_data(df_events, team_name):
    df_passes = df_events[df_events['type.primary'] == 'pass']
    df_accurate_passes = df_passes[df_passes['pass.accurate'] == True]
    ap_team = df_accurate_passes[df_accurate_passes['team.name'] == team_name]
    filtered_passes = ap_team[['player.name', 'pass.recipient.name', 'location.x', 'location.y']].copy()
    average_positions = ap_team.groupby('player.name').agg({'location.x': 'mean', 'location.y': 'mean'}).reset_index()
    return filtered_passes, average_positions

def create_weighted_graph(df):
    G = nx.DiGraph()
    unique_players = set(df['player.name'])
    unique_recipients = set(df['pass.recipient.name'])

    for index, row in df.iterrows():
        player = row['player.name']
        recipient = row['pass.recipient.name']

        if player is None or recipient is None:
            continue

        if player not in unique_recipients or recipient not in unique_players:
            continue

        if G.has_edge(player, recipient):
            G[player][recipient]['weight'] += 1
        else:
            G.add_edge(player, recipient, weight=1)

    return G

def calculate_top_players(G):
    centrality_measures = {
        "Degree Centrality": nx.degree_centrality(G),
        "Betweenness Centrality": nx.betweenness_centrality(G),
        "Closeness Centrality": nx.closeness_centrality(G),
        "Eigenvector Centrality": nx.eigenvector_centrality(G),
        "PageRank Centrality": nx.pagerank(G) 
    }

    top_players = {}
    # Loop through each centrality measure
    for measure, centrality in centrality_measures.items():
        sorted_centrality = sorted(centrality.items(), key=lambda x: x[1], reverse=True)
        top_players[measure] = [f"{player}: {centrality_value:.4f}" for player, centrality_value in sorted_centrality[:3]]

    return top_players


#example usage
df_events = pd.read_csv(f"results/wyscout/5414302_df_events.csv")
filtered_passes_g, average_positions_g = preprocess_team_pass_data(df_events, 'Slovenia')
G = create_weighted_graph(filtered_passes_g)
values = calculate_top_players(G)

for val in values:
    print(f'#### {val}')
    print(values[val])
```
</details>

### Attacking Players Heatmap

In order to analyze Slovenian's attacking behavior, let's take a look at the thermal images of the attacking and midfield players. From the passing Network from chapter 3.1 and the generated images there is a soft tendency that the attacking play is more developped on the right side, through Vipotnik and Verbic/Mlakar. Mlakar and Verbic kept changing their starting positions during the game. Only on the counterattacks do they act as offensive wingers and only then do they give the strikers the opportunity to move into the center. The outside midfielders are therefore very defensively prepared for this game and help out the full-backs.

It is also clear that Slovenian were mainly occupied with defending and Sesko and Vipotnik therefore received little support up front. Elsnik and Cerin took over the position of the typical number 8 and rarely dropped deep to the side and kept the center closed.

![FrontRow](uploads/b5f78ba57adbbe3d904a1d29f327af50/FrontRow.png)

![SecondRow](uploads/4e84976150b60afde79ac028f1cee00f/SecondRow.png)

<details>
  <summary> code </summary>

#### Create an array with players you want to see

```python
  player = ['B. Šeško', 'J. Kurtič', 'Ž. Karničnik']
    for pl in player:
        df_player = df[df['player.name'] == pl]

    pitch = VerticalPitch(pitch_color='#2f8c58',
                          line_color='white',
                          pitch_type='wyscout')

    fig, ax = pitch.grid(grid_height=0.9, title_height=0.06, axis=False,
                         endnote_height=0.04, title_space=0, endnote_space=0)

    # Heatmap as Kernel Density Estimation
    pitch.kdeplot(
    x=df_player['location.x'],
    y=df_player['location.y'],
    shade = True,
    shade_lowest=False,
    alpha=.5,
    n_levels=10,
    cmap = 'coolwarm',
    ax=ax['pitch']
    )

    legend_elements = [Line2D([0], [0], color='w', markerfacecolor='k', marker='o', label=pl)]

    plt.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, 1), bbox_transform=plt.gcf().transFigure,
               handlelength=2, labelspacing=1.2, fontsize=10)

    def replace_dot_space_with_underscore(pl):
        return pl.replace(". ", "_")

    pl = replace_dot_space_with_underscore(pl)

    plt.savefig(f'plots/{pl}_Heatmaps.png', dpi=400)
    plt.show()
```

</details>

### 3.4 Typical tactical moves

#### 3.4.1 Long passes

The Slovenians' great strength lies in the long passes from their two central defenders. The long passes from the full-backs have a high error rate. Especially the right side. Slovenia often need this type of pass to get out of pressure situations. However, with a relatively baleful outcome


| Vs : Kazakhstan | Vs : Denmark | Vs : N_Ireland |
|---|---|---|
|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/long_passes_map_Kazakhstan.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/long_passes_map_Denmark.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/long_passes_map_N_Ireland.png?raw=true" align="center" height="350" width="600"/>|

| Vs : Finland | Vs : San_Marino | Vs : N_Ireland_2 |
|---|---|---|
|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/long_passes_map_Finland.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/long_passes_map_San_Marino.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/long_passes_map_N_Ireland_2.png?raw=true" align="center" height="350" width="600"/>|



#### 3.4.2 Crosses

There is no preferred side in the flank play and a clear key player.

| Vs : Kazakhstan | Vs : Denmark | Vs : N_Ireland |
|---|---|---|
|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/crosses_map_Kazakhstan.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/crosses_map_Denmark.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/crosses_map_N_Ireland.png?raw=true" align="center" height="350" width="600"/>|

| Vs : Finland | Vs : San_Marino | Vs : N_Ireland_2 |
|---|---|---|
|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/crosses_map_Finland.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/crosses_map_San_Marino.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/crosses_map_N_Ireland_2.png?raw=true" align="center" height="350" width="600"/>|


#### 3.4.3 Shots 

What is striking about this statistic is that only shots were taken from the second row and therefore from long range. The two strikers did not get a shot on target. Two shots and only one on goal shows how busy Slovenia were defending. Slovenia's efficiency and above all Janza's shooting technique is astonishing. There is a slight tendency to shoot from the right.

| Vs : Kazakhstan | Vs : Denmark | Vs : N_Ireland |
|---|---|---|
|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/shots_map_Kazakhstan.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/shots_map_Denmark.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/shots_map_N_Ireland.png?raw=true" align="center" height="350" width="600"/>|

| Vs : Finland | Vs : San_Marino | Vs : N_Ireland_2 |
|---|---|---|
|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/shots_map_Finland.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/shots_map_San_Marino.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/shots_map_N_Ireland_2.png?raw=true" align="center" height="350" width="600"/>|


#### 3.4.4 Dribblings
Dribbling has only been implemented for the wingers in Slovenia's game. You can rarely expect dribbling from Elsnik and Cerin from the center.
Verbic's dribbling strength in particular must be emphasized here. There is an increased number of dribbles on the right-hand side with a high chance of success. 

| Vs : Kazakhstan | Vs : Denmark | Vs : N_Ireland |
|---|---|---|
|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/duel_map_Kazakhstan.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/duel_map_Denmark.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/duel_map_N_Ireland.png?raw=true" align="center" height="350" width="600"/>|

| Vs : Finland | Vs : San_Marino | Vs : N_Ireland_2 |
|---|---|---|
|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/duel_map_Finland.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/duel_map_San_Marino.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/duel_map_N_Ireland_2.png?raw=true" align="center" height="350" width="600"/>|

#### 3.4.5 Interceptions

Surprisingly, in the center of the Slovenian defense there is a 50/50 chance of success from intercepted balls. Certainly a weak point that Denmark can exploit by coming through the middle or from the left. The right side with Verbic and Karnicnik seems to be like a wall that is difficult to overcome and has a 100% rate of interceptions.

| Vs : Kazakhstan | Vs : Denmark | Vs : N_Ireland |
|---|---|---|
|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/interception_map_Kazakhstan.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/interception_map_Denmark.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/interception_map_N_Ireland.png?raw=true" align="center" height="350" width="600"/>|

| Vs : Finland | Vs : San_Marino | Vs : N_Ireland_2 |
|---|---|---|
|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/interception_map_Finland.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/interception_map_San_Marino.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/interception_map_N_Ireland_2.png?raw=true" align="center" height="350" width="600"/>|

#### 3.4.6 Fouls

| Vs : Kazakhstan | Vs : Denmark | Vs : N_Ireland |
|---|---|---|
|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/fouls_map_Kazakhstan.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/fouls_map_Denmark.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/fouls_map_N_Ireland.png?raw=true" align="center" height="350" width="600"/>|

| Vs : Finland | Vs : San_Marino | Vs : N_Ireland_2 |
|---|---|---|
|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/fouls_map_Finland.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/fouls_map_San_Marino.png?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/notebooks/plots/3-tactical/fouls_map_N_Ireland_2.png?raw=true" align="center" height="350" width="600"/>|


The Slovenians are disciplined and there is a high incidence of fouls in Slovenia's defensive central midfield. Despite a period of high pressure throughout the game, the Slovenians were not tempted to commit many tactical fouls, which indicated that the team was deep and therefore did not allow the Danes to counter-attack. The central midfield did not seem insurmountable and the central midfielders were often only able to help themselves with fouls.


<details>
  <summary> code </summary>
    
```python
def intercept_color_funcion(entry):    
    color = "red"
    if 'loss' in entry['type.secondary']:
        color = "white"
    return color

def duel_color_function(entry):
    color = "red"
    if 'loss' in entry['type.secondary']:
        color = "white"
    return color

def long_passes_color_function(entry):
    color = "red"
    if 'loss' in entry['type.secondary']:
        color = "white"
    return color

def cross_color_function(entry):
    color = "red"
    if 'loss' in entry['type.secondary']:
        color = "white"
    return color

def shot_color_function(entry):
    goal=entry['shot.isGoal']
    color = "white"
    if goal:
        color = "red"
    return color

def fouls_color_function(entry):
    color = "white"
    if 'yellow_card' in entry['type.secondary']:
        color = "yellow"
    return color

def plot_values(type, against, values, color_function, plot_text = False):
    pitch = VerticalPitch(pitch_color='grass', line_color='white', stripe=True)

    fig, ax = pitch.draw()

    for i,entry in values.iterrows():
        #get the information
        x=entry['location.x']
        y=entry['location.y']
        goal=entry['shot.isGoal']
        team_name=entry['team.name']
        #set circlesize
        circleSize=1
        color = color_function(entry)
        # Plot England
        if (team_name=='Slovenia'):
            shotCircle=plt.Circle((y/100.0 * pitch_width, x/100.0 * pitch_length),circleSize,color=color)
            if plot_text:
                plt.text(y/100.0 * pitch_width-4, x/100.0 * pitch_length - 4,entry['player.name'])
            ax.add_patch(shotCircle)

    plt.savefig(f"plots/3-tactical/{type}_map_{against}.png", dpi=400)


data = [("Kazakhstan", "5414324"),("Denmark", "5414324"),("N_Ireland", "5414284"),("Finland", "5414260"),("San_Marino", "5414226")]

for against, match_id in data:
    # Read data
    df_events = pd.read_csv(f"./results/wyscout/{match_id}_df_events.csv", index_col=0)

    # Save values
    plot_values("interception", against, df_events[df_events["type.primary"].str.contains('interception')], intercept_color_funcion)
    plot_values("duel", against, df_events[df_events["type.primary"].str.contains('duel')], duel_color_function)
    plot_values("long passes", against, df_events[df_events["type.secondary"].str.contains('long_pass')], long_passes_color_function)
    plot_values("crosses", against, df_events[df_events["type.secondary"].str.contains('cross')], cross_color_function)
    plot_values("shots", against, df_events[~df_events["shot.isGoal"].isna()],shot_color_function)
    plot_values("fouls", against, df_events[df_events["type.secondary"].str.contains('foul')],fouls_color_function)

```

</details>

## 4 Out of possesion - defense of Slovenia

Our analysis of Slovenia's defensive performance in the European Championship qualifier against Denmark on November 17, 2023, serves as the initial basis for evaluating their offensive strategy. Future analyses will encompass a broader range of matches to provide a more comprehensive assessment.

### 4.1 Statistics

The defensive performance of Slovenia in the match clearly illustrates that their primary focus was on maintaining a robust defense, engaging in almost double the number of defensive duels compared to Denmark. Despite the intense defensive activity, the play remained mostly disciplined, with both teams committing 13 fouls each and Slovenia receiving only one yellow card.

![defense_statistics](uploads/44c2c922ef5ccc7c3b7af7e21eab02cd/defense_statistics.png)

<details>
  <summary> code </summary>

```python
# load data
match_id = "5414302"
df_events = pd.read_csv(f"./results/wyscout/{match_id}_df_events.csv", index_col=0)

team_type_counts = df_events.groupby(['team.name', 'type.primary']).size().unstack(fill_value=0)

team2 = 'Denmark'
dnk_data = {'Defensive Duels': df_events[(df_events["groundDuel.duelType"] == "defensive_duel") & (df_events["team.name"] == team2)]["groundDuel.relatedDuelId"].notna().sum(),
            'Interceptions': team_type_counts.loc[team2, 'interception'],
            'Clearances': team_type_counts.loc[team2, 'clearance'],
            'Fouls': team_type_counts.loc[team2, 'infraction'],
            'Yellow cards': df_events[(df_events["team.name"] == team2) & (df_events["infraction.yellowCard"] == True)].shape[0],
            'Red cards': df_events[(df_events["team.name"] == team2) & (df_events["infraction.redCard"] == True)].shape[0],
            }

team1 = 'Slovenia'
svn_data = {'Defensive Duels': df_events[(df_events["groundDuel.duelType"] == "defensive_duel") & (df_events["team.name"] == team1)]["groundDuel.relatedDuelId"].notna().sum(),
            'Interceptions': team_type_counts.loc[team1, 'interception'],
            'Clearances': team_type_counts.loc[team1, 'clearance'],
            'Fouls': team_type_counts.loc[team1, 'infraction'],
            'Yellow cards': df_events[(df_events["team.name"] == team1) & (df_events["infraction.yellowCard"] == True)].shape[0],
            'Red cards': df_events[(df_events["team.name"] == team1) & (df_events["infraction.redCard"] == True)].shape[0],
            }

# if category % do not normalize
perc_categories = []

# use functions from 2.2
plot_stats_barchart(svn_data, dnk_data, team1_name='Slovenia', team2_name='Denmark', perc_categories=perc_categories, title='EM Qualifier: 2023-11-17 (2:1)',
                    subtitle='Defensive stats', team1_color='blue', team2_color='red',saveplt=True, savepath='plots/4-defense/defense_statistics.png')
```
</details>

### 4.2 Defensive efficiency & style

Slovenia's defensive efforts were markedly more dominant and effective than their attacking endeavors. They outperformed Denmark in terms of winning defensive duels, with a success rate of nearly 80% in their defensive third. Furthermore, Slovenia made fewer defensive errors compared to their opponents, contributing to their solid defensive performance.

In terms of their defensive approach, Slovenia opted for a more conservative style. Rather than engaging in aggressive high pressing, they predominantly focused on maintaining a deep defensive line, concentrating their efforts on defending within their own third.

![defensive_efficiency_style](uploads/1865d7c12a80bfcc19763cd4f594f89f/defensive_efficiency_style.png)

<details>
  <summary> code </summary>

```python
# load data
match_id = "5414302"
df_events = pd.read_csv(f"./results/wyscout/{match_id}_df_events.csv", index_col=0)

def calculate_defensive_efficiency(team_name, opponent_name):

    team_events = df_events[df_events["team.name"] == team_name]

    # Duels
    defensive_duels = team_events[(team_events["groundDuel.duelType"] == "defensive_duel")]
    defensive_duels_ownthird = defensive_duels[(defensive_duels["location.x"] < 33.3)]
    duels_won = defensive_duels[(defensive_duels["groundDuel.stoppedProgress"] == True) | (defensive_duels["groundDuel.recoveredPossession"] == True)].shape[0]
    duels_won_pos = defensive_duels[(defensive_duels["groundDuel.recoveredPossession"] == True)].shape[0]
    duels_won_ownthird = defensive_duels_ownthird[(defensive_duels_ownthird["groundDuel.stoppedProgress"] == True) | (defensive_duels_ownthird["groundDuel.recoveredPossession"] == True)].shape[0]
    total_events = defensive_duels.shape[0]
    total_events_ownthird = defensive_duels_ownthird.shape[0]

    # ball recovery time avg possession duration of opponent
    ball_recovery_time = df_events[(df_events["possession.team.name"] == opponent_name)]["possession.duration"].mean()

    # defensive errors = interceptions + offensive duels lost + dribbles lost in own half
    own_half = df_events[(df_events["location.x"] < 50)]
    interceptions = own_half[(own_half["type.primary"] == "interception") & (own_half["team.name"] == opponent_name)]
    offensive_duels_lost = own_half[(own_half["groundDuel.duelType"] == "offensive_duel") & (own_half["team.name"] == team_name) & (own_half["groundDuel.keptPossession"] == False)]
    dribbles_lost = own_half[(own_half["groundDuel.duelType"] == "offensive_duel") & (own_half["team.name"] == team_name) & (own_half["groundDuel.keptPossession"] == False)]
    defensive_errors = pd.concat([interceptions, offensive_duels_lost, dribbles_lost]).shape[0]

    # Pressure actions
    interceptions = team_events[(team_events["type.primary"] == "interception")]
    clearence = team_events[(team_events["type.primary"] == "clearance")]
    defensive_duels = team_events[(team_events["groundDuel.duelType"] == "defensive_duel")]
    pressures = pd.concat([interceptions, clearence, defensive_duels])

    # High press: Pressure in the opposing third
    high_press = pressures[(pressures["location.x"] > 66.6)]
    mid_press = pressures[(pressures["location.x"] > 33.3) & (pressures["location.x"] < 66.6)]
    low_press = pressures[(pressures["location.x"] < 33.3)]

    return {'Duels Won': round(duels_won / total_events, 2),
            'Duels Won Own Third': round(duels_won_ownthird / total_events_ownthird, 2),
            'Duels Gained Possession': round(duels_won_pos / total_events, 2),
            'Ball Recovery Time': round(ball_recovery_time, 2),
            'Defensive Errors': defensive_errors,
            'High Press': round(high_press.shape[0] / pressures.shape[0], 2),
            'Mid Press': round(mid_press.shape[0] / pressures.shape[0], 2),
            'Low Press': round(low_press.shape[0] / pressures.shape[0], 2),
            }


# Use the function to calculate stats for Denmark and Slovenia
dnk_data = calculate_defensive_efficiency("Denmark", "Slovenia")
svn_data = calculate_defensive_efficiency("Slovenia", "Denmark")

# if category % do not normalize
perc_categories = ["Duels Won", "Duels Won Own Third", "Duels Gained Possession", "High Press", "Mid Press", "Low Press"]

# use functions fromm 2.2
plot_stats_barchart(svn_data, dnk_data, team1_name='Slovenia', team2_name='Denmark', perc_categories=perc_categories, title='EM Qualifier: 2023-11-17 (2:1)',
                    subtitle='Defensive Efficiency & Style', team1_color='blue', team2_color='red', saveplt=True, savepath='plots/4-defense/defensive_efficiency_style.png')
```
</details>

It's clear to see that the 4-man chain was played consistently throughout the game and that they stayed true to their strategy. In other words, the coach doesn't allow himself to be tempted into plan B, C or D, but draws a clear line. Karnicnik is talented on both feet, which must be taken into account when analyzing the game. In very rare cases, the chain dared to cross the halfway line, but for the majority of the game, it certainly focused solely on defending.

![DefensiveRow](uploads/14120d63275d18a01a50b1db56b398a0/DefensiveRow.png)

<details>
  <summary> code </summary>
  
```python

import json
import pandas as pd
from mplsoccer import Pitch, Sbopen
from mplsoccer import VerticalPitch,Pitch
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Patch
from matplotlib.lines import Line2D


# Import the dataset
file_path = 'input/wyscout/5414302.json'
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file) 
    
df = pd.json_normalize(data, record_path=['events'])


# Create an array with players you want to see
player = ['B. Šeško', 'Ž. Vipotnik', 'J. Mlakar', 'T. Elšnik', 'A. Čerin', 'B. Verbič', 'J. Bijol', 'M. Blažič', 'Ž. Karničnik', 'E. Janža' ]
for pl in player:
    df_player = df[df['player.name'] == pl]
        
    # Pitch     
    pitch = VerticalPitch(pitch_color='#2f8c58', 
                          line_color='white', 
                          pitch_type='wyscout')
    
    fig, ax = pitch.grid(grid_height=0.9, title_height=0.06, axis=False,
                         endnote_height=0.04, title_space=0, endnote_space=0)

    # Heatmap as Kernel Density Estimation
    pitch.kdeplot(
    x=df_player['location.x'],
    y=df_player['location.y'],
    shade = True,
    shade_lowest=False,
    alpha=.5,
    n_levels=10,
    cmap = 'coolwarm',
    ax=ax['pitch']
    )

    legend_elements = [Line2D([0], [0], color='w', markerfacecolor='k', marker='o', label=pl)]

    plt.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, 1), bbox_transform=plt.gcf().transFigure,  
               handlelength=2, labelspacing=1.2, fontsize=10)
    
    def replace_dot_space_with_underscore(pl):
        return pl.replace(". ", "_")
    
    pl = replace_dot_space_with_underscore(pl)
    
    plt.savefig(f'plots/{pl}_Heatmaps.png', dpi=400)
    plt.show()
```
</details>


### 4.3 Duel defence performance of the players
In this section the players of the match Denmark-Slovenia on 17.11.2023 are analyzed regarding the duel performance while defending.

#### 4.3.1 Total duels and duels won: Slovenia
The plot below shows the duel performance of the players from Slovenia. It can be seen that J. Bijpol has the most duels with a total of 13. That showcases that Slovenia had to do a lot of defending and especially J. Bijpol made a big impact in the defending line of Slovenia with 11 duels won. Further more the second CB M. Blažič with a total of 7 duels and 6 won duels strenghted the defense of Slovenia as well. A. Čerin made a lot of work in the defence too with a total of 10 duels. Although with only 5 won duels he has a percentage of won duels of 50%, which is improvable.

![duel_performance_svn_final](uploads/853d576009a2834f0b53a4eb90a09da2/duel_performance_svn_final.png)

#### 4.3.2 Duels won percentage: Slovenia
It can be higlighted here that the percentage won of J. Bijol, M. Blažič, B. Verbič and J. Kurtič is over 75%. Therefore they strenghed the defense of slovenia considerably.
J. Kurtič has a percentage of 100%. It has to be considered here that J. Kurtič was substituted in minute 62. Therefore the message of the most percentage needs to be analyzed with the minutes played per player as well.

![duel_percentage_sorted_svn_final](uploads/cd3e796ac13b153997420196cf02b000/duel_percentage_sorted_svn_final.png)

#### 4.3.3 Total duels and duels won: Denmark
Like mentioned in Section 4.2 Denmark was outperformed regarding the defense statistics. V. Kristiansen, J. Maehle and J. Andersen had a total of 6, 6 and 5 total duels. All of them won 4 duels. Therefore it can be said that the CB and RWB of Denmark defend with effort and win most of their defence duels. In the following plot the statistics of Denmark can be seen with all player that had a duel.

![duel_performance_dnk_final](uploads/66b057caa633789604a75eb70511a062/duel_performance_dnk_final.png)

#### 4.3.4 Duels won percentage: Denmark
With J. Andersen, V. Kristiansen and J. Maehle the defence line of denmark has a percentage of over 65% duels won, which is acceptable but also can be improven.
It has to be mentioned that Y. Poulsen with a total of 4 duels and 3 duels won has a percentage of won duels of 75%. The help of the strikers in defending mode can have a big impact on whether the game is won or lost.
In the plot below the stats of Denmark are shown.

![duel_percentage_sorted_dnk_final](uploads/e033f08ba3a262882fabde9b3a3a6784/duel_percentage_sorted_dnk_final.png)

<details>
<summary> code</summary>

```python
# For simplicitiy the code is given for Slovenia only, by changing Slovenia to Denmark it can be analyzed for Denmark too
import pandas as pd
import json
from IPython.display import display
import zipfile
from pathlib import Path
from datetime import datetime, timedelta
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# specfic soccer analysis packages
from mplsoccer import Pitch

# load custom functions
from src.visualization import *
from src.dataloader import dataloader

# Load Data from Slovenia-Danemark November 20, 2023
match_id = "5414302"
df_events = dataloader(match_id)
df_events.columns

# duel events
df_duels = df_events[df_events['type.primary'] == 'duel']

# defensive duels slovenia
df_dduels_svn = df_duels[(df_duels['team.name'] == 'Slovenia') & (df_duels["groundDuel.duelType"] == "defensive_duel")]
dduels_svn = df_dduels_svn.shape[0]

# get the players who had a duel in the game
df_dduels_svn_players = df_dduels_svn['player.name'].dropna().unique()

# get the number of duel per player
df_dduels_svn_player_count = df_dduels_svn['player.name'].dropna().value_counts()

# get the duels that were won
df_dduelswon_svn = df_dduels_svn[df_dduels_svn['player.name'].notna() & ((df_dduels_svn["groundDuel.stoppedProgress"] == True) | (df_dduels_svn["groundDuel.recoveredPossession"] == True))]
# duels won per player
df_dduelwon_svn_player_count = df_dduelswon_svn['player.name'].value_counts()


aligned_counts_svn = pd.concat([df_dduels_svn_player_count, df_dduelwon_svn_player_count], axis=1, keys=['total_duels', 'duels_won']).fillna(0)
aligned_counts_svn['percentage_won'] = ((aligned_counts_svn['duels_won']) / (aligned_counts_svn['total_duels']) * 100).round(0)

# -------------------------------------------------------------------------------------
# Plot 1 Slovenia
# Set Seaborn theme and color palette
sns.set_theme(style="darkgrid")
palette = sns.color_palette("viridis", len(aligned_counts_svn))

# Plotting the data using Seaborn and Matplotlib
plt.figure(figsize=(10, 6))

# Plot total duels
sns.barplot(x=aligned_counts_svn.index, y=aligned_counts_svn['total_duels'], color=palette[3], label='Total Duels')

# Plot duels won
sns.barplot(x=aligned_counts_svn.index, y=aligned_counts_svn['duels_won'], color=palette[10], label='Duels Won')

# Annotate bars with percentage of duels won
#for i, (percentage, player) in enumerate(zip(aligned_counts['percentage_won'], aligned_counts.index)):
#    plt.text(i, aligned_counts.loc[player, 'duels_won'] + 1, f'{percentage}%', ha='center', color='red' if percentage > 75 else 'black')

# Adding labels and title
plt.xlabel('Player')
plt.ylabel('Count')
plt.title('Duel Performance per Player: Slovenia')
plt.xticks(rotation=45, ha='right')

# Show legend
plt.legend()

# Save plot to a specified path
save_path = 'C:/Users/loris/Documents/ETH Zürich/Master/Soccer Analytics/duel_performance_svn.png'  # Specify your desired save path here
plt.tight_layout()
plt.savefig(save_path)


# Plot 2 Slovenia Sorted Percentage
# ---------------------------------------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.barplot(x=aligned_counts_svn_sorted.index, y=aligned_counts_svn_sorted['percentage_won'], color=palette[3])

# Adding labels and title
plt.xlabel('Player')
plt.ylabel('Percentage of Duels Won')
plt.title('Percentage of Duels Won per Player: Slovenia')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Save plot to a specified path
save_path = 'C:/Users/loris/Documents/ETH Zürich/Master/Soccer Analytics/duel_percentage_sorted_svn.png'  # Specify your desired save path here
plt.tight_layout()
plt.savefig(save_path)

```
</details>

### 4.4 Goalkeeper behaviour

To the analysis of the defense the goal keeper needs also to be considered. He is a main part of the defense not only that he is the last man who can save a shot on target but also for his view over the pitch. He can manage his defense optimal and help the defense to understand the play style of the opponent strikers. In the first part the shot parried per goalkeeper are analysed and in the second part the passes played per goalkeeper.

#### 4.4.1 Shots parried per goalkeeper

It can be seen two plot below that Denmark had a total of 8 shot on target and 2 goals scored. For J. Oblak, the goalkeeper of Slovenia, it therefore makes a percentage of parried shots on targets of 75%.
With a percentage parried of 0% K. Schmeichel the goalkeeper of Denmark does not have a good statistic only regarding the game from November 17, 2023. With a shot on target of 1 and 1 scored goal the Slovenien strikers where 100% effective when the shot was on target.

By analayzing the goal zone where the shot hit the goal it can be seen which saves the goalkeepers needed to do. In the following picture the goal zones according to Wyscout are shown.

![wyscout_goal](uploads/1fad8af06a7d6a3d097f200d43c1e6ca/wyscout_goal.png)

It can be seen from the chart below that J. Oblak had to parry a lot of low shots in the centre and his left corner.
The shot from Slovenia, it was a free kick, was shot in the top right corner from striker side of view and K. Schmeichel was not able to parry the shot.

![Shots_parried](uploads/f58574f5296f99418f1f3349f44a6e2d/Shots_parried.png)

<details>
<summary> code</summary>

```python
# The import part is the same as in Section 4.3

# Goalkeeper events: Shot on Target
df_goalkeeper = df_events[(df_events['shot.onTarget'] == True)]
display(df_goalkeeper)

# Shot on target from Denmark (In final version the goalkeeper is not hard coded)
df_ontarget_dnk = df_goalkeeper[(df_goalkeeper['shot.onTarget'] == True) & (df_goalkeeper['shot.goalkeeper.name'] == 'J. Oblak')]
df_ontarget_dnk_count = df_ontarget_dnk.shape[0]
#print("Shot on Target from Denmark")
#print(df_ontarget_dnk_count)

# Shot on target from Slovenia
df_ontarget_svn = df_goalkeeper[(df_goalkeeper['shot.onTarget'] == True) & (df_goalkeeper['shot.goalkeeper.name'] == 'K. Schmeichel')]
df_ontarget_svn_count = df_ontarget_svn.shape[0]
#print("Shot on Target from Slovenia")
#print(df_ontarget_svn_count)

# Shot is Goal Denmark
df_isgoal_dnk = df_goalkeeper[(df_goalkeeper['shot.isGoal'] == True) & (df_goalkeeper['shot.goalkeeper.name'] == 'J. Oblak')]
df_isgoal_dnk_count = df_isgoal_dnk.shape[0]
#print("Shot is Goal from Denmark")
#print(df_isgoal_dnk_count)

# Shot is Goal Slovenia
df_isgoal_svn = df_goalkeeper[(df_goalkeeper['shot.isGoal'] == True) & (df_goalkeeper['shot.goalkeeper.name'] == 'K. Schmeichel')]
df_isgoal_svn_count = df_isgoal_svn.shape[0]
#print("Shot is Goal from Slovenia")
#print(df_isgoal_svn_count)

# percentage parried K. Schmeichel
df_parried_dnk = 100 - (df_isgoal_svn_count / df_ontarget_svn_count * 100)
#print(df_parried_dnk)

# percentage parried J. Oblak
df_parried_svn = 100 - (df_isgoal_dnk_count / df_ontarget_dnk_count * 100)
#print(df_parried_svn)

# Goal zone Shots on target Denmark  GC
gc_dnk = df_ontarget_dnk[df_ontarget_dnk['shot.goalZone'] == 'gc'].shape[0]
print(gc_dnk)
# Goal zone Shots on target Slovenia  GC
gc_svn = df_ontarget_svn[df_ontarget_svn['shot.goalZone'] == 'gc'].shape[0]
print(gc_svn)

# Goal zone Shots on target Denmark  GR
gr_dnk = df_ontarget_dnk[df_ontarget_dnk['shot.goalZone'] == 'gr'].shape[0]
print(gr_dnk)
# Goal zone Shots on target Slovenia  GR
gr_svn = df_ontarget_svn[df_ontarget_svn['shot.goalZone'] == 'gr'].shape[0]
print(gr_svn)

# Goal zone Shots on target Denmark  GB
gb_dnk = df_ontarget_dnk[df_ontarget_dnk['shot.goalZone'] == 'gb'].shape[0]
print(gb_dnk)
# Goal zone Shots on target Slovenia  GB
gb_svn = df_ontarget_svn[df_ontarget_svn['shot.goalZone'] == 'gb'].shape[0]
print(gb_svn)

# Goal zone Shots on target Denmark  GBR
gbr_dnk = df_ontarget_dnk[df_ontarget_dnk['shot.goalZone'] == 'gbr'].shape[0]
print(gbr_dnk)
# Goal zone Shots on target Slovenia  GBR
gbr_svn = df_ontarget_svn[df_ontarget_svn['shot.goalZone'] == 'gbr'].shape[0]
print(gbr_svn)

# Goal zone Shots on target Denmark  GTR
gtr_dnk = df_ontarget_dnk[df_ontarget_dnk['shot.goalZone'] == 'gtr'].shape[0]
print(gtr_dnk)
# Goal zone Shots on target Slovenia  GTR
gtr_svn = df_ontarget_svn[(df_ontarget_svn['shot.goalZone'] == 'gtr') & (df_ontarget_svn['type.primary'] == 'free_kick')].shape[0]
print("Shot on target was freekick?")
print(gtr_svn)

# Goal zone Shots on target Denmark  GL
gl_dnk = df_ontarget_dnk[df_ontarget_dnk['shot.goalZone'] == 'gl'].shape[0]
print(gl_dnk)
# Goal zone Shots on target Slovenia  GL
gl_svn = df_ontarget_svn[df_ontarget_svn['shot.goalZone'] == 'gl'].shape[0]
print(gl_svn)

# Create Plots
# ------------------------------------------------------------------
dnk_data = {'Shots on Target': df_ontarget_dnk_count,
            'Shot goal zone: GC': gc_dnk,
            'Shot goal zone: GR': gr_dnk,
            'Shot goal zone: GB': gb_dnk,
            'Shot goal zone: GBR': gbr_dnk,
            'Shot goal zone: GTR': gtr_dnk,
            'Shot goal zone: GL': gl_dnk,
            'Shot is Goal': df_isgoal_dnk_count,
            '% Parried by Opp. GK': df_parried_svn,
            }
svn_data = {'Shots on Target': df_ontarget_svn_count,
            'Shot goal zone: GC': gc_svn,
            'Shot goal zone: GR': gr_svn,
            'Shot goal zone: GB': gb_svn,
            'Shot goal zone: GBR': gbr_svn,
            'Shot goal zone: GTR': gtr_svn,
            'Shot goal zone: GL': gl_svn,
            'Shot is Goal': df_isgoal_svn_count,
            '% Parried by Opp. GK': df_parried_dnk,
            }

perc_categories = []

plot_stats_barchart(svn_data, dnk_data, team1_name='Slovenia', team2_name='Denmark', perc_categories=perc_categories, title='EM Qualifier: 2023-11-20 (2:1)',
                    subtitle='Shots Parried by Goalkeeper', team1_color='blue', team2_color='red',saveplt=True, savepath='C:/Users/loris/Documents/ETH Zürich/Master/Soccer Analytics/Shots_parried.png')

```
</details>

#### 4.4.2 Passes played per goalkeeper

Like mentioned above the goalkeeper is a main part of the defense. With the ability to really take part in the game and create possible pass stations the goalkeeper can be the one additional man in the defense line. It is possible to make changes of side or also launch a quick attack with a long shot of the goalkeeper.
In the following chart it can be seen that K. Schmeichel had a total of 24 passes. He was often used to calm down the defense and waiting for the right time to launch an attack. Furthermore with a total of 10 high and long passes K. Schmeichel made some passes near and over the own pitch half to start an attack.
J. Oblak had a total of 18 passes and only 5 high and long passes. This reflects that Slovenia had its main focus on defending and was not often able to get out of their half.

![goalkeeper_passes](uploads/baf88f90598db23ecdba2e0cad5f1417/goalkeeper_passes.png)

<details>
<summary> code</summary>

```python
# The import part is the same as in Section 4.3

# Passes from Denmark Goalkeeper K. Schmeichel
passes_goalkeeper_dnk = df_events[(df_events['type.primary'] == 'pass') & (df_events['player.name'] == 'K. Schmeichel')].shape[0]
print(passes_goalkeeper_dnk)
long_high_passes_goalkeeper_dnk = df_events[(df_events['type.primary'] == 'pass') & (df_events['player.name'] == 'K. Schmeichel') & (df_events['pass.length'] >= 40) & (df_events['pass.height'] == 'high')].shape[0]
print(long_high_passes_goalkeeper_dnk)

# Passes from Slovenian Goalkeeper J. Oblak
passes_goalkeeper_svn = df_events[(df_events['type.primary'] == 'pass') & (df_events['player.name'] == 'J. Oblak')].shape[0]
print(passes_goalkeeper_svn)
long_high_passes_goalkeeper_svn = df_events[(df_events['type.primary'] == 'pass') & (df_events['player.name'] == 'J. Oblak') & (df_events['pass.length'] >= 40) & (df_events['pass.height'] == 'high')].shape[0]
print(long_high_passes_goalkeeper_svn)


# Plot Data
# 1 Prepare Data
# Create dataframe for goalkeeper name and passes played
df_passes_gk = pd.DataFrame(columns=['name', 'passes'])

# Assign names
df_passes_gk.at[0, 'name'] = 'K. Schmeichel passes'
df_passes_gk.at[1, 'name'] = 'K. Schmeichel high/long passes'
df_passes_gk.at[2, 'name'] = 'J. Oblak passes'
df_passes_gk.at[3, 'name'] = 'J. Oblak high/long passes'

# Assign calculated passes
df_passes_gk.at[0, 'passes'] = passes_goalkeeper_dnk
df_passes_gk.at[1, 'passes'] = long_high_passes_goalkeeper_dnk
df_passes_gk.at[2, 'passes'] = passes_goalkeeper_svn
df_passes_gk.at[3, 'passes'] = long_high_passes_goalkeeper_svn

# 2 Plot Data
# Set Seaborn theme and color palette
sns.set_theme(style="darkgrid")
# palette = sns.color_palette("viridis", len(df_passes_gk))
palette = sns.color_palette("viridis", len(aligned_counts_svn))

# Plotting the data using Seaborn and Matplotlib
plt.figure(figsize=(10, 6))

# Plot percentage of duels won per player
sns.barplot(x='name', y='passes', data=df_passes_gk, color=palette[10])

ax = sns.barplot(x='name', y='passes', data=df_passes_gk, color=palette[10])
# Adding labels and title
plt.xlabel('Goalkeeper')
plt.ylabel('Number of Passes')
plt.title('Total Passes per Goalkeepers')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Customize x-axis labels
ax.set_xticklabels(['K. Schmeichel\nPasses', 'K. Schmeichel\nHigh/long passes', 'J. Oblak\nPasses', 'J. Oblak\nHigh/long passes'])

# Save plot to a specified path
save_path = 'C:/Users/loris/Documents/ETH Zürich/Master/Soccer Analytics/goalkeeper_passes_final.png'  # Specify your desired save path here
plt.tight_layout()
plt.savefig(save_path)

# Show plot
plt.show()

```
</details>


## 5. Set plays

### 5.1 Corners

This section analyzes the corners of the match between Denmark and Slovenia on 17.11.2023 and their impact on the game. Corners are a very important part of the game of football as they can often lead to scoring opportunities for the attacking team, but also to counter-attacking opportunities for the defending team. As can be seen from the following graph of corner events, Denmark was the more dominant team, with regards to corners.

![corner_statistics](uploads/ea0c3cce26886caefb3f02849a219339/corner_statistics.png)

In total, Denmark received 8 corners and Slovenia only 2. With 8 corners in a match, we can take a closer look at Denmark's offensive tactics and Slovenia's defensive tactics. The statistics of the corners show that 3 of the corners resulted in a shot, 2 of which were on target and 1 was a goal.

If we take a look at the map of the Danes' pass receiver position, we can see more details of their offensive tactics.

![corner_recipient_loc_DEN](uploads/acc2d2fb1bc633cc68d582252454a112/corner_recipient_loc_DEN.png)

87.5% of their corners found their target in the middle of the penalty area, while 12.5% were hit far behind the penalty area.

A look at the map of shots after corners shows what happened at the dangerous corners.

![Denmark_shots_corners_map](uploads/991497378c8da09751e25d593d0e6d43/Denmark_shots_corners_map.png)

It is possible to see the shooting positions of the 3 shots after the corners. From this map you can conclude that Denmark is pretty good at generating shooting opportunities after corners if these are whipped into the center of the penalty area. You can also see that Slovenia had trouble defending M. Jensen in aerial duels, as he is their main shot creator from corners with two shots and one goal.

The same analysis can be done for Slovenia as an attacking team. As we can see from the statistics of corner kicks, 1 of the 2 corners resulted in a shot that was not on target.

![corner_recipient_loc_SVN](uploads/e5f63c2932336cc2dc3eee0ce2899d70/corner_recipient_loc_SVN.png)

As Slovenia only had two corner kicks, they could not try multiple corner kick tactics, and as can be seen from the corner kick recipient locations map, all of their corner kick targets were inside the penalty area.

We can get more information from the shots after corner for Slovenia map.

![Slovenia_shots_corners_map](uploads/157bdc7c2df9a1e1cc81d41e02e37c7d/Slovenia_shots_corners_map.png)

We see that one of the corners, which was originally targeted at the center of the penalty area, was deflected and immediately taken by M. Zajc as a shot, but not on target and therefore not particularly dangerous.

After corners, there is often an opportunity to launch a counter-attack if they are defended properly. Therefore, we looked at the consecutive counter-attacks after corners for this game, but in this case there were none, as the advanced statistics of corner events show.

![corner_statistics_with_ca](uploads/d56bf9ef1cf640852c5e9cef5265388c/corner_statistics_with_ca.png)

<details>
<summary> code</summary>

##### Corner events

```python
# Corner events
df_corners = df_events[df_events['type.primary']=='corner']

# Corner for Slovenia
df_corners_svn = df_corners[df_corners["team.name"] == "Slovenia"]
corners_svn = df_corners_svn.shape[0]

# Coorner for Opponent
df_corners_opp = df_corners[df_corners["opponentTeam.name"] == "Slovenia"]
corners_opp = df_corners_opp.shape[0]

# Amount of corner events that ended with a shot for Slovenia
shots_svn = (df_corners_svn['possession.attack.withShot'] == True).sum()
shots_on_goal_svn = (df_corners_svn['possession.attack.withShotOnGoal'] == True).sum()
goals_scored_svn = (df_corners_svn['possession.attack.withGoal'] == True).sum()
xgoal_svn = df_corners_svn[~df_corners_svn['possession.attack.xg'].isnull()]['possession.attack.xg'].sum().round(2)

# Amount of corner events that ended with a shot for Denmark
shots_opp = (df_corners_opp['possession.attack.withShot'] == True).sum()
shots_on_goal_opp = (df_corners_opp['possession.attack.withShotOnGoal'] == True).sum()
goals_scored_opp = (df_corners_opp['possession.attack.withGoal'] == True).sum()
xgoal_opp = df_corners_opp[~df_corners_opp['possession.attack.xg'].isnull()]['possession.attack.xg'].sum().round(2)

# Create barchart for corner overview
svn_data = {'Corners': corners_svn,
            'Shots': shots_svn,
            'Shots on Target': shots_on_goal_svn,
            'Goals': goals_scored_svn,
            'Expected Goals': xgoal_svn,
            }

opp_data = {'Corners': corners_opp,
            'Shots': shots_opp,
            'Shots on Target': shots_on_goal_opp,
            'Goals': goals_scored_opp,
            'Expected Goals': xgoal_opp,
            }

# if category % do not normalize
perc_categories = []

# Show and save the plot
plot_stats_barchart(svn_data, opp_data, team1_name='Slovenia', team2_name='Denmark', perc_categories=perc_categories, title='EM Qualifier: 2023-11-17', subtitle='Corner events', team1_color='blue', team2_color='red', saveplt=True, savepath='plots/5-SetPieces/5_1-Corners/corner_statistics.png')
```

##### Shot map

```python
# Plot shot position and success on football field for Slowenia
df_shots_svn = df_corners_svn[df_corners_svn['possession.attack.withShot'] == True]

# Create Pitch with certain attributes
pitch = Pitch(pitch_length=pitch_length, pitch_width=pitch_width, pitch_color='grass', line_color='white', stripe=True)
fig, ax = pitch.draw()

# Draw every shot and colour it regarding its success
for i, shot in df_shots_svn.iterrows():

    # Position of shot
    [x, y] = shot[['possession.endLocation.x', 'possession.endLocation.y']].to_list()

    teamname = shot['team.name']

    # Color of shot depends on if it was off/on target or goal
    if shot['possession.attack.withGoal'] is True:
        color = "green"

    elif shot['possession.attack.withShotOnGoal'] is True:
        color = "orange"

    else:
        color = "red"

    shotCircle = plt.Circle((x/100.0 * pitch_length, y/100.0 * pitch_width), 2, color=color)

    plt.text(x/100.0 * pitch_length-4, y/100.0 * pitch_width - 4, shot['player.name'])

    ax.add_patch(shotCircle)

# Define the legend labels and corresponding colors
legend_labels = ['Goal', 'On Target', 'Off Target']
legend_colors = ['green', 'orange', 'red']

# Create proxy artists for legend
legend_patches = [Patch(color=color, label=label) for color, label in zip(legend_colors, legend_labels)]

# Add legend to the plot
plt.legend(handles=legend_patches, loc='lower right')

# Create title and save plot
fig.suptitle(f"Shots after Corner for {teamname}", fontsize = 12)
plt.savefig(f"plots/5-SetPieces/5_1-Corners/{teamname}_shots_corners_map.png", dpi=400)
plt.show()
```

##### Recipients location map

```python
# Create Dataframe for the distribution of corner passes for Slowenia
df_distribution = pd.DataFrame()

# Determine pass types based on recipient location
pass_short = ((df_corners_svn["pass.endLocation.y"] < 19.0) & (df_corners_svn["location.y"] == 0.0)) | \
             ((df_corners_svn["pass.endLocation.y"] > 81.0) & (df_corners_svn["location.y"] == 100.0))
pass_parea = (df_corners_svn["pass.endLocation.y"] >= 19.0) & (df_corners_svn["pass.endLocation.y"] <= 81.0)
pass_long  = ((df_corners_svn["pass.endLocation.y"] < 19.0) & (df_corners_svn["location.y"] == 100.0)) | \
             ((df_corners_svn["pass.endLocation.y"] > 81.0) & (df_corners_svn["location.y"] == 0.0))
pass_wide  = (df_corners_svn["pass.endLocation.x"] >= 16.0) & (df_corners_svn["pass.endLocation.x"] <= 84.0)

# For every Corner type safe statistics for plotting
for i, pass_dst in enumerate([pass_short, pass_parea, pass_long, pass_wide]):

    if df_corners_svn.loc[pass_dst].empty:
        df_distribution.at[i, "x"] = -1.0
        df_distribution.at[i, "y"] = -1.0
        df_distribution.at[i, "amount"] = -1.0
        continue

    df_distribution.at[i, "x"] = np.mean(df_corners_svn.loc[pass_dst]['pass.endLocation.x'].to_numpy()).round(1)
    df_distribution.at[i, "y"] = np.mean(df_corners_svn.loc[pass_dst]['pass.endLocation.y'].to_numpy()).round(1)
    df_distribution.at[i, "amount"] = df_corners_svn.loc[pass_dst]['pass.endLocation.x'].count()

# Adjust circle sizes and transparency proportional to the number of passes received in a specific area
df_distribution['marker_size'] = (df_distribution['amount'] / df_distribution['amount'].max() * 1500)
df_distribution['marker_size'] = abs((df_distribution['marker_size'] > 0) * df_distribution['marker_size']).round(0)
df_distribution['alpha'] = abs(df_distribution['marker_size'] / df_distribution['marker_size'].max()).round(2)
df_distribution['percentage'] = abs(df_distribution['amount'] / df_distribution[df_distribution['amount'] > 0]['amount'].sum() * (df_distribution['amount'] > 0)) * 100

# Create pitch with certain attributes
pitch = Pitch(pitch_color='grass', line_color='white', stripe=True)
fig, ax = pitch.draw()

# Draw circles proportional to the number of passes received in specific areas
pitch.scatter(df_distribution.x / 100. * pitch_length, df_distribution.y / 100. * pitch_width, s=df_distribution.marker_size, \
              color='cornflowerblue', edgecolors='mediumblue', linewidth=2, alpha=df_distribution.alpha.apply(lambda x: max(x, 0.75)), ax=ax, zorder = 3)

# Annotate circles with percentage of total passes
for i in range(4):

        x = df_distribution.at[i, "x"]
        if x == -1.0:
                continue

        x = x/100. * pitch_length
        y = df_distribution.at[i, "y"]/100. * pitch_width

        pitch.annotate(f"{df_distribution.at[i, 'percentage']}%", xy=(x, y), c='white', va='center',
                   ha='center', size=8, weight = "bold", ax=ax, zorder = 4)

# Create title and save plot
team_name = df_corners_svn["team.name"].iloc[0]
fig.suptitle(f"Corner pass recipient location percentage for {team_name}", fontsize = 12)
plt.savefig('plots/5-SetPieces/5_1-Corners/corner_recipient_loc_SVN.png', dpi=400)
plt.show()

```
</details>

### 5.2 Penalties

There were no penalties in the match between Denmark and Slovenia on 17.11.2023, which is why this section is not covered in the first draft.

<details>
<summary> code</summary>

</details>

### 5.3 Free kicks

This section analyzes the free kicks of the match between Denmark and Slovenia on 17.11.2023 and their impact on the game. Free kicks, especially the closer they get to the goal, are a very important part of the game.

If you look at the Slovenia free-kick map, you can see 4 different types of free-kicks. First, the goal kick, which we defined as a free kick inside your own penalty area. Secondly, the shot, which is a free kick that is taken directly as a shot on goal, regardless of whether it is on target or not. Thirdly, the cross, which is a free kick that is used to directly create a promising attacking opportunity by hitting the ball into the penalty area, but is not taken as a shot. And the "Else" category, which serves as a catch-all for all other types of free kicks.

![Slovenia_freekick_map](uploads/36588b8d1c739c77db3adafc09e9cc3d/Slovenia_freekick_map.png)

From Slovenia's free-kick map, it can be deduced that Slovenia were pushed back deep into their own half by Denmark's pressing and were sometimes able to get a free-kick out of it. Slovenia also had a direct free-kick from E. Janza, which he was able to convert into a goal. As they are 1 for 1 in goals scored from free kicks, they appear to be very dangerous in this area of the game.

![Denmark_freekick_map](uploads/f59e996fe396b12027c53bf668ab0c63/Denmark_freekick_map.png)

Denmark's free-kick map shows that the Danes were often stopped by fouls in the build-up to their attacking play, as their free kicks are usually taken at the end of the second third of the pitch. Slovenia also managed to avoid free kicks near their own goal, meaning that Denmark only had one opportunity for an attacking free kick.

It is also possible to see when teams consider the distance to goal suitable for an attacking free kick such as a shot or a cross.

![avg_distance_freekick_slov](uploads/912d9baf2bdba9484f6c3781a1ebb1a4/avg_distance_freekick_slov.png)

With Slovenia, we see that most of the free kicks were around 80 meters, so neither suitable for a cross nor for a direct shot. But as soon as they were closer than 30 meters, they shot directly and were quite efficient in this game. Since they didn't have an offensive free kick cross, we can't say much about that.

![avg_distance_freekick_den](uploads/a84702827a54b3dc3cf573f59260b869/avg_distance_freekick_den.png)

With Denmark, we see that most of the free kicks were taken around the 70m mark, so they are not suitable for either a cross or a direct shot, but this suggests that they were a bit more offensive than the Slovenians. When they get closer to goal, around the 40-meter mark, they start using the free kicks as crosses. Since they didn't have a direct free kick shot, we can't say much about that.

To see which players shoot free kicks most often, we have listed all players in a diagram.

![freekick_takers_slov](uploads/2387a36bb0e4dae0f0df78039217588f/freekick_takers_slov.png)

With Slovenia, you can see that they had a lot of goal kicks and free kicks which defenders like Bijol took, indicating that they were constantly under pressure and in risky situations in their own half around the penalty area.

![freekick_takers_den](uploads/2c52c831c4fb27a3eefe4665bae9b173/freekick_takers_den.png)

Denmark's most prominent free kick taker is midfielder P. Hojberg. This suggests that they have been fouled mainly in the build-up to their attacking play.

To summarize, Slovenia doesn't seem to get many dangerous free-kicks, but when they do, they are very dangerous. Slovenia seems to try to disrupt the Danish build-up play by fouling the Danes in midfield in the Slovenian half, but not in the attacking positions around the penalty area. Denmark could exploit this by playing more 1-v-1 situations as Slovenia seems to defend passively and does not try to risk a free kick near the goal.

<details>
<summary> code</summary>

##### Free kick average distance

```python
# Free kick events for Slowenia
df_freekicks = df_events[(df_events['type.primary'] == 'free_kick') & (df_events['team.name'] == 'Slovenia')]

# Classify free kicks as shot, cross, goalkick or else
df_freekick_shots = df_freekicks[df_freekicks['type.secondary'].str.contains("shot")]
df_freekick_cross = df_freekicks[df_freekicks['type.secondary'].str.contains("cross")]
df_goalkick = df_freekicks[(df_freekicks['location.x'] <= 16.0) & ((df_freekicks['location.y'] <= 81.0) & (df_freekicks['location.y'] >= 19.0))]
df_freekick_else = df_freekicks[~df_freekicks['type.secondary'].str.contains("cross") & ~df_freekicks['type.secondary'].str.contains("shot") & ~((df_freekicks['location.x'] <= 16.0) & ((df_freekicks['location.y'] <= 81.0) & (df_freekicks['location.y'] >= 19.0)))]

# Calculate averages
avg_distance_shots = np.mean(np.sqrt(((100 - df_freekick_shots['location.x'])/100. * pitch_length)**2 + ((50 - df_freekick_shots['location.y'])/100. * pitch_width)**2))
avg_distance_cross = np.mean(np.sqrt(((100 - df_freekick_cross['location.x'])/100. * pitch_length)**2 + ((50 - df_freekick_cross['location.y'])/100. * pitch_width)**2))
avg_distance_else = np.mean(np.sqrt(((100 - df_freekick_else['location.x'])/100. * pitch_length)**2 + ((50 - df_freekick_else['location.y'])/100. * pitch_width)**2))

# Create Dataframe for the average distances of types of free kicks for Slowenia
df_distance = pd.DataFrame(columns=['type', 'average_distance'])

# Assign calculated averages
df_distance.at[0, 'type'] = 'shot'
df_distance.at[1, 'type'] = 'cross'
df_distance.at[2, 'type'] = 'else'

df_distance.at[0, 'average_distance'] = avg_distance_shots
df_distance.at[1, 'average_distance'] = avg_distance_cross
df_distance.at[2, 'average_distance'] = avg_distance_else

# Apply a Seaborn theme
sns.set_theme(style="darkgrid")

# Choose a color palette for the plot
palette = sns.color_palette("viridis", len(df_distance))

# Create the bar chart with the chosen palette
sns.barplot(x='type', y='average_distance', data=df_distance, palette=palette)

# Set the title of the plot
plt.title('Average Distance for Freekick Types')

# Customize further with Seaborn and Matplotlib
plt.xlabel('Free kick Type') # X-axis label
plt.ylabel('Average Distance [m]')    # Y-axis label

# Show and save the plot
plt.savefig('plots/5-SetPieces/5_3-FreeKicks/avg_distance_freekick_slov.png', dpi=400)
plt.show()

```

##### Free kick takers

```python
# Create Dataframe that holds average distance of the different freekick types
df_fk_amount = pd.DataFrame(columns=['name', 'amount'])
for i, name in enumerate(df_freekicks["player.name"].unique()):

    if isinstance(name, float) and np.isnan(name):
        continue

    df_fk_amount.at[i, "name"] = name

    # Calculate number of passes
    df_fk_amount.at[i, "amount"] = df_freekicks.loc[df_freekicks["player.name"] == name].count().iloc[0]

# Apply a Seaborn theme
sns.set_theme(style="darkgrid")

# Choose a color palette for the plot
palette = sns.color_palette("viridis", len(df_fk_amount))

# Create the bar chart with the chosen palette
sns.barplot(x='name', y='amount', data=df_fk_amount, palette=palette)

# Set the title of the plot
plt.title('Amount of free kicks taken by indiviual players')

# Customize further with Seaborn and Matplotlib
plt.xlabel('Player Name') # X-axis label
plt.ylabel('Amount of Free kicks')    # Y-axis label

# Show and save the plot
plt.savefig('plots/5-SetPieces/5_3-FreeKicks/freekick_takers_slov.png', dpi=400)
plt.show()
```

##### Free kick location map

```python
# Create pitch with certain attributes
pitch = Pitch(pitch_length=pitch_length, pitch_width=pitch_width, pitch_color='grass', line_color='white', stripe=True)
fig, ax = pitch.draw()

# Define the legend and pitch circle colors
colors=['red', 'orange', 'yellow', 'green']

# Draw circles on basis of free kick types
for idx, dataset in enumerate([df_freekick_shots, df_freekick_cross, df_freekick_else, df_goalkick]):
    color = colors[idx]
    for i, freekick in dataset.iterrows():

        if isinstance(freekick['player.name'], float) and np.isnan(freekick['player.name']):
            continue

        # Position of free kick
        [x, y] = freekick[['location.x', 'location.y']].to_list()

        shotCircle = plt.Circle((x/100.0 * pitch_length, y/100.0 * pitch_width), 2, color=color)

        plt.text(x/100.0 * pitch_length-4, y/100.0 * pitch_width - 4, freekick['player.name'])

        ax.add_patch(shotCircle)

# Define the legend labels
legend_labels = ['Shot', 'Cross', 'Else', 'Goal Kick']

# Create proxy artists for legend
legend_patches = [Patch(color=color, label=label) for color, label in zip(colors, legend_labels)]

# Add legend to the plot
plt.legend(handles=legend_patches, loc='lower right')

# Create title and save plot
fig.suptitle(f"Free kicks for Slovenia", fontsize = 12)
plt.savefig(f"plots/5-SetPieces/5_3-FreeKicks/Slovenia_freekick_map.png", dpi=400)
plt.show()
```

</details>

## 6 Physical data

Based on the provided data, the most dangerous players can be identified across different metrics. These players have a diverse set of skills, combining endurance, speed, and agility, which can pose significant challenges for opposing teams. They have the most dangerous from a physical perspective.

**Adam Gnezda Čerin**: He stands out for his overall distance covered, running distance, and high-speed running distance. His combination of endurance and speed makes him a formidable presence on the field.

**Benjamin Verbič**: Not only does Verbič excel in running and high-speed running distances, but he also demonstrates significant sprinting ability. His capability to cover ground quickly and maintain high speeds makes him a threat to opponents, particularly in quick transitions and counterattacks.

**Benjamin Šeško**: While not leading in total distance covered, Šeško shines in sprinting distance and max speed. His explosive acceleration and top speed make him a dangerous forward, capable of breaking through defenses and creating scoring opportunities.

#### Overall values
| Player name | Distance | Running Distance | HSR Distance | Sprinting Distance | Accelerations | Max speed |
|:---------------------|-----------:|-------------------:|---------------:|---------------------:|----------------:|------------:|
| Adam Gnezda Čerin | 12318 | 2323 | 675 | 118 | 5 | 27.2 |
| Benjamin Verbič | 8654 | 1350 | 564 | 156 | 11 | 27.5 |
| Benjamin Šeško | 9439 | 1226 | 462 | 228 | 11 | 31.1 |
| Erik Janža | 6943 | 833 | 363 | 115 | 8 | 28.1 |
| Jaka Bijol | 9688 | 1061 | 355 | 57 | 6 | 27.1 |
| Jan Mlakar | 10772 | 1675 | 590 | 81 | 5 | 26.9 |
| Jasmin Kurtič | 4454 | 922 | 117 | 0 | 2 | 22.9 |
| Jon Gorenc- tankovič | 2986 | 546 | 185 | 12 | 2 | 24.6 |
| Miha Blažič | 10579 | 1368 | 333 | 67 | 5 | 25.9 |
| Miha Zajc | 1266 | 223 | 90 | 6 | 0 | 25.2 |
| Sandi Lovrič | 2926 | 498 | 153 | 52 | 2 | 29.6 |
| Timi Max Elšnik | 7857 | 1185 | 367 | 27 | 3 | 25.3 |
| Vanja Drkušić | 3954 | 597 | 264 | 101 | 0 | 29.4 |
| Žan Karničnik | 11470 | 1751 | 501 | 129 | 7 | 28.4 |
| Žan Vipotnik | 10364 | 1195 | 490 | 149 | 13 | 29.2 |


In examining the top three players across each specific physical aspect, we gain a better insight into the diverse skill sets present in Slovenia:

#### Top 3 Distance
| Player name | Distance | Running Distance | HSR Distance | Sprinting Distance | Accelerations | Max speed |
|:------------------|-----------:|-------------------:|---------------:|---------------------:|----------------:|------------:|
| Adam Gnezda Čerin | 12318 | 2323 | 675 | 118 | 5 | 27.2 |
| Žan Karničnik | 11470 | 1751 | 501 | 129 | 7 | 28.4 |
| Jan Mlakar | 10772 | 1675 | 590 | 81 | 5 | 26.9 |
#### Top 3 Running Distance
| Player name | Distance | Running Distance | HSR Distance | Sprinting Distance | Accelerations | Max speed |
|:------------------|-----------:|-------------------:|---------------:|---------------------:|----------------:|------------:|
| Adam Gnezda Čerin | 12318 | 2323 | 675 | 118 | 5 | 27.2 |
| Žan Karničnik | 11470 | 1751 | 501 | 129 | 7 | 28.4 |
| Jan Mlakar | 10772 | 1675 | 590 | 81 | 5 | 26.9 |
#### Top 3 HSR Distance
| Player name | Distance | Running Distance | HSR Distance | Sprinting Distance | Accelerations | Max speed |
|:------------------|-----------:|-------------------:|---------------:|---------------------:|----------------:|------------:|
| Adam Gnezda Čerin | 12318 | 2323 | 675 | 118 | 5 | 27.2 |
| Jan Mlakar | 10772 | 1675 | 590 | 81 | 5 | 26.9 |
| Benjamin Verbič | 8654 | 1350 | 564 | 156 | 11 | 27.5 |
#### Top 3 Sprinting Distance
| Player name | Distance | Running Distance | HSR Distance | Sprinting Distance | Accelerations | Max speed |
|:----------------|-----------:|-------------------:|---------------:|---------------------:|----------------:|------------:|
| Benjamin Šeško | 9439 | 1226 | 462 | 228 | 11 | 31.1 |
| Benjamin Verbič | 8654 | 1350 | 564 | 156 | 11 | 27.5 |
| Žan Vipotnik | 10364 | 1195 | 490 | 149 | 13 | 29.2 |
#### Top 3 Accelerations
| Player name | Distance | Running Distance | HSR Distance | Sprinting Distance | Accelerations | Max speed |
|:----------------|-----------:|-------------------:|---------------:|---------------------:|----------------:|------------:|
| Žan Vipotnik | 10364 | 1195 | 490 | 149 | 13 | 29.2 |
| Benjamin Verbič | 8654 | 1350 | 564 | 156 | 11 | 27.5 |
| Benjamin Šeško | 9439 | 1226 | 462 | 228 | 11 | 31.1 |
#### Top 3 Max speed
| Player name | Distance | Running Distance | HSR Distance | Sprinting Distance | Accelerations | Max speed |
|:---------------|-----------:|-------------------:|---------------:|---------------------:|----------------:|------------:|
| Benjamin Šeško | 9439 | 1226 | 462 | 228 | 11 | 31.1 |
| Sandi Lovrič | 2926 | 498 | 153 | 52 | 2 | 29.6 |
| Vanja Drkušić | 3954 | 597 | 264 | 101 | 0 | 29.4 |

<details>
<summary> code</summary>

```python
# Load data
metadata_df = pd.read_csv(data_dir / f"{match_id}_metadata.csv")
play_direction_df = pd.read_csv(data_dir / f"{match_id}_play_direction.csv")
phase_df = pd.read_csv(data_dir / f"{match_id}_phase.csv")
lineup_df = pd.read_csv(data_dir / f"{match_id}_lineup.csv")
tracking_df = pd.read_csv(data_dir / f"{match_id}_tracking.csv")
visible_area_df = pd.read_csv(data_dir / f"{match_id}_visible_area.csv")
physical_df = pd.read_csv(data_dir / f"{match_id}_physical.csv")
passes_df = pd.read_csv(data_dir / f"{match_id}_passes.csv")
on_ball_pressures_df = pd.read_csv(data_dir / f"{match_id}_on_ball_pressures.csv")
off_ball_runs_df = pd.read_csv(data_dir / f"{match_id}_off_ball_runs.csv")
max_ball_z = int(tracking_df.z.max())

# Skillcorner
physical_data = physical_df[['player_name','player_id', 'Distance','Running Distance', 'HSR Distance', 'Sprinting Distance','Count High Acceleration','PSV-99']]

# Rename some columns
physical_data = physical_data.rename(columns={
"player_name": "Player name",
"Count High Acceleration": "Accelerations",
"PSV-99": "Max speed"
})

# Exclude danish team
valid_players = np.array(lineup_df[lineup_df['team_name'] != "Denmark"]['player_id'])

# Sort by values
physical_data = physical_data.sort_values(by="Player name")
physical_data = physical_data[physical_data['player_id'].isin(valid_players)].drop(columns=['player_id'])

# Print players
print(physical_data.to_markdown(index=False))

# Print top 3 each time
for val in physical_data.keys():
    print(f'#### Top 3 {val}')
    print(physical_data.sort_values(by=val, ascending=False).head(3).to_markdown(index=False))
```

</details>

## 7 Goals


| Vs : Denmark | Vs : Portugal | Vs : Portugal |
|---|---|---|
|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/video1.mov?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/video2.mov?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/video3.mov?raw=true" align="center" height="350" width="600"/>|


| Vs : Usa | Vs : Khazakhtan | Vs : Khazakhtan |
|---|---|---|
|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/video4.mov?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/video5.mov?raw=true" align="center" height="350" width="600"/>|<img src="https://github.com/ngroggy/SoccerAnalytics/blob/main/video6.mov?raw=true" align="center" height="350" width="600"/>|

## 8 Fifa ranking, monetary values of the players

### 8.1 Fifa rating

![slovenia](uploads/6fcecaa356e75c1f10dc1366a7fed302/slovenia.png)

An examination of Slovenia's FIFA ratings over the past four years reveals a small progression. In the most recent year, Slovenia has risen from 64th to 56th place, indicating a correction towards their average rank. Based on their rating, it appears that Slovenia may not pose as formidable a challenge for strong opponents. For instance, we, Denmark,  holds the 22nd position, suggesting that from this standpoint, the match seems to be in our favor.

<details><summary>Sources</summary>

[Fifa ranking](https://inside.fifa.com/fifa-world-ranking/SVN?gender=men)

</details>

### 8.2 Transfer value

According to the website Transfermarkt, two players hold considerable value for the Slovenian team: Jan Oblak and Benjamin Šeško. 

![jan](uploads/69bb2799d97161bafdcf0dcd62333274/jan.png)

Jan Oblak, valued at 30€ million, is a standout goalkeeper renowned for his exceptional shot-stopping abilities and commanding presence in the penalty area. He is widely considered one of the best goalkeepers in the world and provides Slovenia with a solid defensive foundation.

![benjamin](uploads/fc16fc1998851a63d4c4f08654281cf5/benjamin.png)

Benjamin Šeško, valued at 40€ million, is a promising young talent known for his prowess as a forward. Despite his relatively young age, Šeško has shown great potential with his goal-scoring ability and versatility on the field.

Given their significant value and potential impact on the team, Jan Oblak and Benjamin Šeško are expected to be two players to watch closely during Slovenia's matches.

<details><summary>Sources</summary>

[Transfer Markt](https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop/mw/land_id/155)

</details>

#### Fifa 24 - the video game

In FIFA 24, the Slovenian national team boasts six players with ratings surpassing 75, indicating their proficiency within the virtual football game. Here's a summary of each player's strengths based on their analysis.

![fifa_game](uploads/cfc8a7fbaf14c417d101d142853f1b51/fifa_game.png)

1. **Jan Oblak (Goalkeeper):**
    Jan Oblak is a top goalie in FIFA 24. He's really good at stopping shots, controlling his area, and staying consistent. Oblak stops a lot of shots, which makes it hard for the other team to score.

2. **Kevin Kampl (Midfielder):**
    Kevin Kampl is a versatile midfielder in FIFA 24. He's good at passing, keeping possession, and defending. Kampl is smart on the field and knows where to be to help his team. He's good at starting attacks and stopping the other team's attacks.

3. **Jaka Bijol (Defender):**
Jaka Bijol is a strong defender in FIFA 24. He's solid in defense and good in the air. Bijol reads the game well and makes important tackles to stop the other team's attacks. He brings stability and reliability to Slovenia's defense.

4. **Sandi Lovrić (Midfielder):**
Sandi Lovrić is an important midfielder in FIFA 24. He's known for his skill and vision. Lovrić creates chances for his team with his smart passes and playmaking ability. He controls the pace of the game and helps his team attack effectively.

5. **Benjamin Šeško (Forward):**
    Benjamin Šeško is a young forward who's great at scoring goals in FIFA 24. Even though he's young, he's quick and skillful. He's good at getting past defenders and creating chances to score. Šeško's ability to find the goal and finish chances makes him a dangerous player.

6. **Miha Zajc (Midfielder):**
    Miha Zajc is another talented midfielder in FIFA 24. He's skilled with the ball and can score goals from midfield. Zajc adds creativity and energy to his team's midfield play. His ability to score goals from midfield positions makes him a threat to the other team.

These six players, each excelling in their respective positions, form the strongest part of the Slovenian team in FIFA 24 and are therefore players to watch.

<details><summary>Sources</summary>

[Fifa video game](https://www.ea.com/games/ea-sports-fc/ratings?gender=0&nationality=44)

</details>

## 9 Weaknesses & Tactic to adopt

### 9.1 General tactic

Slovenia typically adopts a balanced tactical approach, focusing on organized defending while looking to exploit counterattacking opportunities. They often maintain a compact defensive shape, with midfielders dropping deep to provide defensive cover and limit space for the opposition. Quick transitions from defense to attack, utilizing the pace and skill of players like Šeško, are a key aspect of Slovenia's gameplay.

### 9.2 Strengths

**Solid Defense**: Led by the commanding presence of Jan Oblak in goal, Slovenia boasts a resilient defense capable of frustrating opposing attackers and keeping clean sheets.

**Creative Midfield**: Josip Iličić's playmaking abilities combined with the technical skill of midfielders like Miha Zajc provide Slovenia with creativity and flair in midfield.

**Attacking Threat**: With Benjamin Šeško leading the frontline, Slovenia poses a potent attacking threat, capable of scoring goals in many situations.

### 9.3 Weaknesses

**Lack of Depth**: While Slovenia possesses quality in key positions, their squad depth may be a concern, especially in midfield and defensive areas.

**Vulnerability to High Pressure**: Slovenia's reliance on quick transitions leaves them susceptible to high-pressing opponents who disrupt their build-up play and force turnovers in dangerous areas.

**Inexperience in Key Areas**: Despite the presence of talented individuals, Slovenia may lack experience in high-pressure situations, particularly in international competitions, which could affect their decision-making and composure.



