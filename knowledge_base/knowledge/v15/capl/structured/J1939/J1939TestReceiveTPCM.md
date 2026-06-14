# J1939TestReceiveTPCM

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestReceiveTPCM_RTS( pg rxBuffer, dword rxBufferSize, dword da, pg tpcmBuffer, dword tpcmBufferSize, dword timeout, dword options )
long J1939TestReceiveTPCM_Data( pg rxBuffer, dword rxBufferSize, dword da, pg tpcmBuffer, dword tpcmBufferSize, dword delay, dword waitPackets, dword timeout, dword options )
long J1939TestReceiveTPCM_Abort( pg rxBuffer, dword rxBufferSize, dword da, dword options )
```

## Description

With this function receiving of a message with the RTS/CTS transport protocol can be influenced. It can created errors during transmission, i.e. violate time distances or wrong sequence numbers.

First the function J1939TestReceiveTPCM_RTS must be called to wait for the RTS message. The DUT must be triggered to send a RTS/CTS transmission, i.e. with a request.

After that the function J1939TestReceiveTPCM_Data must be used to send a CTS message and wait for a number of data messages (TPDT). The received data is copied to rxBuffer. In the tpcmBuffer, the data for the next CTS message is copied. The function J1939TestReceiveTPCM_Data can be called until the result 2 is returned and the EoMA message was sent.

Before calling J1939TestReceiveTPCM_Data the tpcmBuffer can be modified and i.e. the another sequence number can be requested.

## Parameters

| Name | Description |
|---|---|
| rxBufferSize | size of the receive buffer in bytes |
| rxBuffer | receive buffer The received message is copied into this buffer. The buffer must be big enough. |
| da | destination address for the RTS transmission |
| tpcmBufferSize | size of the buffer for the TPCM message, must be 8 |
| tpcmBuffer | buffer for the TPCM message The CTS message is copied into this buffer. The data from this buffer is used when sending a CTS message. Afterwards the buffer contains the data of the next CTS message. |
| delay | delay before sending CTS, EoMA or Abort message in [ms] |
| waitPackets | wait until this number of packets is received |
| timeout | timeout for response in [ms] |
| options | Bit 0 = 1 receive every RTS/CTS Transmisison, else receive only the PGN of rxBuffer |

## Example

```c
pg EC1  rxMsg = { DLC=38 };
pg TPCM tpcm;
LONG result;

// send Request for EC1 to DUT, but do not wait for response
J1939TestRequest( EC1, Tester, EMS, 0, 0 );

// wait for RTS from DUT
result = J1939TestReceiveTPCM_RTS( rxMsg, 38, 10, tpcm, 8, 1250, 0x00 );

// send CTS and wait for data, if all packets are receive send EoMA
while (result == 1) {
  result = J1939TestReceiveRTS_Data( rxMsg, 36, 10, tpcm, 8, 5, 16, 250, 0x00 );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 | 13.0 | — | — | 1.1 SP2 |
| Restricted To | — | J1939 | J1939 | — | — | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
