# Iso11783PDDGetValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
float Iso11783PDDGetValue( dword ecuHandle, dbSignal signal, dword elementNumber );
```

## Description

The function requests the value of a process variable.

## Return Values

Value of the process variable, 0 if the variable is not defined

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
