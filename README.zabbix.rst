VzUbcMon and Zabbix
^^^^^^^^^^^^^^^^^^^


``VzUbcMon`` can be used together with Zabbix for efficiently monitoring
a OpenVZ hardware node.

In the contrib subdirectory a little helper utility can be found to
read ``/proc/user_beancounters`` as unprivileged ``zabbix`` user and also
a template for the Zabbix server with an item and trigger to create events
once any failcount of a container on the node increased.

``VzUbcMon`` is directly started from the Zabbix agent every five minutes
(default update interval for the item) and either simply returns 'ok'
to the Zabbix server in case no failcounts increased since the last
check or it returns a descriptive text with information about the containers
and the UBC information of each increased failcount.

Using strings as output for monitoring seems unfitting but it allows
to monitor the UBC failcounts for all containers of a hardware nodes
with one single check which is way more efficiently than using multiple
items for the various UBCs. And since we return just a string we can include
all necessary information for the admin to get informed properly.
The trigger on the Zabbix server gets active once the item won't return
'ok' and then puts the output of the check into the trigger's description.


Setup
=====

Hardware Node
-------------

Get the code::

    # git clone git://github.com/eht16/vzubcmon /usr/local/vzubcmon


Then compile the tool readubc.c in the contrib
subdirectory and install it somewhere on the system, e.g.
``/etc/zabbix/vzubcmon/readubc``. ``readubc`` should have the setuid bit set
and be owned by the zabbix user::

    # make
    # mkdir /etc/zabbix/vzubcmon
    # cp readubc /etc/zabbix/vzubcmon/
    # chown root:zabbix /etc/zabbix/vzubcmon/readubc
    # chmod u+s /etc/zabbix/vzubcmon/readubc


Now configure the Zabbix agent to use ``readubc`` and ``VzUbcMon``.
Add the following line into your agent configuration::

    UserParameter=openvz.ubc,/etc/zabbix/vzubcmon/readubc|python /usr/local/vzubcmon/vzubcmon --okmsg --database /etc/zabbix/vzubcmon/vzubcmon.pck --ubc -

(don't forget to adjust paths as needed and restart the agent)
This will add the item ``openvz.ubc`` to your agent which then pipes the output
of ``readubc`` to ``VzUbcMon`` and passes the result to the Zabbix server.

``--okmsg`` tells ``VzUbcMon`` to print 'ok' if there are no changes which is
necessary for the Zabbix trigger. ``--ubc -`` specifies that the UBC input
data is read from standard input instead of a regular file.


Zabbix Server
-------------

Import the simple template in the contrib subdirectory and link your OpenVZ
hardware node(s) to the template to start monitoring.

That's it. Now your node(s) are monitored for increasing UBC failcounts of
all containers and in case any UBC failcount change, an event will inform
you about the container, the UBC and the failcount which increased.


Happy monitoring.
