# KLine_SendFrame

> Category: `KLine` | Type: `function`

## Syntax

```c
long KLine_SendFrame( byte data[], dword count)
```

## Description

Send data on the active K-Line communication channel.

The K-Line header is generated automatically due to header settings.

## Parameters

| Name | Description |
|---|---|
| data | Data buffer |
| dword count | Length of data buffer |

## Return Values

On success 0, otherwise a value less than 0.

## Example

```c
_Diag_DataRequest( BYTE data[], dword count, long furtherSegments)
{
   long status;
   status = KLine_SendFrame( data, count);
   write( "KLine_SendFrame returns %d for sending %d bytes", status, count);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 SP4 | — | — | — | 1.1 SP2 |
| Restricted To | — | K-Line Real bus mode Online mode ECU simulation | — | — | — | K-Line Real bus mode Online mode ECU simulation |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
