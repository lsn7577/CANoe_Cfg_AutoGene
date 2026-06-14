# EncodeString

> Category: `Other` | Type: `function`

## Syntax

```c
long EncodeString(byte output[], long& encodedSize, long maxOutputSize, char input[], dword codepage);
```

## Description

Encodes the string input with the encoding codepage.

The length of the encoded string and a terminating “\0” depend on the requested encoding. The number of bytes used in the output byte array is written to encodedSize. If the size of the output array maxOutputSize is not sufficient to hold the encoded string and the “\0”, the functions returns an error and the content of the output array is undefined.

Characters that cannot be represented in the requested encoding, are replaced with the best matching character, selected by the Windows function WideCharToMultiByte.

## Parameters

| Name | Description |
|---|---|
| output | Target byte array. |
| encodedSize | EncodeString writes the number of bytes used in output (including the terminating “\0”) to this parameter. |
| maxOutputSize | Size of the output array. |
| input | The input string, using the current CAPL string encoding. |
| codepage | Windows code page number for the encoded string.The include file Encoding.cin defines the following code pages: CP_UTF8 CP_UTF16 CP_LATIN1 CP_SHIFT_JIS |

## Example

```c
includes
{
  #include "Encoding.cin"
}

...
{
  int result;
  char text[4] = "äöü";
  byte stream[10];
  long len;
  result = EncodeString(stream, len, 10, text, CP_UTF8);
  // on German Windows, len is now 7, stream is now {0xC3, 0xA4, 0xC3, 0xB6, 0xC3, 0xBC, 0};
  if (result == 0) {...}
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
