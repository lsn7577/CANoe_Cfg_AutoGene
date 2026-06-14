# TestModuleDescription

> Category: `Test` | Type: `function`

## Syntax

```c
TestModuleDescription (char description[]);
```

## Description

With this function, a description text for the test module can be written into the report. The function can be called several times in a row, the transmitted texts are then added to one another without additional separation.

To obtain line breaks (in form of <br /> tags) in the CANoe Test Report Viewer or HTML test report, "\n" may be inserted at any place. In case of XML/HTML format, the required replacement takes place during the transformation of the XML test report into an HTML file by means of an XSLT style sheet, where it can also be deactivated.

## Return Values

—

## Availability

| Since Version |
|---|
