# ipsecAssociationDatabaseAdd

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long ipsecAssociationDatabaseAdd(long association);
```

## Description

With this function it is possible to manually add a security association to the security association database of the current network stack.

A security association record can be created with ipsecAssociationInit or with ipsecAssociationDatabaseGetSpi.

## Parameters

| Name | Description |
|---|---|
| association | Handle to an security association record object. |

## Example

```c
on start
{
  long association;

  // create and init a security association record
  association = ipsecAssociationInit(ip_Endpoint(192.168.1.1), ip_Endpoint(192.168.1.10), "ah", "any", 30000);

  // add the security association to the security association database
  ipsecAssociationDatabaseAdd(association);

  // release the association record object when it isn't needed anymore
  ipsecAssociationRelease(association);
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
