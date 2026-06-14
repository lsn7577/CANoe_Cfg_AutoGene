# AfdxGetDBAttrValue

> Category: `ADFX` | Type: `function`

## Syntax

```c
double AfdxGetDBAttrValue( long msgID, char attrName[] );
```

## Description

Retrieves the value of a specific attribute of a dedicated message if the attribute is not of type string.

## Return Values

found attribute value as double representation
If any error occurs, 0 is returned and the exact error code and text can be retrieved using AfdxGetLastError and AfdxGetLastErrorText.

## Example

```c
{
  char[256] RXlist[long]; // Rx messages: store MSG-Id to name association
  long invRXlist[ char[] ]; // Rx messages: store name to MSG-Id association
}
on preStart
{
  dword i;
  dword Tmp;
  long err;
  double txRefreshRate;
  char msgName[256];
  char portMasterName[128];

  for (i = 0; i < elCount(thisNode.RX); i++)
  {
    Tmp = thisNode.RX[i]; // fetch the message ID
    err = AfdxGetDBMessageName(Tmp, elCount(RXlist[Tmp]), RXlist[Tmp]);
    invRXlist[RXlist[Tmp]] = Tmp;
    write("RX-ID = %x (%s)", Tmp, RXlist[Tmp]);

    // retrieve some attributes
    err = AfdxGetDBAttrAsString(Tmp, “AfdxPortMasterName”, elCount(portMasterName), portMasterName);
    txRefreshRate = AfdxGetDBAttrValue(Tmp, “AfdxMsgTxRate”);
    if (err == 0 && AfdxGetLastError() == 0)
    {
      write("AfdxMasterPortName = %s", portMasterName);
      write("AfdxMsgTxRate = %d", (int)txRefreshRate);
    }
  }
}
```

## Availability

| Since Version |
|---|
