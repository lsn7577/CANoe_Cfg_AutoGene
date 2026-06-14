# J1939TestWaitForAnyJoinedEvent, J1939TestWaitForAllJoinedEvents

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestWaitForAnyJoinedEvent( dword timeout )
long J1939TestWaitForAllJoinedEvents( dword timeout)
```

## Description

Waits for the actual set of "joined events". Each of this events can cancel the wait state or the wait condition will be canceled if all "joined events" are signaled. If no event occurred until the time of "timeout" the wait condition will be canceled.

## Parameters

| Name | Description |
|---|---|
| timeout | timeout in [ms] or 0 to disable |

## Example

```c
long lret;

J1939TestJoinPGEvent(10, 0xFF, 0xF123);
J1939TestJoinPGEvent(20, 0xFF, 0xF123);

lret = J1939TestWaitForAnyJoinedEvent ( 500 );
switch(lret) {
case 1:
  // first PG received
  break;
case 2:
  // second PG received
  break;
default:
  // error, timeout or constraint violation
  break;
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
