# TestGetByteInput

> Category: `Test` | Type: `function`

## Syntax

```c
TestGetByteInput(byte[] result, dword resultSize);
```

## Description

After a dialog with byte input is closed you can use this function to get the input.

## Return Values

resultSize
Size of the byte array

## Example

```c
handle = TestWaitForByteInput("Test Text", "Test Caption", "Test Byte Input", 0);
TestGetByteInput(resultByte, elcount(resultByte));
```

## Availability

| Since Version |
|---|
