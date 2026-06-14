# keypressed

> Category: `Other` | Type: `function`

## Syntax

```c
dword keypressed();
```

## Description

This function returns the key code of a currently pressed key. If no key is being pressed it returns 0.. For example, pressing of a key can be queried in a timer function. The reaction can also be to letting go of a key.

## Return Values

Key code of pressed key.
If the 8 lower bits do not equal 0, keypressed returns the ASCII code of the next key in the keyboard buffer. If the 8 lower bits do not equal 0, the 8 upper bits represent the extended key code (see IBM PC Technical Reference Manual).

## Example

```c
variables
{
   message 0x1A0 msg; // intialises a message with the
         // name msg and identifier 0x1A0
   msTimer myTimer;  // timer with millisecond resolution
   int running;  // memorises the first keypress to
         // bypass the key repeat
   int counter;  // message counter
}
on timer myTimer
{
   if (keypressed())   // if key is pressed ...
   {  
      counter++;   // increment counter by 1
      msg.byte(0) = counter; // write the counter reading
         // into the 1. byte of the message
      output(msg);  // send the message to the bus
      setTimer(myTimer, 100); // set a timer to 100 ms
   }
   else      // if key is released...
   {
      running = 0;  // wait until new keypress
   }
}
on key 'r'
{
   if (running == 1) return; // inhibit key repeat

   setTimer (myTimer,0);  // start timer
   running = 1;   // memorise of first keypress
}
```

## Availability

| Since Version |
|---|
