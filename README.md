codereview
==========

A script for listing most recent work by an author on multiple git repositories

Scans through any folders from the directory it is called from looking for git repository and will list and repositorys that have a commit by an author matching the provided string, ordered by most recent commits.

Git author searching will use like matching, so searching part of a name will work.

###Requirements###

- Python
- GitPython

####Ubuntu Instructions####

```
sudo apt-get install python python-git
```

###Usage###

use in the directory that contains all your repositorys

```
./codereview.py _username_
```

Example:
```
./codereview.py smmccabe
```
