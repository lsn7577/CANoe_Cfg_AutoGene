# J1939TestChkConfig_SetTitle

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestChkConfig_SetTitle( long aCheckId, char aTitle[] )
```

## Description

This functions sets the title of a check.

The check is displayed in the Write Window and the test report with this title.

## Example

```c
// set title of the check
dword checkID;
checkID = J1939TestChkCreate_BAMViolation( 50, 200, 0x00 );

J1939TestChkConfig_SetTitle( checkID, "This is a BAM violation title");
```

## Availability

| Since Version |
|---|
