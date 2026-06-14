# TestAddValueTableEntry

> Category: `Test` | Type: `function`

## Syntax

```c
TestAddStringTableEntry(long handle, char[] value);
```

## Description

This functions adds a new value table entry.

## Return Values

—

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
