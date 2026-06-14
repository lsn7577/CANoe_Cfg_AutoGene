# J1939ILControlStart

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILControlStart(); // form 1
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
 J1939ILControlStart();
}
```

## Availability

| Since Version |
|---|
