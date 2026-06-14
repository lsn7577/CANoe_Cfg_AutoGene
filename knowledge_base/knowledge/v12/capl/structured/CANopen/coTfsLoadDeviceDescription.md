# coTfsLoadDeviceDescription

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLoadDeviceDescription( dword nodeId, char fileName[] );
```

## Description

This function reads an EDS, DCF or XML file. This allows the interpretation of index and sub index during SDO accesses, so that object names can be displayed in plain text.

The object names can be deleted with coTfsClearObjectName.

## Return Values

Error code

## Example

```c
/* load for CANopen device with node ID 112 the eds file "coslave.eds" (path is relative to configuration folder) */
if (coTfsLoadDeviceDescription(112, "coslave.eds") != 1)
{
  /* file could not be loaded, either it does not exist or it is faulty */
} /* if */
```
