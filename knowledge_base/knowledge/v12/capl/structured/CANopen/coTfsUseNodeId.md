# coTfsUseNodeId

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsUseNodeId( void );
```

## Description

This function instructs the node layer, for functions which accept both the node-ID and the CAN-ID as parameter, to use the node-ID. This setting is active automatically on measurement start.

## Return Values

Error code

## Example

```c
coTfsUseNodeId();
// uses node-ID for simplified functions
// …

coTfsUseCANid();
// uses can identifier for simplified functions
// …
```
