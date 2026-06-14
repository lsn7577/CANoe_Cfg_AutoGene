# CANopenDownloadDomain

> Category: `CANopen` | Type: `function`

## Syntax

```c
void CANopenDownloadDomain(dword nodeID, dword index, dword subIndex, dword dataSize, dword blockMode, dword errCode); // form 1
void CANopenDownloadDomain(SysVarName, dword dataSize, dword blockMode, dword[] errCode); // form 2
void CANopenDownloadDomain(char[] namespace, char[] variable, dword dataSize, dword blockMode, dword[]errCode); // form 3
void CANopenDownloadDomain(dword clientCOBID, dword serverCOBID, dword index, dword subIndex, dword dataSize, dword flags, dword[]errCode); // form 4
```

## Description

Writes an entry of type DOMAIN from the object dictionary of another node...

## Parameters

| Name | Description |
|---|---|
| nodeID | Node ID of the SDO server, i.e. the node that contains the object dictionary with the entry to be changed. Value range 1..127. |
| clientCOBID | CAN ID of the SDO client. |
| serverCOBID | CAN ID of the SDO server. |
| index | Index of the object, value range 1..65.535. |
| subIndex | Sub index of the object, value range 0..255. |
| dataSize | Size of the data in bytes. |
| blockMode | 0: Use expedited or segmented data transfer 1: Use block data transfer |
| errCode | Error code buffer (is entered in index 0 of the field): 0: Operation can be started 1: Operation already running 3: Invalid Client-COBID 4: Invalid Server-COBID 5: No CANopen license 6: No CAN channel |
| id | nodeId for form 1-3, serverCOBID for form 4. |
| abortCode | SDO abort code. |
| namespace | Name of the name space. |
| variable | Name of the CANopen system variable. |
| SysVarName | Name of the fully qualified name of the CANopen system variable, including all name spaces, separated by "::". The name must be preceded by "sysVar::". |
| payloadSize | Size of the payload in bytes. |
| payload | Data to be written. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | — | — | 5.0 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
