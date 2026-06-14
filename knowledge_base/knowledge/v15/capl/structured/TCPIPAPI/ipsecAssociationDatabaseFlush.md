# ipsecAssociationDatabaseFlush

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long ipsecAssociationDatabaseFlush(char[] protocol);
```

## Description

With this function it is possible to manually delete all security associations of the same protocol type from the security association database of the current network stack.

## Parameters

| Name | Description |
|---|---|
| UNSPEC | 0 |
| ESP | 1 |
| AH | 2 |

## Example

```c
void CleanSecurityAssociationDatabase()
{
  // clean the security association database
  IPsecAssociationDatabaseFlush("ah");
  IPsecAssociationDatabaseFlush("esp");
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
