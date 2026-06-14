# J1939TestRequestACL

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestRequestACL( dword requestSA, dbNode aclSender, dword timeout, dword options )
```

## Description

A request for ACL is sent. The configured node must respond with the ACL message (0xEE00).

## Parameters

| Name | Description |
|---|---|
| requestSA | the request is sent from this source address |
| aclSender | send node from database, optional |
| timeout | timeout in [ms] |
| options | Bit 1: specific request Bit 2: not configured nodes are allowed to send ACL Bit 3: node may use another address than defined in NmStationAddress |

## Example

```c
long result;
result = J1939TestRequestACL( 254, EMS, 250, 0x00 );

if (result == 1) {
  TestStepPass( "ACL received" );
}
else if (result == 0) {
  TestStepFail( “Timeout, ACL message not receive” );
}
else {  
  TestStepFail( “Error during Request for ACL test“);
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
