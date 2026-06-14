# coTfsSDOResetAbortList

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOResetAbortList( dword nodeID ); // form 1
```

## Description

Form 1: Removes all entries of the previously received SDO abort codes from the internal list. The following call of coTfsSdoGetAbortCode returns 0.

Form 2: It is possible to omit the parameter nodeID. In this case, the internal saved value set with coTfsSetNodeId() is used as node-ID.

## Return Values

Error code

## Example

```c
coTfsSDOResetAbortList( 0 );
```
