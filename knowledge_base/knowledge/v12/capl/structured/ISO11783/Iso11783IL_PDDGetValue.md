# Iso11783IL_PDDGetValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
float Iso11783IL_PDDGetValue( dbSignal signal, dword elementNumber ); // form 1
```

## Description

The function returns the value of a process variable.

## Return Values

value of the process variable, 0 if the variable is not defined

## Example

```c
char text[256];
value = Iso11783IL_PDDGetValue( PD::AppRateSignal, 0 );
if (Iso11783IL_PDDGetLastError 
 () != 0) {
  Iso11783IL_PDDGetLastErrorText 
 ( elCount(text), text );
  write( 
 "ERROR: %s", text);
}
```

## Availability

| Since Version |
|---|
