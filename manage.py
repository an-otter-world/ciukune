# coding: utf-8
#!/usr/bin/env python
#
# Copyright © 2019 STJV <contact@stjv.fr>
#
# This work is free. You can redistribute it and/or modify it under the terms
# of the Do What The Fuck You Want To Public License, Version 2, as published
# by the comrade Sam Hocevar.
#
# See the COPYING file for more details.
''' Django's command-line utility for administrative tasks. This file was auto
generated by the Django toolchain. Type python manage.py --help to see a list
of available commands. '''
import os
import sys

def main():
    ''' manage.py entry point '''
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
