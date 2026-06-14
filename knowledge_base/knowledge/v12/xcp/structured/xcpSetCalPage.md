# xcpSetCalPage

> Category: `XCP` | Type: `function`

## Syntax

```c
void xcpSetCalPage(char ecuQualifier[], byte mode, byte segmentNr, byte pageNr);
```

## Description

If the XCP slave device supports calibration data page switching, this command sets the current page and access mode.

The callback returns that the ECU switched the calibration data page.

## Return Values

—

## Example

```c
variables
{
   long mMode;
   long mSegmentNr;
}

void OnXcpConnect(char ecuName[])
{
   mMode = 255;
   mSegmentNr = 0;
   write("Connect callback! ECU: %s", ecuName);
   XcpGetCalPage(ecuName, mMode, mSegmentNr);
}

void OnXcpGetCalPage(char ecu[], long reserved1, long reserved2, long pageNumber)
{
   Write("OnXcpGetCalPage callback! ECU: %s. Current PageNumber: %d", ecu, pageNumber);
   if (pageNumber == 0)
   {
      pageNumber = 1;
   }
   else
   {
      pageNumber = 0;
   }
   XcpSetCalPage(ecu, mMode, mSegmentNr, pageNumber);
}

void OnXcpSetCalPage(char ecu[])
{
   Write("OnXcpSetCalPage callback! ECU: %s", ecu);
}
```

## Availability

| Since Version |
|---|
