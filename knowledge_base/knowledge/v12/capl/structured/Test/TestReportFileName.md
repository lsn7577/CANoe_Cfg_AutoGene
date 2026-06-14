# TestReportFileName

> Category: `Test` | Type: `function`

## Syntax

```c
TestReportFileName (char data name[]);
```

## Description

Sets the name and path of a report file.In the CANoe GUI the name and path of a report file can be set. With this function these settings can be overwritten.

## Return Values

—

## Example

```c
void MainTest()
{
   // report is written in a file with the name ‚DynamicName’ beside the configuration
   TestReportFileName("DynamicName");
}
```

## Availability

| Since Version |
|---|
