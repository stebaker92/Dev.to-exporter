# Dev.to Exporter

A Python script to export all of your Dev.to articles as local Markdown files — useful for migrating to a self-hosted blog or archiving your content.

## Usage
- Create a dev.to API KEY and put it in a `.env` file (or rename `.env.example`)
- Install python requirements `pip3 install -r requirements.txt`
- Run `python3 dev.to-exporter.py` to download all posts to a `posts/` directory
