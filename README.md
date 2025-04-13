EuroPython Theme for MoinMoin Wiki
==================================

This [MoinMoin theme][] is used as the default theme for the [Python Wiki][].

It was created by Radomir Dopieralski in 2009 based on the default MoinMoin
theme [of that time][], adapted to match the look of [the Python.org website][]
at that time.

This is a fork of the original version.

In case you were wondering: this theme was originally used for the EuroPython
conferences in [2009][] and 2010.


Installation
------------

1. clone this repository or download a .zip of [the latest release][] and
   extract it somewhere
2. copy or symlink `europython.py` from this repository to the
   `wiki/data/plugin/theme` directory within your MoinMoin installation:

    ```bash
    cd path/to/YourMoinMoin/wiki/data/plugin/theme
    cp path/to/moin-europython-theme/europython.py .

    # or, for local development
    ln -s path/to/moin-europython-theme/europython.py
    ```
3. create a new directory `MoinMoin/web/static/htdocs/europython` in your
   MoinMoin installation and copy or symlink `css` and `img` from this
   repository to this new directory:

    ```bash
    cd path/YourMoinMoin/MoinMoin/web/static/htdocs
    mkdir europython
    cp -r path/to/moin-europython-theme/css europython
    cp -r path/to/moin-europython-theme/img europython

    # or, for local development
    cd europython
    ln -s path/to/moin-europython-theme/css
    ln -s path/to/moin-europython-them/img .
    ```
4. update the [site logo][] and its alt text by modifying `logo_string` in your
   `wikiconfig.py`; see below if running the local development server

    ```bash
    cp wikiconfig.py wikiconfig.py.orig

    # Linux
    sed -i -e 's^common/moinmoin.png^europython/img/python-logo.gif^' \
        -e 's/alt="MoinMoin Logo"/alt="Python logo"/' wikiconfig.py

    # macOS or *BSD
    sed -i '' -e 's^common/moinmoin.png^europython/img/python-logo.gif^' \
        -e 's/alt="MoinMoin Logo"/alt="Python logo"/' wikiconfig.py
    ```
5. if desired, set the default theme to be `europython` in your
   `wikiconfig.py`:

    ```python
    # inside your `wikiconfig.py`…
    theme_default = 'europython'
    ```

    At your option, you can make this the _only_ theme available to users with:

    ```python
    # inside your `wikiconfig.py`…
    theme_force = True
    ```

    These settings don't exist when using the `wikiconfig.py` supplied for the
    local development server (see below), so you'll need to add them.


Development
-----------

For local development, it's sufficient to run `wikiserver.py` from the top
level of the unpacked MoinMoin source:

```bash
python27 wikiserver.py

# or, if Python 2.7 is your default `python`, simply
./wikiserver.py
```

You may see this referred to in various places as the "Desktop Edition" of
MoinMoin, mostly in the form of admonishments not to use it in production.

The "Desktop Edition" reads its configuration (_e.g._, `wikiconfig.py`
and `wikiserverlogging.conf`) from the same directory where `wikiserver.py`
resides. You may notice a `wiki/config/wikiconfig.py` which is intended as a
template for a [WSGI server installation][]; do not modify this one for a local
development setup, as your changes will have no effect.


License
-------

[GPLv2](LICENSE)


[MoinMoin theme]: https://moinmo.in/HelpOnThemes
[Python Wiki]: https://wiki.python.org
[of that time]: https://web.archive.org/web/20090826084417/http://moinmo.in/MoinMoin
[the Python.org website]: https://web.archive.org/web/20090201113423/http://python.org
[2009]: https://www.europython-society.org/europython/#europython-2009
[the latest release]: https://github.com/malemburg/moin-europython-theme/archive/refs/heads/main.zip
[site logo]: https://master.moinmo.in/HelpOnThemes#Modify_wiki_configuration
[WSGI server installation]: https://master.moinmo.in/InstallDocs/ServerInstall
