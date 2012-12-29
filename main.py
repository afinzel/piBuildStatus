from Lights import Lights
from TrafficLights import TrafficLights

import time
import twitter


def main():

    twitter_username = "GMGShopJenkins"

    twitter_api = twitter.Api()

    traffic = TrafficLights()
    lights = Lights()

    traffic.cycle_lights()

    while (True):
        statuses = twitter_api.GetUserTimeline(twitter_username)

        last_status = statuses[0].text
        print last_status

        if "SUCCESS" in last_status:
            traffic.reset_lights()
            traffic.turn_on_light(lights.Green)

        if "UNSTABLE" in last_status:
            traffic.reset_lights()
            traffic.turn_on_light(lights.Amber)

        if "FAILURE" in last_status:
            traffic.reset_lights()
            traffic.turn_on_light(lights.Red)

        if last_status == "blink":
            traffic.blink(lights.Amber, 2, 15)
        else:
            time.sleep(60)

if __name__ == "__main__":
    main()
