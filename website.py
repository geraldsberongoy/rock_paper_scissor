from flask import Flask, request, render_template
import random

app = Flask(__name__)

# Constants for game choices
CHOICES = ["paper", "rock", "scissor"]

def get_game_result(player_choice, opponent_choice):
    """Determine the game result based on player and opponent choices."""
    results = {
        "paper": {"paper": "Draw", "rock": "Win", "scissor": "Lose"},
        "rock": {"paper": "Lose", "rock": "Draw", "scissor": "Win"},
        "scissor": {"paper": "Win", "rock": "Lose", "scissor": "Draw"}
    }
    return results.get(player_choice, {}).get(opponent_choice, "Error. Invalid choice.")

@app.route("/", methods=["GET", "POST"])
def game():
    if request.method == "POST":
        # Randomly select the opponent's choice
        opponent_choice = random.choice(CHOICES)
        
        # Get the player's choice from the form submission and convert it to lowercase
        player_choice = request.form.get("choice", "").lower()

        # Get the game result based on the player's choice and opponent's choice
        result_text = get_game_result(player_choice, opponent_choice)
        
        # Render the template with the result and opponent's choice
        return render_template("index.html", result=result_text, opponent_choice=opponent_choice.capitalize())
    else:
        # Render the template for a GET request with no result
        return render_template("index.html", result=None, opponent_choice=None)

if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run(debug=True)