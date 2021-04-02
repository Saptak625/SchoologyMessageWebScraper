from requests import Session
from bs4 import BeautifulSoup
import lxml
import getpass

print("------------------------------------Schoology Message Bot------------------------------------")

outputFile = open('output.txt', 'w')

def addEntry(text):
  print(text)
  outputFile.write(text+"\n")

linkToParse = input('Enter Link to Parse: ')
linkForLogin = "https://schoology.dasd.org/login/ldap?&school=6571728"
loginUsername = input("Username: ")
loginPassword = getpass.getpass()
with Session() as s:
  site = s.get(linkForLogin)
  bs_content = BeautifulSoup(site.content, "html.parser")
  login_data = {"mail":loginUsername,"pass":loginPassword, 'school_nid':"6571728", 'form_build_id':'583f9a7-8AeXRRqi2yOHzBOqVQXOZ6VYy876DDxCl86I3SO98tk', 'form_id':'s_user_login_form'}
  s.post(linkForLogin, login_data)
  home_page = s.get(linkToParse)
  file = open("schoology.html", 'w')
  file.write(home_page.content.decode("utf-8"))
  file.close()

with open('schoology.html') as html_file:
  soup = BeautifulSoup(html_file, 'lxml')

#Find Individual Messages 
messages = soup.find_all('div', class_='s_message_box')
for message in messages:
  username = message.find('a', title="View user profile.").text
  msgTime = message.find('span').text
  addEntry(f'==> {username} at {msgTime}')
  msgText = message.find('div', 'message-body').p.text
  addEntry(msgText)
  #Check for attachements
  if message.find('div', 's-message-attachments-container') != None:
    attachments = []
    #There are attachments
    #Check for pics
    if message.find('div', 'attachments-file-image') != None:
      #There are pics attached.
      for picDiv in message.find_all('div', 'attachments-file-image'):
        attachments.append(picDiv.div.a['href'])
    #Check for all other types of files
    if message.find('div', 'attachments-file') != None:
      for picDiv in message.find_all('div', 'attachments-file'):
        attachments.append(picDiv.find('span', 'attachments-file-name').a['href'])
    #Add all Attachments in file
    for a in attachments:
      addEntry(a)
    addEntry('\n----------------------------------------------------------------------------------\n')
outputFile.close()