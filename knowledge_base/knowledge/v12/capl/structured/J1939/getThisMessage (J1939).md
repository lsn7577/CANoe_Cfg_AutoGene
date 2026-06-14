# getThisMessage (J1939)

> Category: `J1939` | Type: `function`

## Syntax

```c
getThisMessage(pg pg_variable, int length);
```

## Description

Transfers the parameter group to the indicated parameter group pg. The number of bytes of the transmitted parameter group data is given by length.

This function must be used exclusively within the program block.

## Return Values

—

## Example

```c
pg TC1 pg_tc1; // Definition of a parameter group

on pg * { // Event procedure for all parameter groups
if (pg.pgn == TC1) { // If the received parameter group is TC1
// Transfer the received parameter group to the variable
GetThisMessage(pg_tc1, pg_tc1.dlc);
}
```

## Availability

| Since Version |
|---|
