from flask import Flask, request, render_template_string
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
            return render_template_string(HTML_FORM, result=result_text, opponent_choice=opponent_choice.capitalize())
    else:
        return render_template_string(HTML_FORM, result=None, opponent_choice=None)

HTML_FORM = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rock Paper Scissors</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }
        .choices button {
            background: none;
            border: none;
            padding: 0;
            margin: 0;
            cursor: pointer;
            outline: none;
        }
        
        .choices img {
            width: 100px;
            height: auto;
            cursor: pointer;
            margin: 10px;
            border: 2px solid black;
            border-radius: 10px;
            transition: transform 0.2s;
        }
        .choices img:hover {
            transform: scale(1.2);
            border: 2px solid black;
        }
        .bold {
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Rock Paper Scissors Game</h1>
    <p>Choose your weapon!</p>
    <div class="choices">
        <form action="/" method="post">
            <button type="submit" name="choice" value="rock"><img src="{{ url_for('static', filename='images/rock.png') }}" alt="Rock"></button>
            <button type="submit" name="choice" value="paper"><img src="{{ url_for('static', filename='images/paper.png') }}" alt="Paper"></button>
            <button type="submit" name="choice" value="scissor"><img src="{{ url_for('static', filename='images/scissors.png') }}" alt="Scissor"></button>
        </form>
    </div>
    {% if result %}
    <p>Opponent's choice:  <span class="bold">{{ opponent_choice }} </span></p>
    <p>Result: <span class="bold">{{ result }}</span.</p>
    {% endif %}
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
