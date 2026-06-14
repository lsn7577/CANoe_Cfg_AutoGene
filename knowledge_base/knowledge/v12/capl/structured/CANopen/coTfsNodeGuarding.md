# coTfsNodeGuarding

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsNodeGuarding( dword maxResponseTime );
```

## Description

After that, 20 guarding remote frames are sent to the target device. The target device must respond to all queries within the maxResponseTime.

## Return Values

Error code

## Example

```c
if ( coTfsNodeGuarding (40) != 1) {  // maxResponseTime
  write("Node guarding test  failed");
}
```
