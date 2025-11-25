# -*- coding: utf-8 -*-
"""
Add old wordpress comments to posts' metadata
=============================================
"""

import os
import json
from pelican import signals
from datetime import datetime
import pytz

comments = {}

with open('comments.json') as f:
    comments = json.load(f)

# preprocess dates so we can easily format them later
for postid, postcomments in comments.items():
    for comment in postcomments:
        comment['datetime'] = datetime.strptime(comment['date_gmt'], "%Y-%m-%d %H:%M:%S").replace(tzinfo=pytz.utc)

def static_comments(generator, metadata):
    if 'wordpress_id' in metadata and metadata['wordpress_id'] in comments:
        metadata.update({'static_comments' : comments[metadata['wordpress_id']]})

def register():
    signals.article_generator_context.connect(static_comments)
