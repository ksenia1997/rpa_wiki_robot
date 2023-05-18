import time

import robotics
import settings.static


def main():
    robot = robotics.Robot("Quandrinaut")
    robot.say_hello()
    robot.intro()
    robot.open_webpage("https://google.com")
    time.sleep(1)
    for scientist_name in settings.static.SCIENTISTS:
        robot.retrieve_scientist_info(scientist_name=scientist_name)
    robot.browser.close_browser()
    robot.say_goodbye()


if __name__ == "__main__":
    main()
