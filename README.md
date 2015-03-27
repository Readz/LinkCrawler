# LinkCrawler
Crawl a web site and count the number of links of specific types

--
### Author(s):
Derek Frank &lt;derek at readz dot com&gt;


### Install
#### Mac OS X (Yosemite)
Open Terminal `/Applications/Utilities/Terminal.app`

    CMD-SPACE
    terminal.app

Command line tools.

    % xcode-select --install
    
Git makes retrieving files simple.

    % git clone git@github.com:Readz/LinkCrawler.git || git clone https://github.com/Readz/LinkCrawler.git

Be sure to navigate within the base directory of the package.

    % cd LinkCrawler

Run install script.

    % ./install


### Uninstall
#### Mac OS X (Yosemite)
Open Terminal and `cd` to your `LinkCrawler` directory.

Run uninstall script.

    % ./uninstall


### Example Usage
Print help.

    % find_resources -h

Find all PDFs on cslibrary.stanford.edu

    % find_resources http://cslibrary.stanford.edu

Find all images (PNG, JPEG, GIF, ...) on a single page.

    % find_resources --dont-follow -c image http://cslibrary.stanford.edu/110 

Force include size information of resources.

    % find_resources --deoptimize http://cslibrary.stanford.edu

Unless specified, the output CSV file will be located on the Desktop as "resources.csv"

    % find_resources -o "Desktop/cslibrary-pdfs.csv" http://cslibrary.stanford.edu


### Potential Platform Errors
##### OSX Python Cryptography [source](http://chriskief.com/2014/03/25/installing-cryptography-via-pip-with-macports-or-homebrew/)

MacPorts

    % sudo port selfupdate
    % sudo port upgrade outdated
    % sudo port install openssl
    % sudo env ARCHFLAGS="-arch x86_64" LDFLAGS="-L/opt/local/lib" CFLAGS="-I/opt/local/include" pip install --upgrade --force-reinstall pyopenssl cryptography

Homebrew

    % brew install openssl
    % env ARCHFLAGS="-arch x86_64" LDFLAGS="-L/usr/local/opt/openssl/lib" CFLAGS="-I/usr/local/opt/openssl/include" pip install --upgrade --force-reinstall pyopenssl cryptography


### Credits:
 * [testspiders](http://github.com/scrapinghub/testspiders)
