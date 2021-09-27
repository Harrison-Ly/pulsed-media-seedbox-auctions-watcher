# pulsed-media-seedbox-auctions-watcher

Watch the Pulsed Media Seedbox Auctions for your price target and get notified via pushover

## Requirements
- Python 3.8.2
- pushover-complete 1.1.1

## Setup
```
pip install -r requirements.txt
```

## Configuration
1. change `PRICE_TARGET` in `pulsedmedia_watch.py`
2. add your pushover keys in `config.py`

## Crontab
Run the script every minute  
```
* * * * * python <path_to>/pulsedmedia_watch.py >> /var/log/pulsedmedia_watch.log 2>&1
```
