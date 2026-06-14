# coTfsSetTestModuleNodeId

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSetTestModuleNodeId( dword nodeId );
```

## Description

The function set the node-ID of the tester. This is particularly necessary for the application profile. The function has to be called before the first use of SDOs.

## Return Values

Error code

## Example

```c
coTfsSetTestModuleNodeId(15); // set node-ID to 15
```
