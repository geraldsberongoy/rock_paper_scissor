from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def game():
    if request.method == "POST":
        game_choices = ["paper", "rock", "scissor"]
        opponent_choice = random.choice(game_choices)
        player_choice = request.form.get("choice", "").lower()

        results = {
            "paper": {"paper": "Draw", "rock": "Win", "scissor": "Lose"},
            "rock": {"paper": "Lose", "rock": "Draw", "scissor": "Win"},
            "scissor": {"paper": "Win", "rock": "Lose", "scissor": "Draw"}
        }

        result_text = "Invalid choice. Please select rock, paper, or scissor."
        if player_choice in results:
            result_text = results[player_choice].get(opponent_choice, "Error. Choice between the three.")
            return render_template("index.html", result=result_text, opponent_choice=opponent_choice.capitalize())
    else:
        return render_template("index.html", result=None, opponent_choice=None)

if __name__ == "__main__":
    app.run(debug=True)