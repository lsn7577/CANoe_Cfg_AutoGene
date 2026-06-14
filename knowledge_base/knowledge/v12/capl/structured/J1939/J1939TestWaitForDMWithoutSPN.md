# J1939TestWaitForDMWithoutSPN

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestWaitForDMWithoutSPN( dword sourceAddr, dword pgn, dword spn, dword timeout )
```

## Description

The function waits until a defined Suspect Parameter Number (SPN) is not longer transmitted with the parameter group or a timeout occurred.

The parameter group must be able to contain a SPN, so only this parameter groups are allowed: DM1, DM2, DM6, DM12, DM23, DM27, DM28 and DM41-DM52.

## Example

```c
long lret;
lret = J1939TestWaitForDMWithoutSPN(10, 0xF123, 110, 500 );

switch (lret) {
  case 1:
    break;
  default: // error, timeout or constraint violation
    break;
}
```

## Availability

| Since Version |
|---|
