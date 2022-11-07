import os
import sys

os.system("git bisect start " + sys.argv[1] + " " + sys.argv[2])
os.system("git bisect run python manage.py test")
os.system("git bisect reset")
