def goto(browser, url):
    return browser.get(url)


def click_button(browser, element):
    return browser.click(element)


action_dict = {}

action_dict["goto"] = goto
action_dict["click_button"] = click_button
