# coTfsEmcyResetList

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsEmcyResetList( void );
```

## Description

This function deletes the internal list on which occurring emergency messages are stored.

It is possible to omit the nodeID parameter. In this case, the internally-stored value set with coTfsSetNodeId is used.

## Return Values

Error code

## Example

```c
coTfsEmcyResetList(2);
```
