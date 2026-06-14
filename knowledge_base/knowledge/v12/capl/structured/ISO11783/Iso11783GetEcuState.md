# Iso11783GetEcuState

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783GetEcuState(dword ecuHandle);
```

## Description

Returns the current state of the ECU.

## Example

```c
if (Iso11783GetEcuState( handle ) == 2) {
  write( "ECU is online" );
}
```

## Availability

| Since Version |
|---|
