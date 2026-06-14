# coTfsClearObjectName

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsClearObjectName( dword nodeId );
```

## Description

This function deletes stored object names that are load with coTfsLoadDeviceDescription.

## Return Values

Error code

## Example

```c
/* clear known object dictionary entries for node-ID 112 */
if (coTfsClearObjectName(112) != 1)
{
  /* clear process failed */
} /* if */
```
