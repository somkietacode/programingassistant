# programingassistant
![eliot](https://user-images.githubusercontent.com/108131461/222901063-7f4c8d92-ed82-4147-a1ed-f558f04d2fcd.png)

This is Eliot your comandline based programing assistant. Ask him anything about programing, he would be glad to help you.
A project inpired by Chat GPT

### email : s.r.a.ouedraogo@gmail.com

### Tel : 226 72 58 78 71 / 57 74 21 32

# How it work ?

Just instal the required libraries using :

```console
foo@bar:~$ pip install -r requirement.txt
Requirement already satisfied: bs4 in c:\users\sraou\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from -r requirement.txt (line 1)) (0.0.1)
Requirement already satisfied: requests in c:\users\sraou\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from -r requirement.txt (line 2)) (2.28.2)
Requirement already satisfied: beautifulsoup4 in c:\users\sraou\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from bs4->-r requirement.txt (line 1)) (4.11.2)
Requirement already satisfied: idna<4,>=2.5 in c:\users\sraou\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from requests->-r requirement.txt (line 2)) (3.4)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\users\sraou\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from requests->-r requirement.txt (line 2)) (1.26.14)
Requirement already satisfied: certifi>=2017.4.17 in c:\users\sraou\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from requests->-r requirement.txt (line 2)) (2022.12.7)
Requirement already satisfied: charset-normalizer<4,>=2 in c:\users\sraou\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from requests->-r requirement.txt (line 2)) (3.0.1)
Requirement already satisfied: soupsieve>1.2 in c:\users\sraou\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (from beautifulsoup4->bs4->-r requirement.txt (line 1)) (2.4)

[notice] A new release of pip available: 22.3.1 -> 23.0.1
[notice] To update, run: C:\Users\sraou\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip

```

Then simply go to the path where you clone the repostorie and run :

```console
foo@bar:~$ python ProgramingAssistant.py
Hi, my name is  Eliot . Ask me something about how to program something i would be glad to help you...
Eliot > So, how could i help you today ?
User >
```

Simply ask your question and press enter :
```console
User > What is sql injection ?
Eliot >
Can someone explain SQL injecton?
SQL injection happens when you interpolate some content into a SQL query string, and the result modifies the syntax of your query in ways you didn't intend.
It doesn't have to be malicious, it can be an accident.  But accidental SQL injection is more likely to result in an error than in a vulnerability.
The harmful content doesn't have to come from a user, it could be content that your application gets from any source, or even generates itself in code.
How does it cause vulnerabilities?
It can lead to vulnerabilities because attackers can send values to an application that they know will be interpolated into a SQL string.  By being very clever, they can manipulate the result of queries, reading data or even changing data that they shouldn't be allowed to do.
Example in PHP:
$password = $_POST['password'];
$id = $_POST['id'];
$sql = "UPDATE Accounts SET PASSWORD = '$password' WHERE account_id = $id";

Now suppose the attacker sets the POST request parameters to "password=xyzzy" and "id=account_id" resulting in the following SQL:
UPDATE Accounts SET PASSWORD = 'xyzzy' WHERE account_id = account_id

Although I expected $id to be an integer, the attacker chose a string that is the name of the column.  Of course now the condition is true on every row, so the attacker has just set the password for every account.  Now the attacker can log in to anyone's account -- including privileged users.
Where exactly is the point where SQL is injected?
It isn't SQL that's injected, it's content that's interpolated ("injected") into a SQL string, resulting in a different kind of query than I intended.  I trusted the dynamic content without verifying it, and executed the resulting SQL query blindly.  That's where the trouble starts.
SQL injection is a fault in the application code, not typically in the database or in the database access library or framework.
Most cases of SQL injection can be avoided by using query parameters. See How can I prevent SQL injection in PHP? for examples.
```

```console
User > How to translate using python ?
Eliot >
With the googletrans (pypi.org/project/googletrans) module that is possible. The following code takes an input folder with text files of the format you provided (multiple occurrences are allowed), translates the relevant parts and creates a new translated text file in the output folder for every input file. Please be aware that google translate is not known for its accuracy. 
googletrans translated your examples:"Finish Black Peter case." to "Valmis Musta Pekka tapaus.""Aye Aye, Captain!" to "Ai-ai, kapteeni!"
from googletrans import Translator
import os
import re

INPUT_FOLDER_PATH = 'path/to/inputFolder'
OUTPUT_FOLDER_PATH = 'path/to/outputFolder'

# a translator object from the googletrans api
tl = Translator()

# go through all the files in the input folder
for filename in os.listdir(INPUT_FOLDER_PATH):

    # open the file to translate and split the data into lines
    in_file = open(f'{INPUT_FOLDER_PATH}/{filename}', 'r')
    data = in_file.read()
    data = data.split('\n')

    # the modified data string we will now fill
    transl_data = ""

    # translate the relevant parts of each line
    for line in data:

        # find matches: is this a relevant line?
        locname = re.findall('(?<=LocName=").*(?=")', line)
        locdesc = re.findall('(?<=LocDescription=").*(?=")', line)

        # if there is a locName or locDescription match, translate the important part and replace it
        if len(locname) == 1:
            locname_trans = tl.translate(locname[0], dest='fi').text
            line = re.sub('(?<=LocName=").*(?=")', locname_trans, line)
        elif len(locdesc) == 1:
            locdesc_trans = tl.translate(locdesc[0], dest='fi').text
            line = re.sub('(?<=LocDescription=").*(?=")', locdesc_trans, line)

        # add the translated line to the translated string
        transl_data += line + '\n'

    # create a new file for the translations
    out_file = open(f'{OUTPUT_FOLDER_PATH}/{filename}-translated', 'w')

    # write the translated data to the output file
    out_file.write(transl_data)

    # clean up
    in_file.close()
    out_file.close()

```

# Screen shoot
![image](https://user-images.githubusercontent.com/108131461/222900549-077139c6-fd88-407e-9ada-0da0a0ef314c.png)

# Try it your self it is amazing 
## Don't forget to leave stars on the repo that help referencing...

## Support

You can ask questions and join the development discussion:

- [Facebook page](https://www.facebook.com/globalanalysistech) .

