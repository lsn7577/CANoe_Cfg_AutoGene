# coGetVersionInfo

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coGetVersionInfo( char buffer[], dword bufferSize, dword errCode[] );
```

## Description

The function returns the current version number of the node layer used.

## Return Values

—

## Example

```c
dword errCode[1];
char buffer[128];

coGetVersionInfo( buffer, elCount(buffer), errCode );
if (errCode[0] == 0) {
  write( "Used Node layer version: %s", buffer ); 
}
```

## Availability

| Up to Version |
|---|
