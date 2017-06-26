import Tkinter as tk

"""Model Class used in MVC design"""

import wx


class view(wx.Frame):
    user_name = ''

    """Setups all Gui Parameters"""
    def __init__(self):
        # creat app object
        self.app = wx.App()

        # Set up the main window
        wx.Frame.__init__(self, parent=None, title='Background Checker', size=(400, 300))

        # The platforms available
        self.platforms = ['reddit', 'twitter']

        """ Layout panel and hbox """
        self.panel = wx.Panel(self, size=(500, 100))
        self.box = wx.BoxSizer(wx.VERTICAL)

        # Greeting combobox
        self.platform = wx.ComboBox(parent=self.panel, value='Please Select an Option', size=(180, -1),
                                    choices=self.platforms)

        # Add the platform button to the hbox
        self.box.Add(self.platform, 0, wx.TOP)
        self.box.Add((-1, 10))

        """ setup username textbox entry """
        username_prompt = 'Please type a username (type a letter to clear this field)'
        self.username_textbox = wx.TextCtrl(parent=self.panel, size=(280, -1), value=username_prompt)

        # Add the greeting combo to the hbox
        self.box.Add(self.username_textbox, 0, wx.TOP)

        # Add padding to lower the button position
        self.box.Add((-1, 100))

        # The background check button
        self.background_check_button = wx.Button(self.panel, 10, '&Background Check')

        """ Bind an event for the button """
        self.Bind(wx.EVT_TEXT, self.clear_textbox, self.username_textbox)
        self.Bind(wx.EVT_BUTTON, self.record_username, self.background_check_button)

        # Add the button to the hbox
        self.box.Add(self.background_check_button, 0, flag=wx.ALIGN_CENTER | wx.BOTTOM)

        # Tell the panel to use the hbox
        self.panel.SetSizer(self.box)

    """
    Records the username typed into the textbox and closes the GUI
    """
    def record_username(self, *args):
        self.user_name = self.username_textbox.GetValue()
        self.Close()

    """
    Clears the textbox and skips to the next event
    @param event
        event object
    """
    def clear_textbox(self, event):
        self.username_textbox.SetValue("")
        self.Unbind(wx.EVT_TEXT, self.username_textbox)
        event.Skip()

    """Runs the app"""
    def run(self):
        self.Show()
        self.app.MainLoop()

