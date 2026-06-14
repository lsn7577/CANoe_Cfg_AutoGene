# linGetMasterResistorState

> Category: `LIN` | Type: `function`

## Syntax

```c
long linGetMasterResistorState();
```

## Description

Returns the internal master resistor’s current state of the LIN interface hardware.

This function only works with LIN core network interfaces.

## Return Values

State of the master resistor:
1: Resistor is on0: Resistor is off

## Example

```c
// on pressing key ‘c’ switch on the master resistor
...
on key 'c'
{
  long ret;
  ret = linGetMasterResistorState();
  write("Resistor State: %d", ret);
}
```

## Availability

| Since Version |
|---|
