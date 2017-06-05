from flask import Flask, render_template, abort, send_file, request
import postal
import os

app = Flask(__name__)
mail_client = postal.Client()

# The main episode data store
episodes = {
    'dave-burson-hotels-combined': {
        'title': 'Dave Burson, Hotels Combined',
        'soundcloud-url': 'https://soundcloud.com/intercom/daniel-burka-design-partner-at',
        'soundcloud': '296867798',
        'length': '28:28',
        'number': 1, 
        'url': 'dave-burson-hotels-combined'
    }, 
    'carlos-pacheco-escrow': {
        'title': 'Carlos Pacheco, Escrow.com',
        'soundcloud-url': 'https://soundcloud.com/intercom/amy-thibodeau-content-strategy',
        'soundcloud': '325557698',
        'length': '33:01',
        'number': 2,
        'url': 'carlos-pacheco-escrow'
    }
}


@app.route('/')
def index():
    # Change the 'latest' key to make the homepage show the latest episode
    return render_template('homepage.html', title="Home", episode='carlos-pacheco-escrow')


@app.route('/episodes')
def past_episodes():
    # TODO: sort the episodes into reverse order - currently they are "random"
    #       determined by the way python sorts its dictionary
    return render_template('past.html', title="Past Episodes")


@app.route('/episodes/<name>')
def view_episode(name):
    if name not in episodes:
        return abort(404)
    # if not os.path.isfile('templates/episodes/%s.html'):
    #     return abort(404)
    return render_template('episodes/%s.html' % name, episode=name, title=episodes[name]['title'])


@app.route('/sw.js')
def service_worker():
    return send_file('static/js/sw.js')


@app.route('/favicon.ico')
def favicon():
    return send_file('static/img/favicon.ico')


@app.context_processor
def inject_url():
    return dict(url=request.url_rule, episodes=episodes)

# TODO: Send email to welcome people to the list
# def send():
#     message = client.send_message(
#         subject='Hi there!',
#         from_address='James - The Prodcast <james@theprodcast.com.au>',
#         to_address=['james@cooperstanbury.com'],
#         html='templates/emails/welcome.html'
#     )
#     print message["data"]
#     return 'Thanks!'


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
