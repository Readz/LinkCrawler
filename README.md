# LinkCrawler
Crawl a web site and count the number of links of specific types

--
### Author(s):
Derek Frank &lt;derek at readz dot com&gt;

### Install

    # Install Python packages.
    % python -m ensurepip
    % sudo pip install setuptools
    # Build and install.
    % python setup.py build
    % sudo python setup.py install --install-scripts=/usr/local/bin

### Uninstall

    % sudo pip uninstall ResourceCrawler
    % sudo rm /usr/bin/local/find_resources

### Example Usage

    # Print help.
    % find_resources -h
    # Find all PDFs on cslibrary.stanford.edu
    % find_resources http://cslibrary.stanford.edu
    # Find all images (PNG, JPEG, GIF, ...) on a single page.
    % find_resources --dont-follow -c image http://cslibrary.stanford.edu/110 
    # Force include size information of resources.
    % find_resources --deoptimize http://cslibrary.stanford.edu
    # Unless specified, the output CSV file will be located on the Desktop as "resources.csv"
    % find_resources -o "Desktop/cslibrary-pdfs.csv" http://cslibrary.stanford.edu

### Credits:
 * [testspiders](http://github.com/scrapinghub/testspiders)
