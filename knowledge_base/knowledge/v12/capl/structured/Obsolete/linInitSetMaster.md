# linInitSetMaster

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void linInitSetMaster(long masterMode, long masterResistor)
```

## Description

This function activates or deactivates the Master mode and the terminating resistor on the LIN hardware.

It is of particular significance to the LIN hardware whether an internal Master (a Master modeled in the LIN hardware) or an external Master is used, since when an external Master is used the LIN hardware synchronizes to its pulse, but with an internal master it prescribes the pulse itself.

The default setting is to deactivate both of these parameters when no Master node is modeled.

## Return Values

—

## Example

```c
on linReceiveError
{
linInitSetMaster(1, 1); // manually activate Master mode on LIN hardware
}
```

## Availability

| Up to Version |
|---|
