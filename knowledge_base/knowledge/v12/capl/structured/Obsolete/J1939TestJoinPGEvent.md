# J1939TestJoinPGEvent

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long J1939TestJoinPGEvent( dword sourceAddr, dword destAddr, dword pgn, )
```

## Description

Completes the current set of "joined events" with the transmitted event. This function does not wait.

## Example

```c
long lret;

J1939TestJoinPGEvent(20, 0xFF, 0xF123);
J1939TestJoinPGEvent(10, 0xFF, 0xF123);

lret = J1939TestWaitForAnyJoinedEvent ( 500 );

switch(lret) {
case 1:
  // first PG received
  break;
case 2:
  // second PG received
  break;
default:
  // error, timeout or constrain violation
  break;
}
```

## Availability

| Up to Version |
|---|
