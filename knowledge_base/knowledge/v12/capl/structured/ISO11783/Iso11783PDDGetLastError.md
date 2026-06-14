# Iso11783PDDGetLastError

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783PDDGetLastError();
```

## Description

Supplies the last error code.

## Return Values

Error code of the function most recently executed

## Example

```c
char text[256];

value = Iso11783PDDGetValue 
 ( ecuHandle, PD::AppRateSignal, 0;

if (Iso11783PDDGetLastError
 () != 0) {
  Iso11783PDDGetLastErrorText 
 ( elCount(text), text );
  write( 
 "ERROR: %s", text );
}
```

## Availability

| Since Version |
|---|
