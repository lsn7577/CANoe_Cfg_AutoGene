# TestCreateInputTable

> Category: `Test` | Type: `function`

## Syntax

```c
TestCreateStringInputTable(char text[], char caption[], char info[]);
```

## Description

This function creates a selection dialog. To add a value table entry, use the command TestAddValueTableEntry or TestAddStringTableEntry. After all entries are added the dialog can be opened by the command TestWaitForInput.

## Return Values

The handle of the dialog.

## Example

```c
handle = TestCreateStringInputTable("Test Text", "Test Caption", "Test String Input Table Timeout");
TestAddStringTableEntry(handle, "Test Entry");
TestWaitForInput(handle, 5000);
TestGetStringInput(resultStr, elcount(resultStr));

handle = TestCreateValueInputTable("Test Text", "Test Caption", "Test Value Input Table Timeout");
TestAddValueTableEntry(handle, 9);
TestWaitForInput(handle, 5000);
write("Result: %f", TestGetValueInput());
```

## Availability

| Since Version |
|---|
