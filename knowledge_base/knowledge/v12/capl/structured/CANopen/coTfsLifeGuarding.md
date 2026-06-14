# coTfsLifeGuarding

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLifeGuarding( dword guardTime, dword retryFactor, dword tolerance );
```

## Description

The test sets the guard time and retry factor objects in the DUT Device Under Test. After that, 20 guarding remote frames are sent to the target device which must respond to all queries within the guardTime+tolerance.

Afterwards the sending of the remote frames is stopped. It is waited for the corresponding emergency message (EMCY code = 0x8130, Error Register = 0x11) before the values of the guard time and retry factor objects are reset.

## Return Values

Error code

## Example

```c
if ( coTfsLifeGuarding ( 500, 5, 50) != 1) {  // guard time, retry Factor, tolerance
  write("lifeguarding failed");
}
```
