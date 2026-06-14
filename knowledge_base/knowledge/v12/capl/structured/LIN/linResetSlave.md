# linResetSlave

> Category: `LIN` | Type: `function`

## Syntax

```c
long linResetSlave ()
```

## Description

This function resets the NAD (Node Address for Diagnostic) of the modeled Slave node and marks all its protected identifiers as invalid or it will load the last saved configuration if resetToLastConfiguration is set.

See Notes to the way initial NAD is determined to understand how initial NAD is determined in CANoe.

If the CAPL-program calling this function, does not model a LIN 2.x Slave node, then this function will have no effect.

## Return Values

On success this function returns a value unequal to -1, otherwise -1.

## Example

Force Slave reset on a keyboard event

```c
on key 'r'
{
if ( linResetSlave() != -1) {
// from now on the Slave node stops publishing responses 
...
}
}
```

## Availability

| Since Version |
|---|
