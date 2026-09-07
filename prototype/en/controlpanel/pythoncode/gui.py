import wx
import wx.xrc

choice_list = ["اهلاً,  كيف حالك",
               "السلام عليكم ورحمة الله",
               "وَعَلَيْكُمْ السَلامْ",
               "مَرْحَباً,  كيف حالك",
               "يَسُرُّنِي سَمَاعُ ذَلِكَ",
               "أَنَا بِخَيْرٍ وَ الْحَمْدُ لِلَّهِ",
               "أنا بُوُ سَيْفْ, رجلٌ آلي , صُمِّمْتُ وصُنِعْتُ في جامعة الإماراتِ العَرَبِيَةِ الْمُتَّحِدَة",
               "من العين",
               "العين دار الزين",
               "انت جميل جدا",
               " انتِ جميلة"]

list_of_unknown = ["اهلاً,  كيف حالك",
                   "السلام عليكم ورحمة الله",
                   "وَعَلَيْكُمْ السَلامْ",
                   "مَرْحَباً,  كيف حالك",
                   "يَسُرُّنِي سَمَاعُ ذَلِكَ",
                   "أَنَا بِخَيْرٍ وَ الْحَمْدُ لِلَّهِ",
                   "أنا بُوُ سَيْفْ, رجلٌ آلي , صُمِّمْتُ وصُنِعْتُ في جامعة الإماراتِ العَرَبِيَةِ الْمُتَّحِدَة",
                   "من العين",
                   "العين دار الزين"]


class Frame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(800, 700), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"RUN!", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"Manual", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_button3, 0, wx.ALIGN_RIGHT | wx.ALL | wx.TOP, 5)

        self.m_button41 = wx.Button(self, wx.ID_ANY, u"Camera", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_button41, 0, wx.ALL | wx.TOP, 5)

        self.m_button32 = wx.Button(self, wx.ID_ANY, u"Facial Expression", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_button32, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Write To Speak", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer4.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL)
        bSizer4.Add(self.m_textCtrl3, 3, wx.ALL | wx.EXPAND | wx.TOP, 20)
        m_listBox2Choices = list_of_unknown
        self.m_listBox2 = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox2Choices, 0)
        bSizer4.Add(self.m_listBox2, 1, wx.ALIGN_RIGHT | wx.ALL, 10)

        gSizer2 = wx.GridSizer(0, 2, 0, 0)

        m_choice1Choices = choice_list
        self.m_choice1 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0)
        self.m_choice1.SetSelection(0)
        bSizer4.Add(self.m_choice1, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_staticText21 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)
        gSizer2.Add(self.m_staticText21, 0, wx.ALL, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"Training!", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_button5, 0, wx.ALIGN_BOTTOM | wx.ALIGN_LEFT | wx.ALL, 5)

        self.m_slider2 = wx.Slider(self, wx.ID_ANY, 1, 0, 2, wx.DefaultPosition, wx.DefaultSize,
                                   wx.SL_AUTOTICKS | wx.SL_BOTH | wx.SL_INVERSE | wx.SL_LABELS | wx.SL_TOP | wx.DOUBLE_BORDER)
        gSizer2.Add(self.m_slider2, 0, wx.ALIGN_RIGHT | wx.ALL | wx.EXPAND, 5)

        bSizer4.Add(gSizer2, 1, wx.EXPAND, 5)
        self.m_button6 = wx.Button(self, wx.ID_ANY, u"Don't complete", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_button6, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button4.Bind(wx.EVT_BUTTON, self.Run_Robot)
        self.m_button3.Bind(wx.EVT_BUTTON, self.ManualAnswer)
        self.m_button32.Bind(wx.EVT_BUTTON, self.FacialExpression)
        self.m_button41.Bind(wx.EVT_BUTTON, self.VedioTracking)
        self.m_textCtrl3.Bind(wx.EVT_TEXT_ENTER, self.OnTextEnter)
        self.m_choice1.Bind(wx.EVT_CHOICE, self.onChoice)
        self.m_button5.Bind(wx.EVT_BUTTON, self.Train_button)
        self.m_slider2.Bind(wx.EVT_SCROLL, self.MoveRight)
        self.m_button6.Bind(wx.EVT_BUTTON, self.Dont_complete)

        self.m_slider2.Bind(wx.EVT_SCROLL_TOP, self.MoveLeft)
        self.m_listBox2.Bind(wx.EVT_LISTBOX_DCLICK, self.list_choice)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def Run_Robot(self, event):
        event.Skip()

    def ManualAnswer(self, event):
        event.Skip()

    def VedioTracking(self, event):
        event.Skip()

    def FacialExpression(self, event):
        event.Skip()

    def OnTextEnter(self, event):
        event.Skip()

    def MoveRight(self, event):
        event.Skip()

    def MoveLeft(self, event):
        event.Skip()

    def onChoice(self, event):
        event.Skip()

    def list_choice(self, event):
        event.Skip()

    def Train_button(self, event):
        event.Skip()

    def Dont_complete(self, event):
        event.Skip()