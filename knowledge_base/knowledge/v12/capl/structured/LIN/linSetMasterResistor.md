# linSetMasterResistor

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSetMasterResistor (long onOff)
```

## Description

Enables or disables the internal master resistor of the LIN hardware interface.

This function only works with LIN core network interfaces.

## Return Values

If successful a value unequal to zero.

## Example

```c
// on pressing key ‘c’ switch on the master resisitor
...
on key 'c'
{
  linSetMasterResisitor (1);
  write("Turn Resistor On");
}
```

## Availability

| Since Version |
|---|
