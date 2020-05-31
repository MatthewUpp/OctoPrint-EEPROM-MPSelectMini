# coding=utf-8
from __future__ import absolute_import


import octoprint.plugin
import octoprint.server

class Eeprom_MalyanSTM32F401Plugin(octoprint.plugin.AssetPlugin,
                            octoprint.plugin.TemplatePlugin):
    def get_assets(self):
        return dict(
            js=["js/eeprom_malyan_stm32f401.js"]
        )

    def get_template_configs(self):
        return [
            dict(type="settings", template="eeprom_malyan_stm32f401_settings.jinja2", custom_bindings=True)
        ]

    def get_update_information(self):
        return dict(
            systemcommandeditor=dict(
                displayName="EEPROM Editor for Malyan STM32F401 Based 3D Printers - Plugin",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
                user="MatthewUpp",
                repo="OctoPrint-EEPROM-Malyan-STM32F401",
                current=self._plugin_version,

                # update method: pip
                pip="https://github.com/MatthewUpp/OctoPrint-EEPROM-Malyan-STM32F401/archive/{target_version}.zip"
            )
        )

__plugin_name__ = "EEPROM Editor for Malyan and Monoprice STM32F401 Based 3D Printers"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = Eeprom_MalyanSTM32F401Plugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
