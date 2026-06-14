# _DoIP_EntityStatusResponse

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _DoIP_EntityStatusResponse( char IPaddress[], WORD port, BYTE nodeType, BYTE maxConcurrentTCPsockets, BYTE currentlyOpenTCPsockets, DWORD maxDataSize);
```

## Description

A response for an entity status request was received.

## Parameters

| Name | Description |
|---|---|
| IPaddress | Address in text form, e.g. “169.254.32.1” (IPv4) or “2001::1” (IPv6). |
| port | IP source port of the packet at the sender. |
| nodeType | Type of the node. Currently 0 for gateway and 1 for node are defined. |
| maxConcurrentTCPsockets | Maximum number of TCP connections the entity can handle simultaneously. |
| currentlyOpenTCPsockets | Number of TCP sockets currently open and in use. |
| maxDataSize | Maximum size of a diagnostics request this entity can process. Note: A value of 0 indicates that the response did not carry this optional parameter. |

## Return Values

—

## Example

```c
// Process an entity status response
void _DoIP_EntityStatusResponse( char IPaddress[], WORD port, BYTE nodeType, BYTE maxConcurrentTCPsockets, BYTE currentlyOpenTCPsockets, DWORD maxDataSize)
{
  write( "_DoIP_EntityStatusResponse( '%s', %d, %d, %d, %d, %d)",
  IPaddress, port, nodeType, maxConcurrentTCPsockets,
  currentlyOpenTCPsockets, maxDataSize);
  testSupplyTextEvent( cTE_EntityStatusRespInd);
}

Testcase TC_EntityStatus()
{
  DoIP_SendEntityStatusRequest();
  testWaitForTextEvent( cTE_EntityStatusRespInd, 500);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 | — | — | — | 2.1 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
