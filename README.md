# automated whatsapp messanger

This is a python application to send bulk attachments to numbers from a text file.

## Installation
Just download the zip file Or clone the repo on your system and follow the usage instructions below.

##setup
You will have to set the directories yourself
##In cookie.py
in line 4
```python
options​.​add_argument​(​'--user-data-dir=C:/Users/<your user name>/AppData/Local/Google/Chrome/for_rid'​)
```
##In whatsapp_bulk_messanger.py
In line 23
```python
​image_attach​.​send_keys​(​'C:​\\​Users​\\​,,<your user name>​\\​Desktop​\\​PYTHON​\\​tst.jpg'​)
```
In line 30 pass the name of your text file where from where the program will grab the numbers

```python
​with​ ​open​(​'numbers.txt'​,​'r'​) ​as​ ​f​:
```

In line 40 pass the directory from where the program will grab the session to bypass the QR ccode
```python
​options​.​add_argument​(​"--user-data-dir=C:/Users/<your user name>/AppData/Local/Google/Chrome/for_rid"​)
 ```

And keep the chromedriver.exe in the same direcotry as the program,or it will throw errors.


##USAGE
1.At first you have to scan the whatsapp Web QR code,for that just run
```bash
python cookie.py
```
In terminal,

NOTE - this cookie.py program will store the session cookie on your pc so you won't have to scan the QR code again next time.

After scanning the QR code close that chrome window.

And run 
```bash
python whatsapp_bulk_messanger.py
```
