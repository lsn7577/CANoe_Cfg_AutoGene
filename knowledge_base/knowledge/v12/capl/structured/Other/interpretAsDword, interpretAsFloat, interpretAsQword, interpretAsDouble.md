# interpretAsDword, interpretAsFloat, interpretAsQword, interpretAsDouble

> Category: `Other` | Type: `function`

## Syntax

```c
dword interpretAsDword(float x);
```

## Description

These functions interpret the actual bytes of a value as if the value was of another data type.

InterpretAsFloat for example takes the four bytes or a dword, interprets them as if they were four bytes of an IEEE single precision floating point number, and returns that number.

InterpretAsDouble interprets eight bytes as if they were an IEEE double precision floating point number.

InterpretAsDword and InterpretAsQword are the inverse functions.

## Return Values

The interpreted value.

## Example

```c
// take a message with 8 bytes representing a double number
on message MessageWithDoubleSignal
{
  qword rawBytes;
  double value;
  rawBytes = this.qword(0);
  value = interpretAsDouble(rawBytes);
  write("The value is %g", value);
}
```

## Availability

| Since Version |
|---|
