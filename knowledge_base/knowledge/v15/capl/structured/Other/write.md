# write

> Category: `Other` | Type: `function`

## Syntax

```c
void write(char format[], ...);
```

## Description

Outputs a text message to the Write Window. Write is based on the C function printf.

The compiler cannot check the format string. Illegal format entries will lead to undefined results. Messages output with the write function will be displayed on separate lines.

## Return Values

—

## Example

Examples

```c
float f=123.456;
on key 'h'
{
   write("Hello World!");
   write("f = %5.3f",f);
   write("format is not supported for the given variable");
   write("f = %7.3f",f);
   write("f = %9.3f",f);
}
on key 'q'
{
   qword q = 0x1234567890ABCDEFLL;
   write("Decimal: %I64u", q);
   write("Hexadecimal: %I64X", q);
}
on key 'd'
{
   dword d = 0x1234;
   write("Decimal: %u", d);
   write("Hexadecimal: %X", d);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 2.5 | 2.5 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
