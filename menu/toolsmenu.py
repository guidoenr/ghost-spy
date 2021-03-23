from configuration import configpar

def load_tools_values():
    configpar.config_load()
    strings = ''
    for tool_key in configpar.config['tools']:
        strings = strings + format_tool(tool_key) + ' \n'
    return strings

def format_tool(tool_key):
    status = configpar.config_get('tools', tool_key)
    stry = r'{}: '.format(tool_key)
    if status == 'enabled':
        return stry + '\033[92m enabled \033[0m'
    else:
        return stry + '\033[91m disabled \033[0m'

tools = load_tools_values()
menu = """
\033[93m                                
these are the current options in your configuration, choose one to deactivate or activate: 
\033[0m

{}

    [0] back to main menu

""".format(tools)


if __name__ == '__main__':
    strings = load_tools_values()
    print(menu)
