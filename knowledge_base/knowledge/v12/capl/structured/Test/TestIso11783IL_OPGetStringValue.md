# TestIso11783IL_OPGetStringValue

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_OPGetStringValue( dbNode node, dword objectID, dword bufferSize, char buffer[] );
```

## Description

The function copies a string value of an object in the object pool into a buffer. The object must exist in the object pool and support a string value.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
testcase StructuredDataSample()
{
  long table = 0;
  TestCaseDescription("Shows how to display a user-defined info table.");
  TestStepPass(0, "1", "First Step");

  // begin table
  table = TestInfoTable("User Structured Data");

  // header
  TestInfoHeadingBegin(table, 0);
  TestInfoCell(table, "Left part");
  TestInfoCell(table, "Operation");
  TestInfoCell(table, "Right part");
  TestInfoCell(table, "Result");
  TestInfoHeadingEnd(table);

  // row 1
  TestInfoRow(table, 0);
  TestInfoCell(table, "Frequency");
  TestInfoCell(table, "<");
  TestInfoCell(table, "50");
  TestInfoCell(table, "warning");

  // row 2
  TestInfoRow(table, 0);
  TestInfoCell(table, "Temperature");
  TestInfoCell(table, "in range");
  TestInfoCell(table, "90-100");
  TestInfoCell(table, "pass");

  // intermediate header
  TestInfoHeadingBegin(table, 1);
  TestInfoCell(table, "Additional conditions", 4);
  TestInfoHeadingEnd(table);

  // row 4
  TestInfoRow(table, 1);
  TestInfoCell(table, "Test Duration", 2);
  TestInfoCell(table, "60s");
  TestInfoCell(table, "fail");

  // output table
  TestStepFail(0, "2", table);
}
```

## Availability

| Since Version |
|---|
