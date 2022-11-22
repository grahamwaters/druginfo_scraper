<!-- Hey Copilot, write me a professional ReadMe below -->

![banner](images/meds_banner.png)


**Version 1.0.0**

**Created by Graham Waters**
<div align='center'>
<!-- add badges for the issues, release, latest updates, and stars/forks -->

[![GitHub issues](https://img.shields.io/github/issues/grahamwaters/druginfo_scraper)](https://img.shields.io/github/issues/grahamwaters/druginfo_scraper)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/grahamwaters/druginfo_scraper)](https://img.shields.io/github/v/release/grahamwaters/druginfo_scraper)
[![GitHub last commit](https://img.shields.io/github/last-commit/grahamwaters/druginfo_scraper)](https://img.shields.io/github/last-commit/grahamwaters/druginfo_scraper)
[![GitHub stars](https://img.shields.io/github/stars/grahamwaters/druginfo_scraper)](https://img.shields.io/github/stars/grahamwaters/druginfo_scraper)
[![GitHub forks](https://img.shields.io/github/forks/grahamwaters/druginfo_scraper)](https://img.shields.io/github/forks/grahamwaters/druginfo_scraper)
<!-- add view count to the repo -->
![ViewCount](https://views.whatilearened.today/views/github/grahamwaters/druginfo_scraper.svg)

</div>




## Table of Contents

- [Table of Contents](#table-of-contents)
- [Description](#description)
- [Usage](#usage)
- [License](#license)
- [Contributing](#contributing)
- [Tests](#tests)
- [Questions](#questions)
- [Instructions](#instructions)
- [Repositories that we hope to integrate with in the future](#repositories-that-we-hope-to-integrate-with-in-the-future)

## Description
This simple tool scrapes drug names from `druginfo.nlm.nih.gov` using `bs4` and `requests`.

This script is designed to pull drug names from the website and return a pandas dataframe for use in various applications. I am not responsible for any misuse of this script. It implements a sleeping time to limit the rate of requests to the website.


## Usage

```python
from drug_scraper import DrugScraper
ds = DrugScraper()
df = ds.get_drug_names()
```


## License

This project is licensed under the ${data.license} license.

## Contributing

${data.contributing}

## Tests

To run tests, run the following command:

```
${data.tests}
```

## Questions

See my profile for contact information.

## Instructions

Scrapes Drug names from [druginfo.nlm.nih.gov](https://druginfo.nlm.nih.gov/drugportal/drug/names/a) using bs4 and requests.

This script is designed to pull drug names from the website and return a pandas dataframe for use in various applications. I am not responsible for any misuse of this script. It implements a sleeping time to limit the rate of requests to the website.

## Repositories that we hope to integrate with in the future

1. https://github.com/mlbernauer/drugstandards