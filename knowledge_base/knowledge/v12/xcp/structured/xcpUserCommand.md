# xcpUserCommand

> Category: `XCP` | Type: `function`

## Syntax

```c
void xcpUserCommand(char ecuQualifier[], byte data[], long dataSize);
```

## Description

Sends user-defined data to the XCP slave.

The callback returns the response on the user command.

## Return Values

—

## Example

In the following example the use of user commands for XCP with xcpSet/GetCalPage is shown.

```c
variables
{
   long mMode;
   long mSegmentNr;
   byte mUsrCmdResponse = 0;
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
   ProcessUserCmd();
}

void ProcessUserCmd()
{
   byte adata[12] = { 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C };
   XCPUserCommand("XcpSim", adata, 12);
}

void OnXcpUserCommand(char ecu[],byte data[], long dataSize)
{
   mUsrCmdResponse = data[0];
   Write("OnXcpUserCommandResponse callback! ECU: %s. Data: %d. Data size: %d", ecu, data[0], dataSize);
}
```

## Availability

| Since Version |
|---|
