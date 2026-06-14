# ipsecAssociationInit

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long ipsecAssociationInit(IP_Endpoint source, IP_Endpoint destination, char[] protocol, char[] mode, dword spi);
```

## Description

With this function it is possible to create a security association record. The record gets initialized with the given parameters.

A security association record is needed to modify the security association database of a network stack.

## Parameters

| Name | Description |
|---|---|
| source | Source endpoint of the security association. |
| destination | Destination endpoint of the security association. |
| UNSPEC | 0 |
| ESP | 1 |
| AH | 2 |
| ahalgorithm | sha |
| ahkey | 0123456789ABCDEF |
| espalgorithm | null |
| ahalgorithm | sha |
| ahkey | 0123456789ABCDEF |
| espalgorithm | none |
| ANY | 0 |
| TRANSPORT | 1 |
| TUNNEL | 2 |
| spi | The security parameter index of the security association. |

## Example

```c
on start
{
  long association;

  // create and init a security association record
  association = ipsecAssociationInit(ip_Endpoint(192.168.1.1), ip_Endpoint(192.168.1.10), "ah", "any", 30000);
  if(association < 0)
  {
    write("failed to create a security association");
  }
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
