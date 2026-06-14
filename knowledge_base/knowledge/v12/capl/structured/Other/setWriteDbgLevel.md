# setWriteDbgLevel

> Category: `Other` | Type: `function`

## Syntax

```c
void setWriteDbgLevel (unsigned int priority);
```

## Description

This function sets the priority level for the writeDbgLevel CAPL function. The output priority must be set for every network node.

## Parameters

| Name | Description |
|---|---|
| 0 | Only write output with a priority of 0 are shown in the Write Window. |
| 5 | Write output with a priority ranging from 0 to 5 are shown. |
| 15 | All outputs are shown. |

## Return Values

—

## Example

```c
int i = 10;
int j = 12;
setWriteDbgLevel(7);
writeDbgLevel (4, "This is shown: h= %lxh",j);
 // Output: This is shown: h= 0ch
writeDbgLevel (9, "This is not shown: d= %ld",i);
 // No output
```

## Availability

| Since Version |
|---|
