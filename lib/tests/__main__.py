# coding=utf-8
'''
truepy
Copyright (C) 2014 Moses Palmér

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
'''

import os
import sys

import tests
from tests.suites import *


failures = tests.run()
if failures is None:
    print('Test suite was cancelled by setup')
    sys.exit(-1)


print('')
print('All test suites completed with %d failed tests' % len(failures))
if failures:
    sys.stderr.write('Failed tests:\n%s\n' % '\n'.join(
        '\t%s - %s' % (test.name, test.message)
            for test in failures))
sys.exit(len(failures))