# Ethics and Data Collection Practices

## Purpose of Data Collection

The primary purpose of this data collection project is to gather financial information on stocks identified as the top losers of the day. This data is intended for educational and research purposes, enabling users to develop and refine trading strategies based on daily market movements.
The data collected provides insights into market trends and stock performance, particularly focusing on stocks that have experienced significant losses. Analyzing this data can help traders and researchers identify potential investment opportunities and understand market dynamics better.

## Data Sources and Robots.txt

When collecting data through web scraping, it is crucial to ensure that the target websites do not explicitly prohibit scraping in their terms of service. This project adheres strictly to these guidelines, scraping only from sites that allow such activities.
The project respects the robots.txt file, a standard used by websites to instruct web crawlers which parts of the site should not be accessed or scraped. Before scraping any website, users are encouraged to check the robots.txt file (https://stockanalysis.com/robots.txt) and avoid scraping content from restricted areas.

## Collection Practices
To minimize the impact on the target websites, our scraping practices are designed to be non-intrusive. We limit the frequency and volume of requests to avoid overwhelming the server, thereby ensuring that our activities do not disrupt the normal functioning of the website.

Our project does not engage in any practices that involve bypassing password protection or accessing restricted areas of a website. We only collect data from publicly accessible pages that are intended for general viewing.

## Data Handling and Privacy
This project is committed to respecting user privacy and does not collect any Personally Identifiable Information (PII). The focus is solely on publicly available financial data related to stock performance.

Any collected data is stored securely to prevent unauthorized access. Sensitive files, such as those containing API keys or other confidential information, are added to `.gitignore` to ensure they are not inadvertently shared or exposed in public repositories.

## Data Usage

The data collected through this project is intended exclusively for educational and research purposes. Users are encouraged to use this information to enhance their understanding of market trends and develop informed trading strategies. It is not intended for commercial use or distribution without proper authorization.

By adhering to these ethical guidelines, we aim to conduct our data collection activities responsibly and respectfully, ensuring compliance with legal standards and ethical norms.