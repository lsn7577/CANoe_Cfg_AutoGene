# coODDisconnectEnvVar

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coODDisconnectEnvVar( dword index, dword subIndex, dword errCode[] );
```

## Description

Deletes the connection between an object of the local object dictionary and an environment variable.

## Return Values

—

## Example

```c
dword errCode[1];
char errBuffer[128];

coODDisconnectEnvVar( 0x6000, 0x1, errCode );
if(errCode[0] != 0) {
  coGetLastError(errBuffer, elCount(errBuffer));
  write( "coODDisconnectEnvVar failed with code: %#x - %s", errCode[0], errBuffer);
}

coODDisconnectEnvVar( "MyEnvVar", errCode );
if(errCode[0] != 0) {
  coGetLastError(errBuffer, elCount(errBuffer));
  write( "coODDisconnectEnvVar failed with code: %#x - %s", errCode[0], errBuffer);
}
```

## Availability

| Up to Version |
|---|
