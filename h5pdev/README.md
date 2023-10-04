README.md

Constructing H5P Fill in the Blank Modules

In Python script

1. Open content-template.json for READING and import using json.loads() into variable type dict.

E.g., 
import json

with open ('content-template.json', 'r') as f:
    d = json.loads(f.read())

2. Write passage text to dict item with key 'questions'

	d['questions'] = passage_text

3. Create new directory with name with a random guid.

4. Serialize d in json: json.dumps(d)

5. Write d as a new file named 'content.json' to directory created in 3.


Testing in Browser
1. Open viewer.html, change DIRNAME in Javascript with name of directory created in 3.

2. Save an load viewer.html in browser.