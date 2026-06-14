# beep

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Replaced by msgBeep |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Function Syntax | void beep(int freq, int duration); |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Function | Tone output. In the Windows Version the parameter duration has no effect. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Parameters | freq Integer for tone pitch. In the Windows version, the parameters freq defines the tone output. Different sounds are defined in the section [SOUND] in the file WIN.ini: freq 0x0000 (SystemDefault) freq 0x0010 (SystemHand) freq 0x0020 (SystemQuestion) freq 0x0030 (SystemExclamation) freq 0x0040 (SystemAsterisk) freq 0xFFFF Standard Beep Note Windows always generates the same system beep, if you have no sound card installed on your PC. In this case, the parameter freq has no effect. | freq | 0x0000 (SystemDefault) | freq | 0x0010 (SystemHand) | freq | 0x0020 (SystemQuestion) | freq | 0x0030 (SystemExclamation) | freq | 0x0040 (SystemAsterisk) | freq | 0xFFFF Standard Beep | Note Windows always generates the same system beep, if you have no sound card installed on your PC. In this case, the parameter freq has no effect. |
| freq | 0x0000 (SystemDefault) |  |  |  |  |  |  |  |  |  |  |  |  |  |
| freq | 0x0010 (SystemHand) |  |  |  |  |  |  |  |  |  |  |  |  |  |
| freq | 0x0020 (SystemQuestion) |  |  |  |  |  |  |  |  |  |  |  |  |  |
| freq | 0x0030 (SystemExclamation) |  |  |  |  |  |  |  |  |  |  |  |  |  |
| freq | 0x0040 (SystemAsterisk) |  |  |  |  |  |  |  |  |  |  |  |  |  |
| freq | 0xFFFF Standard Beep |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Note Windows always generates the same system beep, if you have no sound card installed on your PC. In this case, the parameter freq has no effect. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| duration integer for tone length |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Return Values | — |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |  |  |  |  |  |  |  |  |  |  |
| 2.5 | — | • | • |  |  |  |  |  |  |  |  |  |  |  |
| Example void sound() {// with sound card: 400 Hz tone / 500ms long// without sound card: Default signal tonebeep (400,500);} |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
