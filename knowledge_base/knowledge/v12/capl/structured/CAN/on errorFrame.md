# on errorFrame

> Category: `CAN` | Type: `event`

## Description

The error frame handler is called after receiving an Error Frame or an Overload Frame.

If a CAN FD ISO-enabled hardware interface is used, the handler will also be called on occurrence of a protocol exception. The protocol exception is signaled either if the CAN controller is set to restricted mode and an error occurs, or if the protocol exception handling is enabled. In the former case the error code can be used to find out the type of error. In the latter case the error code is set to protocol exception. This means, that either the CAN controller has received a CAN FD frame in classical CAN mode (the FDF bit of the frame is recessive), or the res-Bit in a CAN FD frame is recessive.

The Error Frame handler for CAPL-on-Board is only available for devices whose driver transmit Error Frames to CAPL-on-Board.

## Example

The following code will output the error code and the direction of the error frame as formatted string to the write window.

```c
on errorFrame
{
  const int bufferSize = 256;
  char buffer[bufferSize];
  char cdirection[2][3] = {"RX", "TX"};
  int ndir;
  word ecc;
  word extInfo;
  int isProtocolException;

  ecc = (this.ErrorCode >> 6) & 0x3f;
  extInfo = (this.ErrorCode >> 12) & 0x3;
  isProtocolException = (this.ErrorCode & (1 << 15)) != 0;

  ndir = extInfo == 0 || extInfo == 2 ? 0 : 1; //set ndir to 0 for RX and to 1 for TX

  if(this.CtrlType == 1){
    //SJA1000 specific
    switch (ecc){
    case 0: snprintf(buffer, bufferSize, "Bit error"); break;
    case 1: snprintf(buffer, bufferSize, "Form error"); break;
    case 2: snprintf(buffer, bufferSize, "Stuff error"); break;
    case 3: snprintf(buffer, bufferSize, "Other error"); break;
    default: snprintf(buffer, bufferSize, "Unknown error code");
    }
  }
  else if(this.CtrlType == 2){
    //CAN core specific
    switch (ecc){
      case 0: snprintf(buffer, bufferSize, "Bit error"); break;
      case 1: snprintf(buffer, bufferSize, "Form error"); break;
      case 2: snprintf(buffer, bufferSize, "Stuff error"); break;
      case 3: snprintf(buffer, bufferSize, "Other error"); break;
      case 4: snprintf(buffer, bufferSize, "CRC error"); break;
      case 5: snprintf(buffer, bufferSize, "ACK Del. error"); break;
      case 7:
      {
        switch (extInfo){
        case 0: snprintf(buffer, bufferSize, "RX NACK error (recessive error flag)"); break;
        case 1: snprintf(buffer, bufferSize, "TX NACK error (recessive error flag)"); break;
        case 2: snprintf(buffer, bufferSize, "RX NACK error (dominant error flag)"); break;
        case 3: snprintf(buffer, bufferSize, "TX NACK error (dominant error flag)"); break;
      }
      break;
    }
    case 8: snprintf(buffer, bufferSize, "Overload frame"); break;
    case 9: snprintf(buffer, bufferSize, "FDF or res recessive"); break;  //protocol exception specific
    default: snprintf(buffer, bufferSize, "Unknown error code"); break;
    }
  }
  else snprintf(buffer, bufferSize, "Unsupported CAN controller");

  if(isProtocolException){
    write("Protocol exception on CAN%d at %fs: %s", this.can, this.time/1e5, buffer);
  }
  else{
    write("%s error frame on CAN%d at %fs: %s", cdirection[ndir], this.can, this.time/1e5, buffer);
  }
}
```

## Availability

| Since Version |
|---|

## Selectors

| ErrorFrame | ../CAPLfunctionErrorFrameSelectors.htm |
|---|---|
