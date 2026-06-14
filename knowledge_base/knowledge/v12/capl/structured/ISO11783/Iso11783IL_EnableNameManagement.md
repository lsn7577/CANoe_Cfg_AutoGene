# Iso11783IL_EnableNameManagement

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783IL_EnableNameManagement(dword enable );
```

## Description

This function activates the name management of a node. Not until the name management is activated another node can change the device name of this node by sending a name management message.

## Return Values

0 on success or error code

## Example

```c
//allow every component to be changed except arbitrary address capable flag
Iso11783IL_EnableNameManagement(1, 0xFE);
```

## Availability

| Since Version |
|---|
