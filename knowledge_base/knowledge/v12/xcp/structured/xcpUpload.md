# xcpUpload

> Category: `XCP` | Type: `function`

## Syntax

```c
long xcpUpload(char namespace[], char variable[]);
```

## Description

Initiates an upload of the XCP parameter from ECU and updates the dedicated system variable.

After finishing of the upload the callback function OnXcpUpload is called to indicate the upload status.

Use the return value of xcpUpload to check if an error occurred during initiation of the upload.

Use the errorIndication parameter of the OnXcpUpload callback function to check for errors occurred during the upload, if an error during call of xcpUpload occurs OnXcpUpload is not called.

## Return Values

0: OK

## Example

```c
testcase TC_SignalInactive ()
{
xcpUpload("XCP::ECU","testword0");
....

}
//Callback function:
void OnXcpUpload (char namespace[], char variable[], long returnValue)
{
if (returnValue==0)
write("Systemvariable updated: %s %s", namespace,variable);
}
```

## Availability

| Since Version |
|---|
