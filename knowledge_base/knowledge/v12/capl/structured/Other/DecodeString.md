# DecodeString

> Category: `Other` | Type: `function`

## Syntax

```c
long DecodeString(char output[], long outputSize, byte input[], long inputSize, dword codepage);
```

## Description

Decodes the byte array input from the encoding codepage to the current CAPL string encoding.

The length of the decoded string depends on the given encoding. If the size of the output array outputSize is not sufficient to hold the decoded string and a terminating “\0”, the functions returns an error and the content of output is undefined. Characters that cannot be represented in the current encoding, are replaced with the best matching character, selected by the Windows function WideCharToMultiByte.

## Return Values

0: Success, the byte array output is valid.

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

| Since Version |
|---|
