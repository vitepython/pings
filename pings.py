print '''
pings version 0.01
Pensando Panama Copyright 2013


This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''

# Enter host and amount of pings
import os
hostname = raw_input("Enter Host: ")
p = raw_input("Ping Amount: ")
response = os.system("ping -c %r " % p + hostname)

# Response up or down
if response == 0:
  print hostname, 'is up! amount of pings %s' % p
else:
  print hostname, 'is down!'
