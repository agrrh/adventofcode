#!/usr/bin/env python3

import os
import requests
import json
import logging


def aoc_data_get(event, table_id, cookie_session):
    response = requests.get(
        'https://adventofcode.com/{e}/leaderboard/private/view/{t}.json'.format(e=event, t=table_id),
        cookies={'session': cookie_session}
    )

    result = None

    try:
        result = response.json()
    except json.decoder.JSONDecodeError:
        logging.error('Can\'t decode JSON: {}'.format(response.text))

    return result


def slack_send(token, channel, data):
    payload = {
        "channel": channel,
        "username": "AdventOfCode",
        "icon_emoji": ":christmas_tree:",
        "text": "\n".join([
            "*{user}* :star: x {stars} = {score} pts".format(
                user=user[2], stars=user[1], score=user[0]
            )
            for user
            in data
        ]),
    }

    logging.warning('Sending data: {}'.format(payload))

    response = requests.post(
        'https://hooks.slack.com/services/{t}'.format(t=token),
        json=payload
    )

    logging.warning('Response: {} {}'.format(response.status_code, response.text))


def main():
    event = os.environ.get('AOC_EVENT', '2019')
    table_id = os.environ.get('AOC_TABLE_ID', '0')
    cookie_session = os.environ.get('AOC_COOKIE_SESSION', '0')
    slack_token = os.environ.get('SLACK_TOKEN', '0')
    slack_channel = os.environ.get('SLACK_CHANNEL', '@me')

    data = aoc_data_get(event, table_id, cookie_session)

    # Get only significant informaion
    table = [
        (user.get('local_score'), user.get('stars'), user.get('name'))
        for user_id, user
        in data.get('members', {}).items()
    ]
    # Sort by score
    table = sorted(table, reverse=True, key=lambda x: x[0])

    slack_send(slack_token, slack_channel, table)


if __name__ == '__main__':
    main()
