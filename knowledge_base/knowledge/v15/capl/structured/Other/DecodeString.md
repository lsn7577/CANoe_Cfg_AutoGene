# DecodeString

> Category: `Other` | Type: `function`

## Syntax

```c
long DecodeString(char output[], long outputSize, byte input[], long inputSize, dword codepage);
```

## Description

Decodes the byte array input from the encoding codepage to the current CAPL string encoding.

The length of the decoded string depends on the given encoding. If the size of the output array outputSize is not sufficient to hold the decoded string and a terminating “\0”, the functions returns an error and the content of output is undefined. Characters that cannot be represented in the current encoding, are replaced with the best matching character, selected by the Windows function WideCharToMultiByte.

## Parameters

| Name | Description |
|---|---|
| output | Target char array. |
| outputSize | Size of the output array. |
| input | The input string in encoding codepage, without BOM. |
| codepage | Windows code page number for input.The include file Encoding.cin defines the following code pages: CP_UTF8 CP_UTF16 CP_LATIN1 CP_SHIFT_JIS |

## Example

```c
includes
{
  #include "Encoding.cin"
}

...
{
  int result;
  char text[10];
  byte stream[6] = {0xC3, 0xA4, 0xC3, 0xB6, 0xC3, 0xBC};
  result = DecodeString(text, 10, stream, 6, CP_UTF8);
  // on German Windows, text is now {‘ä’, ‘ö’, ‘ü’, 0}
  if (result == 0) {
    write(text);
    // Output (on a German Windows): äöü
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.1 SP3 | 8.1 SP3 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
