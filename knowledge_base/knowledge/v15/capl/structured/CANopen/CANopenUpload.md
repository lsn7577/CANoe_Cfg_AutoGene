# CANopenUpload

> Category: `CANopen` | Type: `function`

## Syntax

```c
void CANopenUpload( dword id, dword index, dword subIndex, dword blockMode, dword errCode[] ); // form 1
void CANopenUpload( dword clientCOBID, dword serverCOBID, dword index, dword subIndex, dword blockMode, dword errCode[] ); // form 2
void CANopenUpload( char[] namespace, char[] variable, dword blockMode, dword errCode[] ); // form 3
void CANopenUpload( SysVarName, dword blockMode, dword errCode[] ); // form 4
```

## Description

Reads an entry from the object dictionary of another node using the SDO protocol. When the node responds with the requested data, the callback OnCANopenUploadResponse is called. If the data transfer is aborted, the callback OnCANopenAbort is called.

## Parameters

| Name | Description |
|---|---|
| nodeID | CANopen node ID of the SDO server, i.e. the node that contains the object dictionary with the entry to be read. Value range 1..127 |
| id | nodeId for form 1, serverCOBID for form 2 |
| clientCOBID | CAN ID of the SDO client |
| serverCOBID | CAN ID of the SDO server |
| index | Index of the object, value range 1..65.535 |
| subIndex | Sub index of the object, value range 0..255 |
| size | Size of the data in bytes |
| blockMode | 0: Use expedited or segmented data transfer 1: Use block data transfer |
| errCode | Error code buffer (is entered in index 0 of the field) 0: Operation can be started 1: Operation already running 3: Invalid Client-COBID 4: Invalid Server-COBID 5: No CANopen license 6: No CAN channel |
| namespace | Name of the name space. |
| variable | Name of the CANopen system variable. |
| SysVarName | Name of the fully qualified name of the CANopen system variable, including all name spaces, separated by "::". The name must be preceded by "sysVar::". |

## Return Values

—

## Example

```c
dword errCode[1];
CANopenUpload ( 1, 0x1000, 0x00, 0, errCode );

if (errCode[0] == 0)
{
  write( "SDO Upload successfully initiated" );
}

void OnCANopenUploadResponse ( dword nodeId, dword index, dword subIndex, dword size 
{
  dword errCode[1];
  dword value;
  value = CANopenUploadGetUnsigned ( errCode );
  write( "Upload response data: 0x%X", value );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0: form 1, 2 12.0 SP3: form 2, 3 | 13.0 | — | — | 2.2: form 1, 2 4.0 SP3: form 3, 4 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
