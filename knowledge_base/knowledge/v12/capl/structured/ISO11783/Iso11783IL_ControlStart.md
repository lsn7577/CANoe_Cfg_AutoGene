# Iso11783IL_ControlStart

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_ControlStart();
```

## Description

The node starts Address Claiming (if NMT is activated). If the Address Claiming was successful, cyclic messages are sent.

The source address can be specified optionally. If it is not specified the node attribute NmStationAddress must be defined.

## Return Values

0 on success or error code

## Example

```c
on start
{
 Iso11783IL_ControlStart();
}
```

## Availability

| Since Version |
|---|
