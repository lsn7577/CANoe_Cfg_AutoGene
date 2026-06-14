# AfdxGetSignalReal

> Category: `ADFX` | Type: `function`

## Syntax

```c
float AfdxGetSignalReal( long packet, char signalName[] ); // form 1
float AfdxGetSignalReal( long packet, long offset, long isDouble ); // form 2
```

## Description

This function returns the value of a 32-bit or 64-bit float signal (IEEE 754) in a 64-bit float value.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the message. |
| signalName | Name of the signal. Note: The signal and its message need to be defined in the assigned DBC file. |
| offset | The offset value points to the starting byte of the float value in the AFDX payload area. |
| isDouble | 0: get 32-bit float value 1: get 64-bit float value |

## Return Values

Signal value (call AfdxGetLastErrror to check for errors in the call).

## Example

Analyze signals from an incoming AFDX packet using DBC information

```c
on preStart
{
  AfdxRegisterReceiveCallback("OnPacket");
}
void OnPacket( long dir, long line, int64 timestamp, long bag, long afdxFlags, long packet )
{
  long lVal=0; // integer signal
  long eVal=0; // enumeration signal
  long bVal=0; // boolean signal
  double rVal = 0.0; // float signal
  char sVal[16]; // string signal
  byte oVal[16]; // opaque signal
  long len, status, err;
  long msgID;
  char msgName[256];

  // get message ID of this message
  msgID = AfdxGetMessageId( packet );

  // get message name of this message
  err = AfdxGetMessageName( packet, 256, msgName );

  // get signal status
  status = AfdxGetSignalStatus( packet, "VFG_OIL_TEMP_A_34" );

  // get integer signal
  lVal = AfdxGetSignalInt( packet, "VFG_OIL_TEMP_A_34" );

  // get float-signal 2
  rVal = AfdxGetSignalReal( packet, "VFG_OIL_TEMP_AB_32" );

  // get boolean signal 3
  bVal = AfdxGetSignalBool( packet, "VFG_OIL_TEMP_A_ON" );

  // get enumeration signal 4
  eVal = AfdxGetSignalInt( packet, “FLIGHT_GROUND_COND_3" );

  // get string signal 6
  len = AfdxGetSignalString( packet, “TEST_STRING14_CITY", 16, sVal );

  // get opaque signal 7
  len = AfdxGetSignalOpaque( packet, “TEST_OPAQUE14_IDENT", 16, oVal );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 SP3 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
