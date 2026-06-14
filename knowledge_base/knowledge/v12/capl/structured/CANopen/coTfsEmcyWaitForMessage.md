# coTfsEmcyWaitForMessage

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsEmcyWaitForMessage( dword timeout );
```

## Description

This function waits until either a time-out occurs or an emergency message for the selected DUT Device Under Test is received.

## Return Values

0 = A time-out has occurred
1 = An emergency message was received

## Example

```c
if ( coTfsEmcyWaitForMessage( 5000 )== 1) {
  write("emergency message received");
}
else {
  write("time-out occurred");
}
```
