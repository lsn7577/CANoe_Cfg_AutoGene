# coSetNodeLabel

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coSetNodeLabel( char nodeLabel[], dword errCode[] );
```

## Description

Usually the node label is build automatically from the nodes name and its node-ID specified within the assigned CAN database. For test nodes it is not possible to assign a node from a CAN database within the configuration dialog of the test node. Furthermore the user maybe wants to determine the name of a node by itself. This function can be used to determine the node label manually. If the user wants to reset the manually specified label this function has to be called with an empty node label (""). Afterwards the automatically build node label is used.

## Return Values

—

## Example

```c
dword errCode[1]

coSetNodeLabel ("mySimulatedNode", errCode );
if (errCode[0] == 0) {
  write( "New node label successfully set");
}
```

## Availability

| Up to Version |
|---|
