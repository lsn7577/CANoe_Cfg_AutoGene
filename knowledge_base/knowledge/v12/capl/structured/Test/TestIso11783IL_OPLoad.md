# TestIso11783IL_OPLoad

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_OPLoad( dbNode node, char filename[] );
```

## Description

The function loads an object pool file (*.iop). All other object pool access functions can only be used, if an object pool is loaded.

If the activation of the object pool was already done, the object pool is transmitted to the Virtual Terminal immediately. If not, this happens when the activation is done with Iso11873IL_OPActivate.

Optional a version designator for the object pool can be specified. The node layer tries to load the version with the Load Version command. If this is successful the object pool must not be transmitted to the Virtual Terminal.

This function is not necessary if a node was configured completely in the database (DBC):ISO11783IOPFilename and ISO11783IOPVersion are defined and VT21 message is assigned to the node.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

0: Function has been executed successfully

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
