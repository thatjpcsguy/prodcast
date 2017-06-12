#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, abort, send_file, request, jsonify
import postal

import sqlite3
import os
import time

app = Flask(__name__)
mail_client = postal.Client()

from pages import episodes, articles, latest_episode, latest_article


@app.route('/')
def index():
    # Change the 'episode' key to make the homepage show the latest episode
    return render_template(
        'homepage.html', 
        title="Home", 
        episode=latest_episode, 
        article=latest_article
        )


@app.route('/episodes')
def past_episodes():
    # TODO: sort the episodes into reverse order - currently they are "random"
    #       determined by the way python sorts its dictionary
    return render_template(
        'episodes.html', 
        title="Past Episodes"
        )


@app.route('/episodes/<name>')
def view_episode(name):
    if name not in episodes:
        return abort(404)
    return render_template(
        'episodes/%s.html' % name, 
        episode=name, 
        title=episodes[name]['title']
        )


@app.route('/articles')
def past_articles():
    # TODO: sort the episodes into reverse order - currently they are "random"
    #       determined by the way python sorts its dictionary
    return render_template(
        'articles.html', 
        title="Past Articles"
        )


@app.route('/articles/<name>')
def view_article(name):
    if name not in articles:
        return abort(404)
    return render_template(
        'articles/%s.html' % name, 
        article=name, 
        title=articles[name]['title']
        )

@app.route('/subscribe', methods=['POST'])
def subscribe():
    conn = sqlite3.connect('../prodcast.db')
    db = conn.cursor()
    try:
        sql = "INSERT INTO emails (email, time_added, ip, browser) VALUES(?, ?, ?, ?)"
        db.execute(sql, (
                request.get_json()['email'].encode('utf-8').strip(),
                int(time.time()), 
                request.remote_addr,
                request.headers.get('User-Agent')
            )
        )
        conn.commit()
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/sw.js')
def service_worker():
    return send_file('static/js/sw.js')


@app.route('/favicon.ico')
def favicon():
    return send_file('static/img/favicon.ico')


@app.context_processor
def inject_url():
    return dict(url=request.url_rule, episodes=episodes, articles=articles)


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
