# coLssInqRevNo

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coLssInqRevNo( dword errCode[] );
```

## Description

This service causes the determination of the revision number of a LSS slave. It is available in configuration mode only and there may only be one LSS slave in this mode.

## Return Values

—

## Example

```c
dword errCode[1];

coLssInqRevNo( errCode );
if (errCode[0] == 0) {
  write( "LSS inquire Revision-Number commanded" );
}
```

## Availability

| Up to Version |
|---|
