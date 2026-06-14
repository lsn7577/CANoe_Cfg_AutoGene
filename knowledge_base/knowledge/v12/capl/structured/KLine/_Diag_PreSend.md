# _Diag_PreSend

> Category: `KLine` | Type: `function`

## Syntax

```c
_Diag_Presend(BYTE data[], WORD& dataLenInOut, WORD headerLen)
```

## Description

Is called before a frame is transmitted. Allows manipulating the frame.

## Return Values

—

## Example

```c
_Diag_Presend(BYTE data[], WORD& dataLenInOut, WORD headerLen)
{
   if (!gDoPatchInPreSend) // Global variable
   {
      return;
   }

   gDoPatchInPreSend = 0; // deactivate patching

   // Changing the data and the length of the request
   data[2] = 0x99;
   data[3] = 0x99;
   dataLenInOut = 4;
}
```

## Availability

| Since Version |
|---|
