# SchoologyMessageWebScraper
A Schoology Message Web Scraper made using BeautifulSoup4 in Python

## How it Works?
The web scraper extracts information from a schoology message page's html using BeautifulSoup4. In order to access the html, the web scraper must be logged in using proper schoology credentials. 

Therefore, the fields required are:
* Link of Schoology Message Page
* Login Username
* Login Password

The output will be printed as well as dumped into an "output.txt" file. The current version can extract all message attachments(images or otherwise) and will return a link for each of these attachments.

If parser does not properly read, please check troubleshooting guide.

## Troubleshooting Guide
If web scraper does not work properly, please try the following solutions:
* Make sure credentials are correct
* If using Schoology from a different district other than DASD, you will likely need to change session login values. See how to do that below.
* If none of the fixes above don't work, please file a issue. Please replicate the scenario with as simple an example as possible. 

## Changing Login Values
Go to your respective schoology login page in Chrome(works in other browsers, but I don't know the procedure) and use "Ctrl+Shift+I" to open up builtin inspector. Then, press on the "Network" tab on the top bar. Then, keeping the inspector open, enter your Schoology login credentials and press submit. Then, click on the first event that should have just popped up in the "Network" tab. Make sure that for "Request Method" it says "POST" and not "GET". Then, scroll down to the form data section. Under this section, you will see all the parameters that need to be passed in order for login. For changes to the code, you will need to change "linkForLogin"(Line 15) to the link of your schoology login page. Lastly, add the login parameters from the inspector just as is in the original code on line 21. Save and try the code again. If web scraper still doesn't work, please file a issue. Please replicate the scenario with as simple an example as possible.

![Image of Finding Form Data in Inspector](https://github.com/Saptak625/SchoologyMessageWebScraper/blob/main/Troubleshooting%20Screenshots/findFormInfo.png)

## Dependencies
* BeautifulSoup4
* lxml
* requests
* getpass

## Open-Source
This program is completely open-source. Any expansions on this program are permitted by all users.
