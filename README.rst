VzUbcMon
^^^^^^^^


About
=====
A simple monitor to regularly check for UBC failcount changes
in OpenVZ/Virtuozzo containers or on hardware nodes.
It's designed to run as a cronjob to mail the report to the admin
if there are any changes.


Requirements
============
A Virtuozzo/OpenVZ container or hardware node and Python (2.4).


Installation
============
Copy the source directory at a desired location in your filesystem,
e.g. /usr/local/vzubcmon.
Then copy the example crontab file from etc/cron.d/vzubcmon to
/etc/cron.d/vzubcmon and edit it to adjust the path.


Usage
=====
The tool is meant to be run as a cronjob, e.g. hourly.
If it finds any increments on any failcnt values in the
system's /proc/user_beancounters file, it prints a report
to its standard output which usually causes the cron daemon
to send a mail.

Alternatively, you can also run the script manually from the
command line, e.g.

# ./vzubcmon


License
=======
VzUbcMon is distributed under the terms of the GNU General Public License
as published by the Free Software Foundation; version 2 of the license.
A copy of this license can be found in the file COPYING included with
the source code of this program.


Ideas, questions, patches and bug reports
=========================================
Send them to me at enrico(dot)troeger(at)uvena(dot)de.
