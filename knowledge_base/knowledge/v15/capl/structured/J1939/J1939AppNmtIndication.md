# J1939AppNmtIndication

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939AppNmtIndication( long busHandle, long address, long flag );
```

## Description

This function is called when an ECU claims n address or an ECU loses its address. The function is also called, if no ECU was created yet.

With J1939GetRxData() the device name can be copied to a buffer.

## Parameters

| Name | Description |
|---|---|
| busHandle | bus handle |
| address | address of the ECU or Null-Address |
| flag | reason for calling this function: 1: an ECU starts claiming, Address Claim PG received 2: successfully claimed, 250 ms after Address Claim PG 3: Cannot Claim Address received |

## Return Values

—

## Example

```c
dword J1939AppNmtIndication( LONG busHandle, LONG address, LONG flag )
{
  char deviceName[8];
  J1939GetRxData( elCount(deviceName), deviceName ); 
  /* user code */
  return 0; 
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | J1939 | J1939 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
