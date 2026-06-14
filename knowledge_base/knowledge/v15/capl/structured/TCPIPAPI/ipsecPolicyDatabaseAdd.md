# ipsecPolicyDatabaseAdd

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long ipsecPolicyDatabaseAdd(IP_Endpoint source, dword sourcePrefix, IP_Endoint destination, dword destPrefix, char[] nextLayerProtocol, char[] policy);
```

## Description

With this function it is possible to manually add a ipsec policy to the security policy database of the current network stack. The network stack will check the selectors and if it finds a match the traffic will be handled with the given policy.

## Parameters

| Name | Description |
|---|---|
| source | The address and port of the source selector. |
| sourceFix | The prefix of the source selector. This defines which part of the address of the selector is relevant for filtering. |
| destination | The address and port of the destination selector. |
| destPrefix | The prefix of the destination sector. This defines which part of the address of the selector is relevant for filtering. |
| nextLayerProtocol | The upper layer protocol to be used. Can be one of the following protocols: IP_PROTO_ICMP IP_PROTO_TCP IP_PROTO_UDP IP_PROTO_ICMPv6 ANY |
| <direction> discard | This policy will discard all packets which fits the given selectors. |
| <direction> none | This policy will do nothing with the packets that fits the given selectors. |
| <direction>: in\|out | in: policy for incoming data out: policy for outgoing data |
| <protocol>: ah\|esp | ah: use authentication header esp: use encapsulating security payload |
| <mode>: tunnel\|transport | tunnel: use tunnel mode. This requires a next parameter of src-dst. transport: use transport mode. |
| [src-dst] | Is only given if the mode is tunnel src: source address of the tunnel dst: destination address of the tunnel |
| <level>: use\|require | use: use the given policy if a security association is available. Otherwise bypass IPsec. require: always use IPsec. Discard the packet if no security association for the current connection is available. |

## Example

```c
on start
{
  // bypass ipsec for outgoing packets from any address to the node with address 192.168.1.12 on port 23
  IpSecPolicyDatabaseAdd(ip_Endpoint(0.0.0.0:0), 0, ip_Endpoint(192.168.1.12:23), 32, "any", "out bypass");

  // discard all outgoing packets from any address to the node with address 192.168.1.13 with destination port 23
  IpSecPolicyDatabaseAdd(ip_Endpoint(0.0.0.0:0), 0, ip_Endpoint(192.168.1.13:23), 32, "any", "out discard");

  // Use ah in transport mode on outgoing packets from any address to the node with address 192.168.1.10 to destination port 23. Discard the packet if no security association is available.
  IpSecPolicyDatabaseAdd(ip_Endpoint(0.0.0.0:0), 0, ip_Endpoint(192.168.1.10:23), 32, "any", "out ipsec ah/transport//require");

  // Use esp in transport mode on outgoing packets from any address to the network 192.168.1.0/24 to destination port 21 if a security association is available.
  IpSecPolicyDatabaseAdd(ip_Endpoint(0.0.0.0:0), 0, ip_Endpoint(192.168.1.0:21), 24, "any", "out ipsec esp/transport//use");

  // Use esp in tunnel mode on outgoing packets from any address to the network 192.168.2.0/24 to destination port 22. The tunnel is between 192.168.1.1 and 192.168.2.5. Discar the packet if no security association is available.
  IpSecPolicyDatabaseAdd(ip_Endpoint(0.0.0.0:0), 0, ip_Endpoint(192.168.2.0:22), 24, "any", "out ipsec esp/tunnel/192.168.1.1-192.168.2.5/require");

  // Use ah in tunnel mode on outgoing packets from any address to the network 192.168.2.0/24 to destination port 24. The tunnel is between 192.168.1.1 and 192.168.1.5. Discar the packet if no security association is available.
  IpSecPolicyDatabaseAdd(ip_Endpoint(0.0.0.0:0), 0, ip_Endpoint(192.168.2.0:24), 24, "any", "out ipsec ah/tunnel/192.168.1.1-192.168.1.5/require");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 SP3 | — | — | — | 4.0 SP3 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
