from flask import Flask, render_template, request

app = Flask(__name__)


comments = [
    {'id': 1, 'content': 'Комментарий 1', 'rating': 0},
    {'id': 2, 'content': 'Комментарий 2', 'rating': 0},
    {'id': 3, 'content': 'Комментарий 3', 'rating': 0}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        comment_id = int(request.form['comment_id'])
        rating_type = request.form['rating_type']

        for comment in comments:
            if comment['id'] == comment_id:
                if rating_type == 'like':
                    comment['rating'] += 1
                elif rating_type == 'dislike':
                    comment['rating'] -= 1
                break

    return render_template('index.html', comments=comments)

if __name__ == '__main__':
    app.run(debug=True)
