# TestAddRange

> Category: `Test` | Type: `function`

## Syntax

```c
TestAddRange(long handle, double minValue, double maxValue);
```

## Description

This function adds a new range that is allowed for dialog input. This can be a minimum/ maximum for a numerical value or a minimum/ maximum length of a string or byte array.

## Return Values

—

## Example

```c
handle = TestCreateValueInputRange("Test Text", "Test Caption", "Test Value Input Range Timeout");
TestAddRange(handle, 0, 5);
TestWaitForInput(handle, 5000);
write("Result: %f", TestGetValueInput());
```

## Availability

| Since Version |
|---|
