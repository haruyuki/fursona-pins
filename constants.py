import json
import os

from google.oauth2 import service_account
import pygsheets


def authorisation():
    scopes = ('https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive')  # The scopes the bot requires (Spreadsheets and Google Drive)
    credentials_raw = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS', '{}')  # Get the login credentials from environment variables
    service_account_info = json.loads(credentials_raw)
    credentials = service_account.Credentials.from_service_account_info(service_account_info, scopes=scopes)
    return pygsheets.authorize(custom_credentials=credentials)


class Constants:
    prefix = '.'
    owner_id = 277398425044123649
    discord_token = os.environ.get('discord', None)
    discord_log_filename = 'discord.log'
    version = '0.0.1'
    cogs_directory = 'cogs'
    playing_text = '.help | Haru#5616'
    embed_colour = 0x0D75BC
    contact_email='jumpy12359@gmail.com'
    http_headers = {'User-Agent': 'Fursona Pins Discord Bot Agent ' + version,
                    'From': contact_email}
    google_sheets_api = authorisation()


class FursonaPins:
    website = 'https://www.fursonapins.com'
    patreon = 'https://www.patreon.com/FursonaPins'
    trello = 'https://trello.com/b/bf1neYOZ/fursona-pins'
    twitter = 'https://twitter.com/FursonaPins'
    instagram = 'https://www.instagram.com/FursonaPins'
    facebook = 'https://www.facebook.com/FursonaPins'
    discord = 'https://discord.gg/3DWYuvj'
    telegram = 'https://t.me/FursonaPins'
    checklist_spreadsheet = 'https://docs.google.com/spreadsheets/d/1bYyZmN_Bm5NGHpRL-ox-5sn5kqsTDLNiLuyrbsEcEbY'

    fursona_pins_api = os.environ.get('fursona_pins_api', None)
    gallery = 'https://www.fursonapins.com/gallery'
    banner_logo = 'https://www.fursonapins.com/images/banner-logo.png'
    full_logo = 'https://www.fursonapins.com/images/logo.png'
