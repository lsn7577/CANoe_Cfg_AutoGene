# TCIL_EnableNameManagement

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword TCIL_EnableNameManagement(dword enable ); // form 1
```

## Description

This function activates the name management of a node. Not until the name management is activated another node can change the device name of this node by sending a name management message.

## Return Values

0 on success or TC IL Error Code

## Example

```c
//allow every component to be changed except arbitrary address capable flag
TCIL_EnableNameManagement(1, 0xFE);
```

## Availability

| Since Version |
|---|
