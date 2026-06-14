# writeToLogEx

> Category: `Other` | Type: `function`

## Syntax

```c
void writeToLogEx(char format[], ...);
```

## Description

Writes an output string to an ASCII logging file. Write is based on the C function printf.

The compiler cannot check the format string. Illegal format entries will lead to undefined results. Different to the writeToLog function, neither comment characters ("//") nor time stamps will be printed at the beginning of a line.

## Parameters

| Name | Description |
|---|---|
| "%ld","%d" | decimal display |
| "%lx","%x" | hexadecimal display |
| "%lX","%X" | hexadecimal display (upper case) |
| "%lu","%u" | unsigned display |
| "%lo","%o" | octal display |
| "%s" | display a string |
| "%g","%lf" | floating point display |
| "%c" | display a character |
| "%%" | display %-character |
| "%I64d" | decimal display of a 64 bit value |
| "%I64x" | hexadecimal display of a 64 bit value |
| "%I64X" | hexadecimal display of a 64 bit value (upper case) |
| "%I64u" | unsigned display of a 64 bit value |

## Return Values

—

## Example

```c
// write marker with current date and time to logging file
void MarkLogFileWithTimeString(void)
{
char timeBuffer[64];
getLocalTimeString(timeBuffer);
writeToLogEx("===> %s",timeBuffer);
}
```

## Availability

| Since Version |
|---|
