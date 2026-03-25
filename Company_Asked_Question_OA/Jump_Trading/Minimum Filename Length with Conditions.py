'''Task 2

You are given a string containing a detailed list of files. Your task is to evaluate a simple query on a certain subset of these files.

The string consists of N lines separated by end-of-line characters (ASCII code 10). Each line contains information about one file, grouped into three columns:
owner, permissions, and name (in that order).

The columns (except for the last one) have fixed lengths and are separated by one space. They have the following format and meanings:

📌 Column descriptions:
Column owner
Length: 6
A string representing the name of the user who created the file.
The name is case-sensitive and aligned to the right.
Column permissions
Length: 3
Contains three characters:
First → read permission
Second → write permission
Third → execute permission
Each character is either:
'r', 'w', 'x' (permission granted)
or '-' (permission not granted)
Column name
Variable length
The name of the file.
Contains at most 255 printable ASCII characters.
Must contain at least one dot (.).
The part after the last dot is called the extension.
📂 Additional rules:
Files are only interested in if they contain binary document data, meaning their extension is one of:
"doc"
"xls"
"pdf"
A file is considered ready if:
The user has read permission, but NOT write permission
The file was created by a user whose name is not "root"
🎯 Task:

Calculate the minimum length of the names of these files that satisfy the above conditions.

✏️ Function requirement:

Write a function:

def solution(S)

that, given a string S describing the file list, returns the answer as a string.

If no files satisfy the criteria, return:
"NO FILES"
🧪 Example:

Input:

root r-x delete-this.xls
root r-- bug-report.pdf
root r-- doc.xls
root r-- podcast.flac
alice rwx system.xls
root --x invoices.pdf
admin r-- setup.py

Output:

7
⚠️ Assumptions:
N is an integer within range [1..100]
Strings contain only printable ASCII characters
The input string is a valid list of files according to the specification
File names are unique'''

import sys


class FileSystem:

    def Solution(self,x):
        min_len = sys.maxsize
        lines_sep = x.split('\n')
        print(lines_sep)

        for line in lines_sep:
            sept_str = line.split()
            last_filename = sept_str[-1]

            if '.' in last_filename:
                    name, ext = last_filename.rsplit('.', 1)
            else:
                    name, ext = last_filename, ''
            # print("Filename:", name, "Extension:", ext)

            if sept_str[0]!= 'root' and 'w' not in sept_str[1] and ext in ['pdf', 'xls', 'doc']:
                min_len = min(min_len,len(last_filename))
        
        if min_len == sys.maxsize:
            return "NO FILES"
        else:
            return min_len

fs = FileSystem()
print(fs.Solution(x= 'root r-x delete-this.xls\nroot r-- bug-report.pdf\nroot r-- doc.xls\nroot r-- podcast.flac\nalice rwx system.xls\nroot --x invoices.pdf\nadmin r-- setup.py\nalice r-- r.xls'))


'''The line:

name, ext = last_filename.rsplit('.', 1)

has two parts to focus on: rsplit and the 1.

1️⃣ rsplit
rsplit is like split, but it starts splitting from the right (the end of the string).
Syntax: string.rsplit(separator, maxsplit)
separator → character to split on (here, '.')
maxsplit → maximum number of splits (here, 1)

So, last_filename.rsplit('.', 1) means:

Split the string at the last dot only, giving two parts:

Everything before the last dot → name
Everything after the last dot → ext (extension)
2️⃣ Why 1?
Without 1, it would split all dots:
"my.file.name.xls".rsplit('.', 1)   # ['my.file.name', 'xls']
"my.file.name.xls".split('.')       # ['my', 'file', 'name', 'xls']

We only want the extension, so we limit to 1 split from the right.

--
filenames = [
    "my.file.name.xls",
    "document.pdf",
    "setup.py",
    "archive.tar.gz"
]

for f in filenames:
    if '.' in f:
        parts = f.rsplit('.', 2)
        if len(parts) == 3:
            name = parts[0]
            ext = parts[1] + '.' + parts[2]
        else:
            name = parts[0]
            ext = parts[1] if len(parts) > 1 else ''
    else:
        name, ext = f, ''
    print(f"Filename: {f} → name: {name}, ext: {ext}")
Output:

Filename: my.file.name.xls → name: my.file, ext: name.xls
Filename: document.pdf → name: document, ext: pdf
Filename: setup.py → name: setup, ext: py
Filename: archive.tar.gz → name: archive, ext: tar.gz

'''