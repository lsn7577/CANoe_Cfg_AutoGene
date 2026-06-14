# coGetNodeLabel

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coGetNodeLabel( char buffer[], dword bufferSize, dword errCode[] );
```

## Description

The function returns the label of the node. The label is formed from the name and the node-ID of the assigned database.

So that the label of the node can be formed correctly, a few things must be noted. For more details, see Integration of the node layer in the introduction.

## Return Values

—

## Example

```c
dword errCode[1];
char nodeLabel[256];

coGetNodeLabel ( nodeLabel, elcount(nodeLabel), errCode );
if (errCode[0] == 0) {
  write( "Nodelabel is: %s", nodeLabel );
}
```

## Availability

| Up to Version |
|---|
