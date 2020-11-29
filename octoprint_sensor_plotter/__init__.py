# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin


class SensorPlotterPlugin(octoprint.plugin.StartupPlugin,
                          octoprint.plugin.TemplatePlugin,
                          octoprint.plugin.SettingsPlugin,
                          octoprint.plugin.AssetPlugin):

    def on_after_startup(self):
        self._logger.info("Sensor Plotter (more: %s)" % self._settings.get(["url"]))

    def get_settings_defaults(self):
        return dict(url="https://google.com")

    #def get_template_vars(self):
    #    return dict(url=self._settings.get(["url"]))

    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]

    def get_assets(self):
        return dict(
            js=["js/sensor_plotter.js"],
            css=["css/sensor_plotter.css"],
            less=["less/sensor_plotter.less"]
        )


__plugin_name__ = "Sensor Plotter"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = SensorPlotterPlugin()
