# Iso11783IL_PDDGetLastError

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDGetLastError();
```

## Description

Supplies the last error code.

## Return Values

error code of the function most recently executed

## Example

```c
char text[256];

value = Iso11783IL_PDDGetValue ( PD::AppRateSignal, 0;

if (Iso11783IL_PDDGetLastError () != 0) {
  Iso11783IL_PDDGetLastErrorText ( elCount(text), text );
  write( "ERROR: %s", text );
}
```

## Availability

| Since Version |
|---|
