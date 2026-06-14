# coTfsUseCANid

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsUseCANid( void );
```

## Description

This function transmits the internally-stored CAN label to the simplified test functions insofar as it is supported. On measurement start, the system always automatically uses the node-ID.

## Return Values

Error code

## Example

```c
coTfsUseNodeId();
// uses node-ID for simplified functions
// …

coTfsUseCANid(); 
// uses CAN identifier for simplified functions
...
```
