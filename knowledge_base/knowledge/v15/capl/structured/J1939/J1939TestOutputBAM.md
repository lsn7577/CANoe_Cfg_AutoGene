# J1939TestOutputBAM

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestOutputBAM( pg txMsg, dword seqNum, dword seqCount, dword delay, [dword options], [dword optionArg] )
```

## Description

With this function the transmission of a message with the BAM transport protocol is influenced. It can created errors during transmission, i.e. violate time distances or wrong sequence numbers.

## Parameters

| Name | Description |
|---|---|
| txMsg | send this parameter group with BAM |
| seqNum | start with this sequence number, number 0 is the BAM message |
| seqCount | number of messages to send |
| delay | delay between messages [ms] |
| options | optional Bit 0: Do not wait after last message Bit 1: Use number of packets for BAM message from optionArg |
| optionArg | depends on options, optional |

## Example

```c
pg EC1 txMsg = { DLC=38 };

// send BAM and first Data message
J1939TestOutputBAM( txMsg, 0, 2, 50 );

// send Data message, Seq. 2
J1939TestOutputBAM( txMsg, 2, 1, 350 );

// the DUT should detect, that the time between Seq 2 and Seq 3 is more than 200ms 
// send Data message, Seq. 3 to 6
J1939TestOutputBAM( txMsg, 3, 4, 50 );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 | 13.0 | — | — | 1.1 SP2 |
| Restricted To | — | J1939 | J1939 | — | — | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
