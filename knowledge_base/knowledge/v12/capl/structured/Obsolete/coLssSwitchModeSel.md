# coLssSwitchModeSel

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coLssSwitchModeSel( dword vendorId, dword productCode, dword revisionNo, dword serialNo, dword errCode[] );
```

## Description

This service puts the LSS slave whose LSS address matches the transmitted parameters into the configuration mode.

## Return Values

—

## Example

```c
dword errCode[1];

coLssSwitchModeSel( 0x1020304, 0x5060708, 0x90a0b0c, 0xd0e0f10, errCode );
if (errCode[0] == 0) {
  write( "Switch to configuration mode for one slave commanded" );
}
```

## Availability

| Up to Version |
|---|
