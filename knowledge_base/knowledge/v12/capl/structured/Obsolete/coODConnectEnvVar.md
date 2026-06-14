# coODConnectEnvVar

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coODConnectEnvVar( dword index, dword subIndex, char envVar[], dword errCode[] );
```

## Description

Connects an object from the local object dictionary with an environment variable.

## Return Values

—

## Example

```c
dword errCode[1];
char errBuffer[128];

coODConnectEnvVar( 0x6000, 0x1, "MyEnvVar", errCode );
if(errCode[0] != 0) {
  coGetLastError(errBuffer, elCount(errBuffer));
  write( "coODConnectEnvVar failed with code: %x - %s", errCode[0], errBuffer);
}
```

## Availability

| Up to Version |
|---|
