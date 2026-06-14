# Socket Options: IPPROTO_IP

> Category: `TCPIPAPI` | Type: `notes`

## Description

The following socket options can be set at the IPPROTO_IPV6 socket option level in CAPL. They influence the behavior of the IPv6 protocol per socket. For all BOOL typed options a non-zero value will be interpreted as TRUE.

See Also

| Socket Option | Set/Get | Description | Type | Stack |
|---|---|---|---|---|
| IPV6_UNICAST_HOPS | set/get | Set or get the value of the hoplimit field in the IPv6 header in outgoing unicast packets on this socket. The value has to be in the range from 0-255. On the CANoe internal TCP/IP stack a value of -1 indicates that the stack will use a default value. | LONG | C/W |
| IPV6_MULTICAST_IF | set/get | Set or get the interface for outgoing IPv6 multicast traffic. | DWORD | C/W |
| IPV6_MULTICAST_HOPS | set/get | Set or get the value of the hoplimit field in the IPv6 header in outgoing multicast packets. The value has to be in the range from 0-255. | DWORD | C/W |
| IPV6_MULTICAST_LOOP | set/get | This option controls whether multicast data will be received by a listening socket joined the same multicast group when it is send on the same node. | DWORD (boolean) | C/W |
| IPV6_V6ONLY | set/get | If this option is set to 1 the socket is restricted to IPv6 traffic only (default). If the option is set to 0 a socket created for the AF_INET6 address family may be used also for IPv4. For instance a AF_INET6 wildcard listening socket will accept IPv4 traffic as well as it was from a IPv4 mapped address. Note that in this case even if there is no IPv4 listening socket on a port open the traffic to this port will be accepted from the IPv6 socket. | DWORD (boolean) | C/W |
| IPV6_PORTRANGE | set/get | Select the range which is used for the unspecified port. The following values are supported: IP_PORTRANGE_DEFAULT (0) IP_PORTRANGE_HIGH (1) IP_PORTRANGE_LOW (2) | DWORD | C |
| IPV6_USE_MIN_MTU | set/get | Configure whether the minimal IPv6 maximum transmission unit (MTU) will be used to avoid fragmentation on sending datagrams. Possible values are: -1: multicast datagrams use the minimal IPv6 MTU, unicast datagrams not. 0: neither multicast datagrams nor unicast datagrams are limited to the minimal IPv6 MTU 1: both multicast and unicast datagrams are limited to the minimal IPv6 MTU | DWORD | C |
| IPV6_TCLASS | set/get | Set the value of the traffic class field in the IPv6 header. | DWORD (boolean) | C |
| IPV6_DONTFRAG | set/get | If set TRUE the data will not be fragmented anymore. | DWORD (boolean) | C |
| IPV6_BINDANY | set/get | It is possible to bind to any address , even one that is not bound to any interface when this option is set to a nonzero value. | DWORD (boolean) | C |

| Version 15© Vector Informatik GmbH |
|---|
