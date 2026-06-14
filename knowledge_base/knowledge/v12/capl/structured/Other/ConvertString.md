# ConvertString

> Category: `Other` | Type: `function`

## Syntax

```c
long ConvertString(byte output[], long& encodedSize, long maxOutputSize, dword outputCodepage, byte input[], long inputSize, dword inputCodepage);
```

## Description

Converts a string from one encoding to another encoding. The length of the converted string depends on the requested encoding. The number of bytes used in the output byte array is written to encodedSize. If the size of the output array maxOutputSize is not sufficient to hold the converted string and a terminating “\0”, the function returns an error and the content of output is undefined. Characters that cannot be represented in the requested encoding, are replaced with the best matching character, selected by the Windows function WideCharToMultiByte.

## Return Values

0: Success, the byte array output and the resulting length encodedSize are valid.

## Example

```c
// Convert a system variable string value (e.g. input from a panel) into UTF-16 and vice versa
includes
{
  #include "Encoding.cin"
}

// handle input of a string, e.g. from a panel
on sysvar TestVars::StringSV
{
  byte data[100]; long nrOfBytes; byte data2[200]; long res;
  // get the string in UTF-8
  sysGetVariableData(sysvar::TestVars::StringSV, data, nrOfBytes);
  // convert it to UTF-16
  res = ConvertString(data2, nrOfBytes, elcount(data2), CP_UTF16, data, nrOfBytes, CP_UTF8);
  // now use the UTF-16 bytes, e.g. send them over a network
  // here simulated by using a system variable of type data
  sysSetVariableData(sysvar::TestVars::DataVar, data2, nrOfBytes);
}

// receive UTF-16 data, e.g. from a network
// here simulated by using a system variable of type data
on sysvar TestVars::DataVar
{
  byte data[200]; long nrOfBytes; byte data2[100]; long res;
  sysGetVariableData(sysvar::TestVars::DataVar, data, nrOfBytes);
  // data is the string in UTF-16; convert it to UTF-8
  res = ConvertString(data2, nrOfBytes, elcount(bytes), CP_UTF8, data, nrOfBytes, CP_UTF16);
  // copy the string into a system variable of type string, e.g. to display it in a panel
  sysSetVariableData(sysvar::TestVars::OutStringVar, data2, nrOfBytes);
}
```

## Availability

| Since Version |
|---|
