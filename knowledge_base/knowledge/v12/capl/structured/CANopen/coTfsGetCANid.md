# coTfsGetCANid

> Category: `CANopen` | Type: `function`

## Syntax

```c
dword coTfsGetCANid( void );
```

## Description

This function returns the internally-stored CAN-ID that is used for the simplified test functions.

## Return Values

CAN-ID

## Example

```c
dword canID;
canID = coTfsGetCANid();
```
