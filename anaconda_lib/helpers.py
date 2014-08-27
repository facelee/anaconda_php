
# Copyright (C) 2014 - Oscar Campos <oscar.campos@member.fsf.org>
# This program is Free Software see LICENSE file for details

import sublime

from anaconda.anaconda_lib import helpers as anaconda_helpers


def get_settings(view, name, default=None):
    """Get settings
    """

    if view is None:
        return None

    plugin_settings = sublime.load_settings('AnacondaPHP.sublime-settings')
    return view.settings().get(name, plugin_settings.get(name, default))


# reuse anaconda helper functions
active_view = anaconda_helpers.active_view
get_view = anaconda_helpers.get_view


__all__ = ['get_settings', 'active_view', 'get_view']
