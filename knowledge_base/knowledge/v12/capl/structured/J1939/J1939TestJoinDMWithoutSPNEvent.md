# J1939TestJoinDMWithoutSPNEvent

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestJoinDMWithoutSPNEvent( dword sourceAddr, dword pgn, dword spn )
```

## Description

Adds a new diagnostic message without SPN event to the 'joined events'. The function does not wait.

The parameter group must be able to contain a SPN, so only this parameter groups are allowed: DM1, DM2, DM6, DM12, DM23, DM27, DM28 and DM41-DM52.

## Example

```c
long lret;
J1939TestJoinDMWithoutSPNEvent(10, 0xFF, 1119);
J1939TestJoinDMWithoutSPNEvent(20, 0xFF, 1119);

lret = J1939TestWaitForAnyJoinedEvent ( 500 );
switch(lret) {
  case 1: // first PG received
    break;
  case 2: // second PG received
    break;
  default: // error, timeout or constrain violation
    break;
}
```

## Availability

| Since Version |
|---|
