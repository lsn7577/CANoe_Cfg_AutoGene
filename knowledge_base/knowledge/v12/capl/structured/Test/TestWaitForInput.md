# TestWaitForInput

> Category: `Test` | Type: `function`

## Syntax

```c
TestWaitForInput(long handle);
```

## Description

After you have created a value table or range dialog use this function to open the dialog.

## Return Values

—

## Example

```c
handle = TestCreateValueInputTable("Test Text", "Test Caption", "Test Value Input Table Timeout");
TestAddValueTableEntry(handle, 9);
TestWaitForInput(handle, 5000);
write("Result: %f", TestGetValueInput());
```

## Availability

| Since Version |
|---|
