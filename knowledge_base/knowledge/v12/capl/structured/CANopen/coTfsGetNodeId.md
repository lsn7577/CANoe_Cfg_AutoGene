# coTfsGetNodeId

> Category: `CANopen` | Type: `function`

## Syntax

```c
dword coTfsGetNodeId( void );
```

## Description

This function returns the internally-stored node-ID that is used for the simplified test functions.

## Return Values

Node-ID

## Example

```c
dword nodeID;
nodeID = coTfsGetNodeId();
```
