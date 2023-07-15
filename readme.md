# MastodonCrawler
Crawler for Mastodon. Spanish comments by h3st4k3r.
This is a crawler for Mastodon. Enter the user, read new posts, and send an email.
You can monitor as many users as you want. It is recommended to follow the comments throughout the code.
Initially developed for monitoring la9deanon.

##Description
This repository contains a Python script for crawling Mastodon, a decentralized social media platform. The script allows you to input a user, read their new posts, and send email notifications.

##Prerequisites
Python 3.x
Required libraries: html5lib, bs4, urlopen

##Usage
Install the required dependencies:

`pip install html5lib bs4`

Update the necessary variables in the script:

```python
password: Your email password.
msg['From']: The email address from which you want to send notifications.
msg['To']: The email address of the receiver.
```

###Run the script:

`python mastodon_crawler.py`

##Contributing
Contributions are welcome! If you have any ideas or improvements, please open an issue or submit a pull request.

##License
This project is licensed under the GNU License.
