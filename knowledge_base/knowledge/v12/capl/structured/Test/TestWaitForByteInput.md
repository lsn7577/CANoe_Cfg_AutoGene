# TestWaitForByteInput

> Category: `Test` | Type: `function`

## Syntax

```c
TestWaitForByteInput(char text[], char caption[], char info[]);
```

## Description

This function opens a dialog for byte array input. Optionally you can set some timeout in ms. Afterwards the dialog will be closed. You can optionally define some default input for the dialog.

## Return Values

—

## Example

```c
handle = TestWaitForByteInput("Test Text", "Test Caption", "Test Byte Input", 0);
TestGetByteInput(resultByte, elcount(resultByte));

handle = TestWaitForByteInput("Test Text", "Test Caption", "Test Byte Input Timeout", 5000);
TestGetByteInput(resultByte, elcount(resultByte));
```

## Availability

| Since Version |
|---|
