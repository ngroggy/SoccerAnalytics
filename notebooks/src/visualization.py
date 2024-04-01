import matplotlib.pyplot as plt
import numpy as np


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
                        team1_color='red', team2_color='blue'):
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
    plt.show()
