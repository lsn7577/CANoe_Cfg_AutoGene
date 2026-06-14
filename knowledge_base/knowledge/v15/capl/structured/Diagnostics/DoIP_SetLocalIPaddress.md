# DoIP_SetLocalIPaddress

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DoIP_SetLocalIPaddress(char ipAddress[]);
```

## Description

Set local IP address to bind to. In an ECU simulation, Vehicle Announcement Messages (VAM) will be sent from this IP address, in a tester node the Vehicle Identification Request (VIR) messages. If the tester node sets IP address in on prestart, it can receive VAMs even before it sends VIR messages itself. The target IP address is derived from this IP address: for an IPv4 address the broad-cast address is determined using the network mask, for an IPv6 address the multicast address is used.

## Parameters

| Name | Description |
|---|---|
| ipAddress | Textual representation of the IP address to bind to, e.g. 192.169.2.22 for an IPv4 address, or 2001::1234 for an IPv6 address. An empty string may be given to reset the stored address, e.g. if the address of an adapter shall be retrieved in a later step. |

## Example

```c
DoIP_SetLocalIPaddress( "10.10.10.222"); // Set an IPv4 address
...
DoIP_SetLocalIPaddress( "2001::2222");   // Set an IPv6 address
...
// retrieve the IP address configured for this simulation node's TCP/IP stack
ipGetAdapterAddressAsString( 1, localAddr, elcount(localAddr));
// and use it as local address
DoIP_SetLocalIPaddress( localAddr);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP4 | — | — | — | 2.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
