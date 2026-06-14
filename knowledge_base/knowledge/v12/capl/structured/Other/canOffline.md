# canOffline

> Category: `Other` | Type: `function`

## Syntax

```c
void canOffline(); // form 1: deprecated
```

## Description

Cuts the connection between the node and the bus. Messages send from the node are not passed through to the bus. The function canOnline() will restore the connection.

If the node is set to offline, output instructions for sending messages in CAPL or NodeLayer DLL are ignored (refers to a node locally only).Regardless of the status, all messages are received in the CAPL program/NodeLayer.

Form 1 only has an effect on the CAPL-program.

In Form 2 you can choose between the CAPL-program and/or the Nodelayer-DLL.

## Parameters

| Name | Description |
|---|---|
| 1 | Deactivates the CAPL-program |
| 2 | Deactivates the Nodelayer |
| 3 | Deactivates the CAPL-program and the Nodelayer and separates the diagnostic ECU simulation from the network, if one is configured for the node |

## Return Values

Form 2 returns the part of the node being online before the function call. Equal to the flags.

## Example

```c
dword var;
var = canOffline(3); // Deactivates CAPL-Program and Nodelayer-DLL.
...
canOnline(); // Activates CAPL-Program. Form 1
...
var = canOnline(2); // Activates Nodelayer-DLL
```

## Availability

| Since Version |
|---|
