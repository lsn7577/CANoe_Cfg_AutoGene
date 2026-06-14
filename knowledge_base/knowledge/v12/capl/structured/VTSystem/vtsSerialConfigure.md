# vtsSerialConfigure

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsSerialConfigure (char Target[],eVTSBaudRate baudrate, eVTSDataBits numberOfDataBits, eVTSStopBits numberOfStopBits, eVTSParity parity);
```

## Description

Configures the serial port of the VT System channel that is specified by the system variable namespace.

Without setting up a configuration explicitly, the default configuration is used.Default baud rate: 1200, 8 data bits, 1 stop bit, no parity.

## Return Values

0: Successful call

## Example

This example shows how to use the RS232 functionality of the VT7001 module. It is assumed, that power supply 1 of the VT7001 is connected to a proper counterpart (e.g. a PC) via a serial connection. In this example the string “Hello World!” is sent by the VT7001. After that all incoming characters are output to the Write Window. After 10 seconds the connection is closed.

—

```c
RS232Example ()
{
   // Declare variables for RS232 communication
   char stringToSend[20] = "Hello World !"; // String to send
   byte sendBuffer[20];                     // Byte array to hold send data
   byte receiveBuffer[20];                  // Buffer for received data
   int i;                                   // Counter variable

   // Register the RS232 callback functions
   vtsSerialSetOnErrorHandler("VTS::ECUPowerSupply", "OnRS232Error");
   vtsSerialSetOnReceiveHandler("VTS::ECUPowerSupply", "OnRS232Receive");
   vtsSerialSetOnSendHandler("VTS::ECUPowerSupply", "OnRS232Sent");

   // Configure the serial port i.e. for communication with an external
   // ECU power supply to 9600 baud, 8 data bits, 1 stop bit, no parity
   vtsSerialConfigure("VTS::ECUPowerSupply", eVTSBaudRate9600, eVTSDataBitsEight, eVTSStopBitsOne, eVTSParityNone);

   // Open the serial port i.e. for communication with an external ECU power supply
   vtsSerialOpen("VTS::ECUPowerSupply");

 // Wait briefly to make sure settings are applied and port is ready
   TestWaitForTimeOut(10);

   // **** Send data ****

   // Copy the string to a byte array and send it
   for (i=0; i<strlen(stringToSend); ++i) sendBuffer[i] = stringToSend[i];
   vtsSerialSend("VTS::ECUPowerSupply", sendBuffer, strlen(stringToSend));

   // **** Receive data ****

   // For 10s output all received data to the Write Window
   Write("Waiting for incomming data...");
   vtsSerialReceive("VTS::ECUPowerSupply", receiveBuffer, elcount(receiveBuffer));
   TestWaitForTimeOut(10000);

   // Close the serial port
   vtsSerialClose("VTS::ECUPowerSupply");
}

void OnRS232Error(dword flags)
{
   // Write error details to the Write Window
  if((flags & (dword) eVTSSerialErrorsSendOperationFailed) != 0)
  {
    Write("Error occurred on serial port of VT7001 module: eVTSSerialErrorsSendOperationFailed");
  }
  if((flags & (dword) eVTSSerialErrorsFrameError) != 0)
  {
    Write("Error occurred on serial port of VT7001 module: eVTSSerialErrorsFrameError");
  }
}

void OnRS232Receive(byte buffer[], dword number)
{
   long i;
   char string[256];

   // Create a string from the given byte array
   for(i=0; i<elcount(buffer); ++i)
      string[i] = buffer[i];

   // Write received data to the Write Window
   Write("Received '%s' (%d bytes) on ECU power supply port.", string, number);
}

void OnRS232Sent(byte buffer[], dword number)
{
   long i;
   char string[256];

   // Create a string from the given byte array
   for(i=0; i<elcount(buffer); ++i)
      string[i] = buffer[i];

   // Write sent data to the Write Window
   Write("Sent '%s' (%d bytes) on ECU power supply port.", string, number);
}
public void RS232Example()
   {
      // Get VTS interface and external power supply 1
      IVTSystem vts = VTSystem.Instance;
      IVT7001Supply1 ecuPowerSupply = vts.GetChannel("ECUPowerSupply") as IVT7001Supply1;

      // Register the event handlers
      ecuPowerSupply.OnSerialSentEvent += new OnSerialSentHandler(this.SendHandler);
      ecuPowerSupply.OnSerialReceivedEvent += new OnSerialReceivedHandler(this.ReceiveHandler);
      ecuPowerSupply.OnSerialErrorEvent += new OnSerialErrorHandler(this.ErrorHandler);

      // Configure the serial port i.e. for communication with an external
      // ECU power supply to 9600 baud, 8 data bits, 1 stop bit, no parity
      ecuPowerSupply.SerialConfigure(BaudRate.BaudRate9600, DataBits.Eight, StopBits.One, Parity.None);

      // Open the serial port i.e. for communication with an external ECU power supply
      ecuPowerSupply.SerialOpen();

 // Wait briefly to make sure settings are applied and port is ready
      Vector.CANoe.Threading.Execution.Wait(10);

      // **** Send data ****

      // Send a string via RS232
      ecuPowerSupply.SerialSend("Hello world!");

      // **** Receive data ****

      // For 10s output all received data to the Write Window
      byte[] receiveBuffer = new byte[32];
      ecuPowerSupply.SerialReceive(receiveBuffer);
      Vector.CANoe.Threading.Execution.Wait(10000);

      // Close the serial port
      ecuPowerSupply.SerialClose();
   }

   public void SendHandler(object sender, SerialSentEventArgs e)
   {
      // Print sent data to Write Window
      System.Text.ASCIIEncoding enc = new System.Text.ASCIIEncoding();
      Vector.Tools.Output.WriteLine("The following data was sent: " + enc.GetString(e.Buffer));
   }

   public void ReceiveHandler(object sender, SerialReceivedEventArgs e)
   {
      // Print received data to Write Window
      System.Text.ASCIIEncoding enc = new System.Text.ASCIIEncoding();
      Vector.Tools.Output.WriteLine("Received the following data: " + enc.GetString(e.Buffer));
   }

   public void ErrorHandler(object sender, SerialErrorEventArgs e)
   {
      // Print error to Write Window
      Vector.Tools.Output.WriteLine("An error occurred in the serial connection: " + e.ErrorFlags.ToString());
   }
```

## Availability

| Since Version |
|---|
