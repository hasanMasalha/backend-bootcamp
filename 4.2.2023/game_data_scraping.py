import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np

# Function to scrape game data from the Steam store
def scrape_steam_store(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        games = soup.find_all('a', {'class': 'search_result_row'})
        game_data = []

        for game in games:
            title = game.find('span', {'class': 'title'}).text.strip()
            genre = game.find('span', {'class': 'genre'}).text.strip()
            game_data.append({'title': title, 'genre': genre})

        return game_data

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

# Function to plot the most appeared tags
def plot_most_appeared_tags(game_data):
    genres = [game['genre'] for game in game_data]
    unique_genres, counts = np.unique(genres, return_counts=True)

    plt.bar(unique_genres, counts)
    plt.xlabel('Genres')
    plt.ylabel('Number of Games')
    plt.title('Most Appeared Genres on Steam')
    plt.xticks(rotation=45)
    plt.show()

# Function to calculate and print the percentage of a specific tag
def calculate_percentage(game_data, user_input_tag):
    total_games = len(game_data)
    games_with_tag = sum(1 for game in game_data if user_input_tag.lower() in game['genre'].lower())

    percentage = (games_with_tag / total_games) * 100
    print(f"The percentage of games with the tag '{user_input_tag}' is: {percentage:.2f}%")

# Main function
def main():
    steam_store_url = 'https://store.steampowered.com/search/?sort_by=Reviews_DESC'

    # Scrape game data from the Steam store
    game_data = scrape_steam_store(steam_store_url)

    if game_data:
        # Plot the most appeared tags
        plot_most_appeared_tags(game_data)

        # Get user input for a specific tag
        user_input_tag = input("Enter a genre tag: ")

        # Calculate and print the percentage of the user input tag
        calculate_percentage(game_data, user_input_tag)

        # Plot the user input tag with relevant statistics
        user_input_data = [game['genre'] for game in game_data if user_input_tag.lower() in game['genre'].lower()]
        user_input_counts = np.unique(user_input_data, return_counts=True)

        plt.bar(user_input_counts[0], user_input_counts[1])
        plt.xlabel(f'{user_input_tag.capitalize()} Games')
        plt.ylabel('Number of Games')
        plt.title(f'Statistics for {user_input_tag.capitalize()} Games on Steam')
        plt.xticks(rotation=45)
        plt.show()

if __name__ == "__main__":
    main()
