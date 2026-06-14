# output (J1939)

> Category: `J1939` | Type: `function`

## Syntax

```c
output(pg pg_variable);
```

## Description

Outputs a parameter group onto the CAN bus.

## Return Values

—

## Example

```c
variables {
pg 0xFEE1 pg_1 = { // Definition of a parameter group
};
}
on key F1 {
output (pg_1); // Output parameter group
}
```

## Availability

| Since Version |
|---|
