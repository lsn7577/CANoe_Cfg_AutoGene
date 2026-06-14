# write

> Category: `Other` | Type: `function`

## Syntax

```c
void write(char format[], ...);
```

## Description

Outputs a text message to the Write Window. Write is based on the C function printf.

The compiler cannot check the format string. Illegal format entries will lead to undefined results. Messages output with the write function will be displayed on separate lines.

## Parameters

| Name | Description |
|---|---|
| "%ld","%d" | decimal display |
| "%lx","%x" | hexadecimal display |
| "%lX","%X" | hexadecimal display (upper case) |
| "%lu","%u" | unsigned display |
| "%lo","%o" | octal display |
| "%s" | display a string |
| "%g","%f" | floating point display e.g. %5.3f means, 5 digits in total (decimal point inclusive) and 3 digits after the decimal point. 5 is the minimum of digits in this case. |
| "%c" | display a character |
| "%%" | display %-character |
| "%I64d","%lld" | decimal display of a 64 bit value |
| "%I64x","%llx | hexadecimal display of a 64 bit value |
| "%I64X","%llX" | hexadecimal display of a 64 bit value (upper case) |
| "%I64u","%llu" | unsigned display of a 64 bit value |
| "%I64o","%llo" | octal display of a 64 bit value |

## Return Values

—

## Example

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

| Since Version |
|---|
