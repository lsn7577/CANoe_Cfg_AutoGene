# J1939GetEcuState

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939J1939GetEcuState(dword ecuHandle);
```

## Description

Returns the current state of the ECU.

## Example

```c
if (J1939GetEcuState( handle ) == 2) {
  write( "ECU is online" );
}
```

## Availability

| Since Version |
|---|
