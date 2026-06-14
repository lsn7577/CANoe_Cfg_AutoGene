# coLssSwitchModeGlob

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coLssSwitchModeGlob( dword mode, dword errCode[] );
```

## Description

Change of all LSS slaves into the configuration mode or leaving of the mode.

## Return Values

—

## Example

```c
dword errCode[1];

coLssSwitchModeGlob( 1, errCode );
if (errCode[0] == 0) {
  write( "Switch to configuration mode for all slaves commanded" );
}
```

## Availability

| Up to Version |
|---|
