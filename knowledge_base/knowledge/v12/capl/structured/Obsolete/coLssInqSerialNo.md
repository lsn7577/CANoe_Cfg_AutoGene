# coLssInqSerialNo

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coLssInqSerialNo( dword errCode[] );
```

## Description

This service causes the determination of the serial number of a LSS slave. It is available in configuration mode only and there may only be one LSS slave in this mode.

## Return Values

—

## Example

```c
dword errCode[1];

coLssInqSerialNo( errCode );
if (errCode[0] == 0) {
  write( "LSS inquire Serial-Number commanded" );
}
```

## Availability

| Up to Version |
|---|
