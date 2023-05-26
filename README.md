<div align="center" id="top">
  <img src="./.github/app.gif" alt="Eod" />

  &#xa0;

  <!-- <a href="https://eod.netlify.app">Demo</a> -->
</div>

<h1 align="center">EOD Stock Data Downloader</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/javiergarciad/eod?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/javiergarciad/eod?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/javiergarciad/eod?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/javiergarciad/eod?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/javiergarciad/eod?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/javiergarciad/eod?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/javiergarciad/eod?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center">
	🚧  Eod 🚀 Under construction...  🚧
</h4>

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0;
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/javiergarciad" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Simple example of flask backend for downloading stock EOD data from Yahoo. This script will create and update a SQlite database with last year EOD prices for a group of stocks, using Yahoo Finances data.

You can connect to the SQLite database using any external tool to use the data, or you can download CSV file per symbol. This version only download last year data.

This is a very basic example, not suitable for production enviroments. Many logics are not implemented. Feel free to clone it and play with it.

## :sparkles: Features ##

:heavy_check_mark: Download 1yr EOD data.\
:heavy_check_mark: SQLite database you can access.\
:heavy_check_mark: Export to CSV.

## :rocket: Technologies ##

The following tools were used in this project:

- [Python](https://www.python.org/)
- [JQuery](https://jquery.com/)
- [Boostrap5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)


## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Python 3.10](https://www.python.org/) installed.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/javiergarciad/eod

# Access
$ cd eod

# Install dependencies
$ virtualenv .venv -f requirements.txt

# Run the project
$ flask run

# The server will initialize in the <http://localhost:5000>
```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/javiergarciad" target="_blank">Javier Garcia</a>

&#xa0;

<a href="#top">Back to top</a>
