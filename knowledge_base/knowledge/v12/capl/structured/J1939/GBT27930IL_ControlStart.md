# GBT27930IL_ControlStart

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_ControlStart(); // form 1
```

## Description

The node starts the cyclic transmission of the configured messages.

The source address can be specified optionally. If it is not specified the node attribute NmStationAddress must be defined.

## Return Values

0 on success or error code

## Example

```c
on start
{
 GBT27930IL_ControlStart();
}
```

## Availability

| Since Version |
|---|
