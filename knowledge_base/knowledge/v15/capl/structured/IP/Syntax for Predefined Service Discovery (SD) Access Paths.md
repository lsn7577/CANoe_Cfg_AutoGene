# Syntax for Predefined Service Discovery (SD) Access Paths

> Category: `IP` | Type: `notes`

## Description

SomeIpSetValueDWord(msg, "Entry[9].FindService.ServiceID", 0x000A);

DWORD evgID = SomeIpGetValueDWord(msg, "Entry[0].SubscribeAck.EventgroupID");

SomeIpSetValueString(msg, "Option[2].Configuration.String[1]", "def=123");

DWORD prio = SomeIpGetValueDWord(msg, "Option[5].LoadBalancing.Priority");

DWORD res = SomeIpGetValueDWord(msg, "Option[0].Protection.Reserved");

SomeIpSetValueDWord(msg, "Option[0].IPv4Endpoint.PortNumber", 30490);

DWORD prot = SomeIpGetValueDWord(msg, "Option[4].IPv6Endpoint.L4Proto");

SomeIpSetValueDWord(msg, "Option[0].IPv4Multicast.PortNumber", 30490);

SomeIpSetValueDWord(msg, "Option[6].IPv6Multicast.IPv6Address[9]", 0xFE);

| Example |  |
|---|---|
| Flags | SomeIpSetValueDWord(msg, "Flags", 0xC0); //set reboot (0x80) and unicast (0x40) flag |
| Reserved | SomeIpSetValueDWord(msg, "Reserved", 0x00); |

| Type | Member | Example |  |
|---|---|---|---|
| Entry[n] | FindService OfferService RequestService RequestServiceAck | Index1stOptions | SomeIpSetValueDWord(msg, "Entry[9].FindService.ServiceID", 0x000A); |
| Index2ndOptions |  |  |  |
| NumberOfOptions1 |  |  |  |
| NumberOfOptions2 |  |  |  |
| ServiceID |  |  |  |
| InstanceID |  |  |  |
| MajorVersion |  |  |  |
| TTL |  |  |  |
| MinorVersion |  |  |  |
| FindEventgroup Publish Subscribe SubscribeAck | Index1stOptions | DWORD evgID = SomeIpGetValueDWord(msg, "Entry[0].SubscribeAck.EventgroupID"); |  |
| Index2ndOptions |  |  |  |
| NumberOfOptions1 |  |  |  |
| NumberOfOptions2 |  |  |  |
| ServiceID |  |  |  |
| InstanceID |  |  |  |
| MajorVersion |  |  |  |
| TTL |  |  |  |
| Reserved |  |  |  |
| EventgroupID |  |  |  |
| Option[n] | Configuration | Reserved | SomeIpSetValueString(msg, "Option[2].Configuration.String[1]", "def=123"); |
| String[n] |  |  |  |
| LoadBalancing | Reserved | DWORD prio = SomeIpGetValueDWord(msg, "Option[5].LoadBalancing.Priority"); |  |
| Priority |  |  |  |
| Weight |  |  |  |
| Protection | Reserved | DWORD res = SomeIpGetValueDWord(msg, "Option[0].Protection.Reserved"); |  |
| ID |  |  |  |
| AliveCounter |  |  |  |
| CRC |  |  |  |
| IPv4Endpoint | Reserved | SomeIpSetValueDWord(msg, "Option[0].IPv4Endpoint.PortNumber", 30490); |  |
| IPv4Address |  |  |  |
| Reserved_2 |  |  |  |
| L4Proto |  |  |  |
| PortNumber |  |  |  |
| IPv6Endpoint | Reserved | DWORD prot = SomeIpGetValueDWord(msg, "Option[4].IPv6Endpoint.L4Proto"); |  |
| IPv6Address[16] |  |  |  |
| Reserved_2 |  |  |  |
| L4Proto |  |  |  |
| PortNumber |  |  |  |
| IPv4Multicast | Reserved | SomeIpSetValueDWord(msg, "Option[0].IPv4Multicast.PortNumber", 30490); |  |
| IPv4Address |  |  |  |
| Reserved_2 |  |  |  |
| L4Proto |  |  |  |
| PortNumber |  |  |  |
| IPv6Multicast | Reserved | SomeIpSetValueDWord(msg, "Option[6].IPv6Multicast.IPv6Address[9]", 0xFE); |  |
| IPv6Address[16] |  |  |  |
| Reserved_2 |  |  |  |
| L4Proto |  |  |  |
| PortNumber |  |  |  |

| Example void OnSomeIpMessage( dword messageHandle ){ DWORD nbrOfEntries; BYTE i; CHAR valuePath[255]; DWORD entryType; DWORD nbrOfOptions; DWORD optionType; if(SomeIpGetMessageId(messageHandle) == 0xFFFF8100) { nbrOfEntries = SomeIpGetValueDWord(messageHandle, "Entry"); for(i=0; i<nbrOfEntries; i++) { snprintf(valuePath, elCount(valuePath), "Entry[%d]", i); entryType = SomeIpGetValueDWord(messageHandle, valuePath); switch(entryType) { case 0x00 /*FindService*/: snprintf(valuePath, elCount(valuePath), "Entry[%d].FindService.ServiceID", i); write("FindService with ServiceID %d", SomeIpGetValueDWord(messageHandle, valuePath)); break; case 0x01 /*OfferService*/: snprintf(valuePath, elCount(valuePath), "Entry[%d].OfferService.ServiceID", i); write("OfferService with ServiceID %d", SomeIpGetValueDWord(messageHandle, valuePath)); break; case 0x06 /*Subscribe*/: snprintf(valuePath, elCount(valuePath), "Entry[%d].Subscribe.EventgroupID", i); write("Subscribe with EventgroupID %d", SomeIpGetValueDWord(messageHandle, valuePath)); break; case 0x07 /*SubscribeAck*/: snprintf(valuePath, elCount(valuePath), "Entry[%d].SubscribeAck.EventgroupID", i); write("SubscribeAck with EventgroupID %d", SomeIpGetValueDWord(messageHandle, valuePath)); break; } } nbrOfOptions = SomeIpGetValueDWord(messageHandle, "Option"); for(i=0; i<nbrOfOptions; i++) { snprintf(valuePath, elCount(valuePath), "Option[%d]", i); optionType = SomeIpGetValueDWord(messageHandle, valuePath); switch(optionType) { case 0x01 /*Configuration*/: snprintf(valuePath, elCount(valuePath), "Option[%d].Configuration.String[1]", i); write("Configuration with String[1] %s", SomeIpGetValueDWord(messageHandle, valuePath)); break; case 0x02 /*LoadBalancing*/: snprintf(valuePath, elCount(valuePath), "Option[%d].LoadBalancing.Priority", i); write("LoadBalancing with Priority %d", SomeIpGetValueDWord(messageHandle, valuePath)); break; case 0x03 /*Protection*/: snprintf(valuePath, elCount(valuePath), "Option[%d].Protection.ID", i); write("Protection with ID %d", SomeIpGetValueDWord(messageHandle, valuePath)); break; case 0x04 /*IPv4Endpoint*/: snprintf(valuePath, elCount(valuePath), "Option[%d].IPv4Endpoint.PortNumber", i); write("IPv4Endpoint with PortNumber %d", SomeIpGetValueDWord(messageHandle, valuePath)); break; case 0x06 /*IPv6Endpoint*/: snprintf(valuePath, elCount(valuePath), "Option[%d].IPv6Endpoint.PortNumber", i); write("IPv6Endpoint with PortNumber %d", SomeIpGetValueDWord(messageHandle, valuePath)); break; case 0x14 /*IPv4Multicast*/: snprintf(valuePath, elCount(valuePath), "Option[%d].IPv4Multicast.PortNumber", i); write("IPv4Multicast with PortNumber %d", SomeIpGetValueDWord(messageHandle, valuePath)); break; case 0x16 /*IPv6Multicast*/: snprintf(valuePath, elCount(valuePath), "Option[%d].IPv6Multicast.PortNumber", i); write("IPv6Multicast with PortNumber %d", SomeIpGetValueDWord(messageHandle, valuePath)); break; } } }} |
|---|

| Version 15© Vector Informatik GmbH |
|---|
