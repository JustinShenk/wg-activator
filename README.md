WG-activator
============

## Install

Clone the repository and enter the directory. Activate Python 3 virtual environment if necessary.

Note: assumes Mac with ChromeDriver installed in `/Applications`. If running Linux or Windows, download [ChromeDriver](http://chromedriver.chromium.org/downloads) and update `CHROMEDRIVER_PATH` in `wg-updater.py`.

Run `pip install selenium`.

```bash
mv config-sample.ini config.ini
```

Change the fields in config.ini to reflect your settings.

```bash
python wg-updater.py
```
