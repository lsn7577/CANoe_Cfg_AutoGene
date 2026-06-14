# DoIP_SetBroadcastIPaddress

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetBroadcastIPaddress(char broadcastAddress[]);
```

## Description

Sets target IP address for broadcast messages sent from this node.

## Parameters

| Name | Description |
|---|---|
| broadcastAddress | 255.255.255.255: send a limited broadcast (default if IPv4 is active) "" (empty string): send a directed broadcast, deriving address from local IPv4 address other: if this is a valid string representation of an IP address, send to this address, e.g. a broadcast directed to a different network, or an IPv6 multicast address |

## Return Values

—

## Example

```c
DoIP_SetLocalIPaddress( "192.168.1.123”);
if( sendDirectedBroadcast)
  DoIP_SetBroadcastIPaddress( ""); // send to 192.168.1.255
else if( sendToOtherNetwork)
  DoIP_SetBroadcastIPaddress( "192.168.5.255"); // send to 192.168.5.255
else // restore default
  DoIP_SetBroadcastIPaddress( "255.255.255.255"); // limited broadcast
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.5 SP3 | — | — | — | 2.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
