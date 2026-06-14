# J1939TestWaitForAnyJoinedEvent, J1939TestWaitForAllJoinedEvents

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestWaitForAnyJoinedEvent( dword timeout )
```

## Description

Waits for the actual set of "joined events". Each of this events can cancel the wait state or the wait condition will be canceled if all "joined events" are signaled. If no event occurred until the time of "timeout" the wait condition will be canceled.

If function J1939TestJoinPG is used this function must be used to wait. The function TestWaitForAllJoinedEvents must not be used in this case!

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

| Since Version |
|---|
