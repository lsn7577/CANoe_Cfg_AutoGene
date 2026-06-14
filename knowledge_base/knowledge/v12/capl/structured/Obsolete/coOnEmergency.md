# coOnEmergency

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coOnEmergency( dword nodeId, dword errorCode, dword errorRegister );
```

## Description

This function is called if an emergency message was received. Data of manufacturer emergency codes can be read with coThisGetData.

## Return Values

—

## Example

```c
void coOnEmergency( dword nodeId, dword errorCode, dword errorRegister ){
  write( "Emergency message from node %d with error code 0x%X received", nodeId, errorCode );
}
```

## Availability

| Up to Version |
|---|
