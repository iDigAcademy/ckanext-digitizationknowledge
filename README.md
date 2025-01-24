[![Tests](https://github.com/iDigAcademy/ckanext-digitizationknowledge/workflows/Tests/badge.svg?branch=main)](https://github.com/iDigAcademy/ckanext-digitizationknowledge/actions)

# ckanext-digitizationknowledge

This extension contains customization for adapting CKAN for a digitization resources knowledge base.


## Requirements

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.6 and earlier | no            |
| 2.7             | no            |
| 2.8             | no            |
| 2.9             | not tested    |
| 2.10            | not tested    |
| 2.11.1          | yes           |

Values:

* "yes"
* "not tested" - I can't think of a reason why it wouldn't work
* "not yet" - there is an intention to get it working
* "no"


## Installation

To install ckanext-digitizationknowledge:

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

    git clone https://github.com/iDigAcademy/ckanext-digitizationknowledge.git
    cd ckanext-digitizationknowledge
    pip install -e .
	pip install -r requirements.txt

3. Add `digitizationknowledge` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload


## Config settings

None at present

## Developer installation

To install ckanext-digitizationknowledge for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/iDigAcademy/ckanext-digitizationknowledge.git
    cd ckanext-digitizationknowledge
    pip install -e .
    pip install -r dev-requirements.txt


## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini
