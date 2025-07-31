# DeskPlay
@megancampbell + @shumon 

We made a hologram projection desktop display! Our TFT display connects to the Opheus Raspberry Pi Pico and projects onto a clear iphone protector. 

![IMG_0884 2](https://github.com/user-attachments/assets/9fdc3408-ecc8-420a-9565-41f2a2a7a571)

![IMG_0883](https://github.com/user-attachments/assets/c74279d8-f279-45f2-b034-083195a3b964)

![IMG_0882](https://github.com/user-attachments/assets/09dadb86-f34a-4c0f-88ca-2d63c5092f79)

This is also called a heads-up display. It uses an LCD screen inside the box to display an image. That image is then partially reflected by the screen protector (any clear flat object would work, we used a screen protector for simplicity) at an angle that can then be seen by people positioned correctly (roughly perpendicular to the reflective surface) as a hologram inside the screen protector. 

This is a cool effect for a desk display (and where the name came from), but also useful to have an additional display for small things while also not blocking things behind it. While not in use, it is simply a clear glass screen. Even while in use, as the display is a hologram, objects behind it are still visible to some extent, depending on the colors displayed on the Deskplay. 

To make your own, keep in mind that any form factor works! You just need to mount an LCD screen and keep a flat, transparent object at some angle to it (depending on where you want to position it) and bam, holographic display. 

YT Video: https://youtu.be/979JuL8oQ3E

Wiring Guide:

<img width="1024" height="481" alt="image" src="https://github.com/user-attachments/assets/6f74d3a8-2a11-452e-ba7c-8d6bc32c5f03" />


BOM:

| Part                      | Description                        |
|---------------------------|------------------------------------|
| TFT with ILI9341 driver   | Display the GIF                    |
| Orpheus Raspberry Pi Pico| Microcontroller for logic          |
| Jumper wires              | Connecting the display and the Pico|
| 3D printed case           | Holding everything together        |
| iPhone screen protector   | Surface for projection             |

