# coEmergency

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coEmergency( dword active, dword emcyError, byte specificData[], dword dataSize, dword errCode[] );
```

## Description

The function activates or deactivates an emergency error code. The error register [0x1003,0] and the 'Predefined error field' object are set. An emergency message is also sent.

## Return Values

—

## Example

```c
dword errCode[1];
byte data[5] = { 0, 0, 0, 0 };

coEmergency ( 1, 0x8120, data, elcount(data), errCode );
if (errCode[0] == 0) {
  write( "Error passive mode entered" );
}

coEmergency ( 0, 0x8120, data, elcount(data), errCode );
if (errCode[0] == 0) {
  write( "Error active mode entered" );
}
```

## Availability

| Up to Version |
|---|
