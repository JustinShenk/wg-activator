WG-activator
============

## Install

Clone the repository and enter the directory. Activate Python 3 virtual environment if necessary.

Note: assumes Mac with Chromedriver installed in `/Applications`. If running Linux or Windows, download [Chromedriver](http://chromedriver.chromium.org/downloads) and fix path in `wg-updater.py`.

Run `pip install selenium`.

```
mv config-sample.ini config.ini
```

Change the fields in config.ini to reflect your settings.

```
python wg-updater.py
```
