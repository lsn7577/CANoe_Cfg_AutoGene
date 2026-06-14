# AfdxSetSignalString

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxSetSignalString( long packet, char signalName[], char value[], long fdsStatus ); // form 1
long AfdxSetSignalString( long packet, long offset, char value[] ); // form 2
```

## Description

This function sets the value of an AFDX string signal. The AFDX string structure consists of a 16-bit length code n and a sequence of n ASCII characters. The length code is updated too.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the message. |
| signalName | Name of the signal. Note: The signal and its message need to be defined in the assigned DBC file. |
| offset | The offset value points to the starting byte of the AFDX string. |
| value | New ASCII string value. |
| fdsStatus | 255: The status is not updated valid status enumeration: The functional status is updated with this value. |

## Example

```c
long packet;
long msgID = 0x1A112B73;

// create a new AFDX packet as defined in the DBC with this msgID
packet = AfdxInitPacket( msgID, NULL, 0 );

// set integer signal 1 to 78 degrees, don’t change status byte
AfdxSetSignalInt( packet, "VFG_OIL_TEMP_A_34", 78 );

// set float-signal 2 to 52 degree, set corresponding status to <NO>
AfdxSetSignalReal( packet, "VFG_OIL_TEMP_AB_32", 52, 3 );

// set boolean signal 3 to 1, set corresponding status to <NO>
AfdxSetSignalBool( packet, "VFG_OIL_TEMP_A_ON", 1, 3 );

// set enumeration signal 4 to 5, don’t change status byte
AfdxSetSignalInt( packet, “FLIGHT_GROUND_COND_3", 5 );

// set string signal 6 to hello, don’t change status byte
AfdxSetSignalString( packet, “TEST_STRING14_CITY", “hello” );

// set opaque signal 7 to 0x31,0x32,0x33, don’t change status byte
AfdxSetSignalOpaque( packet, “TEST_OPAQUE14_IDENT", 3, “123” );

AfdxOutputPacket( packet );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 SP3: form 1, 2 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
