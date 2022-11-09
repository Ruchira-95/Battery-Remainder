# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 00:04:49 2022

@author: Ruchira
"""

from plyer import notification
import psutil 

battery=psutil.sensors_battery()
plugged=battery.power_plugged

if __name__=="__main__":
    if plugged:
        percent=battery.percent
        if percent<=80:
            notification.notify(
                title="Plugged In",
                message="Charge upto 80%",
                timeout=2
                )
        elif percent==100:
            notification.notify(
                title="Plugged In",
                message="Battery Fully Charged",
                timeout=2
                )
        else:
            notification.notify(
                title="Plugged In",
                message="Remove the charger.",
                timeout=2
                )
    else:
        percent=battery.percent
        if percent<=20:
            notification.notify(
                title="Battery Remainder",
                message=f"Battery is{percent}.",
                timeout=2
                )
        elif percent<=50:
            notification.notify(
                title="Battery Remainder",
                message="Charge upto 80%.",
                timeout=2
                )
        else:
            notification.notify(
                title="Battery Remainder",
                message=f"Battery is {percent}",
                timeout=2
                )