# coTfsNmtStopNode

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsNmtStopNode( void );
```

## Description

This call triggers a NMT message that sets the in DUT Device Under Test to the stopped state. The new state is not checked because SDO transfers are not allowed in stopped mode.

## Return Values

Error code

## Example

```c
if ( coTfsNmtStopNode() != 1) {
  write("stop node failed");
}
```
