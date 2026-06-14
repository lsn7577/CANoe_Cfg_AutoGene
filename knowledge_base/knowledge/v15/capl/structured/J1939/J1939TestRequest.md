# J1939TestRequest

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestRequest( dword rqPGN, dword reqSA, dword respSA, dword timeout, dword options )
long J1939TestRequest( dbMsg msg, dword reqSA, dword respSA, dword timeout, dword options )
long J1939TestRequest( dbMsg msg, dbNode reqNode, dbNode respNode, dword timeout, dword options)
long J1939TestRequest( pg msgBuffer, dword maxRespSize, dword reqSA, dword respSA, dword timeout, dword options )
long J1939TestRequest( pg msgBuffer, dword maxRespSize, dbNode reqNode, dbNode respNode, dword timeout, dword options )
```

## Description

Sends a request from the address reqSA, then wait until the response is received. Within the time interval (timeout) the response or an acknowledgment must be received.

If the requested parameter group is received, the data is copied into the buffer (msgBuffer). The test module can verify the values in this buffer.

If a response is sent with the RTS/CTS transport protocol, with Bit 2 in options sending of CTS and EoMA can be activated

## Parameters

| Name | Description |
|---|---|
| rqPGN | request this PGN |
| msg | message from database |
| msgBuffer | PG variable, the response is copied into this bufferIf the answer is an acknowledge message, the buffer is left untouched. Please use TestGetWaitJ1939PGData to query the information. |
| maxRespSize | size of buffer for response |
| reqSA | source address for request, 0..253 |
| respSA | source address of the response 0..253, with global requests the source address can be ignored by using 0xFE |
| reqNode | database node, which sends the request |
| respNode | database node, which sends the response |
| timeout | timeout in [ms] (If this value is not set, it is not waited for the response.) |
| Bit 1 | 1: global request (DA=255) 0: specific request (DA=respAddr) |
| Bit 2 | 1: enable CTS and EoMA for reqSA 0: no RTS/CTS support |

## Example

```c
pg EC1 rxPG;

if (J1939TestRequest( EC1, Tester, EMS, 250, 0x00 ) != 0) {
  testFail( “EC1 not received after request” );
}

if (J1939TestRequest( rxPG, Tester, EMS, 250, 0x00 ) == 0) {
  if (rxPG.AnyValue.phys > 100.0) {
    testStepFail( “EC1.AnyValue hast wrong value” );
  }
}
else {  
  testStepFail( “EC1 not received after request” );
}
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
