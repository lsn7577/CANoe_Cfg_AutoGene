# ipsecPolicyDatabaseDelete

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long ipsecPolicyDatabaseDelete(IP_Endpoint source, dword srcPrefix, IP_Endoint destination, dword destPrefix, char[] nextLayerProtocol, char[] policy);
```

## Description

With this function it is possible to manually delete a single ipsec policy from the security policy database of the current network stack. The policy to delete is defined by its selectors and the direction (incoming or outgoing).

## Parameters

| Name | Description |
|---|---|
| source | The address and port of the source selector. |
| sourceFix | The prefix of the source selector. |
| destination | The address and port of the destination selector. |
| destPrefix | The prefix of the destination sector. |
| nextLayerProtocol | The upper layer protocol to be used. Can be one of the following protocols: IP_PROTO_ICMP IP_PROTO_TCP IP_PROTO_UDP IP_PROTO_ICMPv6 ANY |
| policy | in: delete a incoming policy out: delete a outgoing policy |

## Example

```c
on start
{
  // delete the outgoing policy from any address to port 21 on the network 192.168.1.0/24
  IPsecPolicyDatabaseDelete(ip_Endpoint(0.0.0.0:0), 0, ip_Endpoint(192.168.1.0:21), 24, "any", "out");
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
