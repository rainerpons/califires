# CALIFIRES

> Califires is an application that presents CAL FIRE incident data in an easy-to-read way by scraping and cleaning over a decade's worth of incident data.

![Image of dry California](https://c2.staticflickr.com/8/7458/27433298474_537359d71c_b.jpg "Santa Teresa County Park")

## Table of Contents
* [Technical Overview](#technical-overview)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installing](#installing)
* [Libraries](#libraries)
* [License](#license)

## Technical Overview

At its current stage, Califires has a three part system: scraping, cleaning, and archiving incident data.

First, the `scraper` module uses an HTML parser to scrape CAL FIRE's incident data. Then the `cleaner` module uses regular expressions and string manipulation to clean the scraped data. Lastly, the `archiver` module stores document-oriented data using the database program MongoDB.

The next step is to use data analysis packages in order to observe and to predict trends in the incident data.

Note: I am not affiliated with the California Department of Forestry and Fire Protection (CAL FIRE).

## Getting Started

### Prerequisites

* [Python](https://www.python.org/downloads) (programming language)
* [pip](https://pip.pypa.io/en/stable/installing) (package management)
* [Pipenv](https://pipenv.readthedocs.io/en/latest/install) (dependency management)

### Installing

Download the master branch of the Califires repository onto your local machine. Then make sure that pip and Pipenv are already installed.

You can use the Terminal command `pip install` to install the necessary packages indicated in the file [`califires/Pipfile`](Pipfile).

## Libraries

* [Pandas](https://pandas.pydata.org/pandas-docs/stable/install.html#installing-from-pypi) (data manipulation)
* [PyMongo](http://api.mongodb.com/python/current/installation.html#installing-with-pip) (database driver)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup), [LXML](https://lxml.de/installation.html#installation), and [html5lib](https://html5lib.readthedocs.io/en/latest/#installation) (HTML parsing)

## License

This project is licensed under the GNU General Public License. See the [LICENSE.md](LICENSE.md) file for details.