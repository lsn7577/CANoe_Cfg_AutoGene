# CANopenInternalNMTCommand

> Category: `CANopen` | Type: `function`

## Syntax

```c
void CANopenInternalNMTCommand(dword nodeId, dword NMTCommand );
```

## Description

Performs an NMT command inside a simulated CANopen node.

## Return Values

The data as qword.

## Example

```c
CANopenInternalNMTCommand(2, 1); //Start node 2

}
```

## Availability

| Since Version |
|---|
