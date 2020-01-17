#!/bin/bash

LED_BTN=4
LED_ROUGE=10
LED_VERTE=27

# monitor GPIO pin 3 for shutdown signal
# export GPIO pin 3 and set to input with pull-up

echo "3" > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio3/direction

# monitor GPIO pin 4 for LED Button and pin 10,27 for LEDs
# export GPIO pin 4,10,27 and set to output

echo "$LED_BTN" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio$LED_BTN/direction
echo "1" > /sys/class/gpio/gpio$LED_BTN/value

echo "$LED_ROUGE" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio$LED_ROUGE/direction
echo "1" > /sys/class/gpio/gpio$LED_ROUGE/value

# wait for pin to go LOW

while [ true ]

do

if [ "$(cat /sys/class/gpio/gpio3/value)" == '0' ]

then

 echo "Raspberry shutting down !"
 echo "0" > /sys/class/gpio/gpio$LED_BTN/value
 echo "0" > /sys/class/gpio/gpio$LED_ROUGE/value

 halt &
  
 exit 0

fi

sleep 1

done
 

