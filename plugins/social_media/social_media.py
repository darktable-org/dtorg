# -*- coding: utf-8 -*-
"""
Post new posts to social media
=====================================
Post to Twitter, Facebook and G+ whenever a new blog or news post gets added
For now only Twitter is supported
"""

import string

import logging
logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)

from pelican import signals

# https://github.com/bear/python-twitter/wiki
import twitter


def read_sitemap():
    try:
        with open('posted_to_social_media.txt', 'r') as f:
            result = map(string.rstrip, f)
    except IOError:
      result = []
    return result


def write_sitemap(sitemap):
    sitemap.sort()
    with open('posted_to_social_media.txt', 'w') as f:
        for article in sitemap:
            f.write("%s\n" % article)

def shorten(message, limit, replacement = u' …'):
    if twitter.twitter_utils.calc_expected_status_length(message) <= limit:
        return message
    limit -= twitter.twitter_utils.calc_expected_status_length(replacement)
    words = message.split()
    result = words.pop(0)
    if twitter.twitter_utils.calc_expected_status_length(result) > limit:
        return result[:limit] + replacement
    while words:
        candidate = result + ' ' + words.pop(0)
        if twitter.twitter_utils.calc_expected_status_length(candidate) <= limit:
            result = candidate
        else:
            break
    result += replacement
    return result


def post_on_twitter(settings, new_posts):
    consumer_key = settings.get('TWITTER_CONSUMER_KEY', '')
    consumer_secret = settings.get('TWITTER_CONSUMER_SECRET', '')
    access_token_key = settings.get('TWITTER_ACCESS_TOKEN_KEY', '')
    access_token_secret = settings.get('TWITTER_ACCESS_TOKEN_SECRET', '')

    if consumer_key == '' or consumer_secret == '' or access_token_key == '' or access_token_secret == '':
        print('Twitter credentials not configured')
        return False

    api = twitter.Api(consumer_key = consumer_key,
                      consumer_secret = consumer_secret,
                      access_token_key = access_token_key,
                      access_token_secret = access_token_secret)

    try:
        api.VerifyCredentials()
    except:
        print('error authenticating to Twitter')
        return False

    limit = 275 # actually 280 but let's account for some bugs and miscalculations
    message = 'new post on darktable.org:\n%s\n%s'

    for article in new_posts:
        url = article.get_siteurl() + '/' + article.url
        free_space = limit - twitter.twitter_utils.calc_expected_status_length(message % ('', url))
        title = shorten(article.title, free_space)
        post = message % (title, url)
        print(post.encode('utf-8'))
        # api.PostUpdate(post) # TODO: add this line and maybe do some error checking

    return True


def post_updates(generator, writer):
    sitemap = read_sitemap()
    new_posts = []
    for article in generator.articles:
        if article.url not in sitemap:
            new_posts.append(article)

    # we only write the newly found sites to disk if posting them worked. that way we can retry later
    if new_posts:
        if post_on_twitter(generator.settings, new_posts):
            for article in new_posts:
                sitemap.append(article.url)
            write_sitemap(sitemap)


def register():
    """Plugin registration"""
    try:
        signals.article_writer_finalized.connect(post_updates)
    except AttributeError:
        pass
