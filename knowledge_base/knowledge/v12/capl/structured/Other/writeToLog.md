# writeToLog

> Category: `Other` | Type: `function`

## Syntax

```c
void writeToLog(char format[], ...);
```

## Description

Writes an output string to an ASCII logging file. Write is based on the C function printf.

The compiler cannot check the format string. Illegal format entries will lead to undefined results. Different to the writeToLogEx function, comment characters ("//") and a time stamp at the beginning of each line will be printed.

The maximum length of the resulting string is limited to 1024 characters.

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
void MarkLogFile(int marker) {
// marks line of ASCII logging file with an integer
writeToLog("===> %d",marker);
}
```

## Availability

| Since Version |
|---|
