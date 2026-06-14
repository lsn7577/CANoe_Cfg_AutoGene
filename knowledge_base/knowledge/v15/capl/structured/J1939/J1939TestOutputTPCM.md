# J1939TestOutputTPCM

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestOutputTPCM_RTS( pg txMsg, dword da, dword maxPacketsPerCTS, pg tpcmBuffer, dword tpcmBufferSize, dword timeout, dword options, [dword optionsArg] )
long J1939TestOutputTPCM_Data( pg txMsg, dword da, dword maxPacketsPerCTS, pg tpcmBuffer, dword tpcmBufferSize, dword delay, dword timeout, dword options )
long J1939TestOutputTPCM_Abort( pg txMsg, dword da, dword abortReason, dword options )
```

## Description

With this function the transmission of a message with the RTS/CTS transport protocol influenced. It can created errors during transmission, i.e. violate time distances or wrong sequence numbers.

First the transmission must be started with J1939TestOutputTPCM_RTS. Then the function J1939TestOutputTPCM_Data can be called until the result is 2 and the transmission was completed with EoMA.

Before calling J1939TestOutputTPCM_Data the tpcmBuffer can be modified and i.e. a wrong message number can be created.

## Parameters

| Name | Description |
|---|---|
| txMsg | send this parameter group with the RTS/CTS protocol |
| da | destination address |
| delay | delay between data messages (TPDT) in [ms] |
| timeout | timeout for CTS or EoMA response in [ms] |
| maxPacketsPerCTS | number of data messages, which can be requested by CTS |
| tpcmBufferSize | size of the CTS buffer (sould be 8) |
| tpcmBuffer | buffer for the tpcm message The received CTS message is copied into this buffer. When sending data messages, next sequence number and number of packets are taken from this buffer. |
| abortReason | Reason for abort 1: No connection free 2: No resources free 3: Timeout 255: No reason |
| options | Bit 1: Use optionsArg as Number of Packets in RTS |
| optionsArg | additional parameter, depends on options, optional |

## Example

Example 1

Example 2

```c
pg EC1 txMsg = { DLC=38 };
pg TPCM cts;
LONG result;

// send RTS and wait for first CTS
result = J1939TestOutputTPCM_RTS( txMsg, 10, 16, cts, 8, 1250, 0x00);

// send data while DUT request more data with CTS
while (result == 1) {
  result = J1939TestOutputTPCM_Data( txMsg, 10, 16, cts, 8, 20, 100, 0x00);
}
pg EC1 txMsg = { DLC=38 };
pg TPCM cts;
LONG result;

// send RTS and wait for first CTS
result = J1939TestOutputTPCM_RTS( txMsg, 234, 16, cts, 8, 1250, 0x00  );

// send data with wrong sequence number
cts.NextPacketNumberToBeSent = 2;
result = J1939TestOutputTPCM_Data( txMsg, 234, 10, cts, 8, 25, 100, 0x00 );

// DUT must send Abort
if (result != 3) {
  TestStepFail( “DUT has not sent Abort” );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 | 13.0 | — | — | — |
| Restricted To | — | J1939 | J1939 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
