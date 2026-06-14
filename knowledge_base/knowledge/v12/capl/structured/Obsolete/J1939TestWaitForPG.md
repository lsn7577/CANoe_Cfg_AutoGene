# J1939TestWaitForPG

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long J1939TestWaitForPG( dword sourceAddr, dword destAddr, dword pgn, dword timeout )
```

## Description

Wait until the specified parameter group is received.

## Example

```c
long lret;
lret = J1939TestWaitForPG(10, 0xFF, 0xF123, 500 );

switch(lret) {
  case 1:
    break;
  default:
    // error, timeout or constrain violation
    break;
}
```

## Availability

| Up to Version |
|---|
