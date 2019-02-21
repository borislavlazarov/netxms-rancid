To execute use:
java -Dnetxms.server=<NETXMSIP> -Dnetxms.login=<USERNAME> -Dnetxms.password=<PASSWORD> -jar /opt/netxms_integration/nxshell-2.2.12.jar /opt/netxms_integration/netxms-export.nxsh <customer_group_name> [debug] 2>/dev/null

this will dump two files in the current directory:
1. router.db for RANCID to use
2. router.db.fromnetxms.unknown with a list of devices that failed to import because there is no match for their rancid type
