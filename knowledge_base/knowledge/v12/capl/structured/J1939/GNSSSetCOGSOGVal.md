# GNSSSetCOGSOGVal

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSSetCOGSOGVal ( dword fixSID, dword cogReference}
```

## Description

This function can be used to change values of the parameter group "COG & SOG, Rapid Update" (PGN 129026) which are not modified by the simulation automatically.

The same settings can be made via node attributes in the used database.

## Return Values

error code

## Example

```c
GNSSSetCOGSOGVal ( 0, 1 );
```

## Availability

| Since Version |
|---|
