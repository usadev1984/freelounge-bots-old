# freelounge
this project is a fork of [*CatLounge*](https://github.com/CatLounge/CatLounge) and it currently hosts the source code of freelounge's /sd/ and /bbc/ bots.

## Changes
you can find the latest changes in [changelog](changelog.txt) or check [change_history](change_history.txt) for the changes that were introduced during each update.

## Setup
to setup the bot and start it, see [*catlounge's setup section*](https://github.com/CatLounge/CatLounge#setup) or [*secertlounge's setup section*](https://github.com/secretlounge/secretlounge-ng/#setup)

## migrating from sqlite to json
starting from version 0.2, to use certain features you must use a json database.

### requirements for migrating old sqlite database to json

- [nushell](https://www.nushell.sh/)
- [jq](https://archlinux.org/packages/extra/x86_64/jq/)

### steps for migration
BACKUP YOUR OLD DATABASE BEFORE PROCEEDING

1. from within nushell run
    ```bash
    $ open secretlounge.sqlite | to json --raw | save tmp.json
    ```
2. in your default shell run
    ```bash
    $ cat tmp.json | jq > infile.json
    ```
3. make sure that sqlite2json.py is executable and run
    ```bash
    $ ./sqlite2json.py
    ```

the resulting json database will be stored as *outfile.json*. be sure to test the new database before removing the old one.

## Contact
you can contact us by joining the discussion chat for the [*freelounge announcement channel*](https://t.me/freeloungebots).
