# coTfsGetVersion

> Category: `CANopen` | Type: `function`

## Syntax

```c
dword coTfsGetVersion( void );
```

## Description

This function returns the internal version number of this CANopen Test Feature Set node layer.

## Return Values

Version number

## Example

```c
dword majorVersion;
dword minorVersion;

minorVersion = coTfsGetVersion();
majorVersion = (minorVersion >> 8) & 0xFF;
minorVersion = minorVersion & 0xFF;

write("coTfs node layer version = %d.%d",majorVersion, minorVersion);
```
