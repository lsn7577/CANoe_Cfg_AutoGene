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

The CAPL string encoding usually matches the encoding of the source file. When you create a file with the CAPL Browser, it will save the file in an encoding which matches the language settings of your computer and write the encoding in a special comment at the beginning of the file. If the source file is encoded in UTF-16 or if an include file has a different encoding than the source file, the CAPL string encoding will be UTF-8.

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

| Since Version |
|---|
