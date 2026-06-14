# FSIL_EnableNameManagement

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword FSIL_EnableNameManagement(dword enable ); // form 1
```

## Description

Activates the name management of a node. Not until the name management is activated another node can change the device name of this node by sending a name management message.

## Return Values

0 on success or FS IL Error Code

## Example

```c
//allow every component to be changed except arbitrary address capable flag
FSIL_EnableNameManagement(1, 0xFE);
```

## Availability

| Since Version |
|---|
