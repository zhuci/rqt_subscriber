<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>SubscriberWidget</class>
 <widget class="QWidget" name="SubscriberWidget">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>739</width>
    <height>406</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Message Subscriber</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <widget class="QPushButton" name="refresh_button">
       <property name="toolTip">
        <string>Refresh topics and types</string>
       </property>
       <property name="text">
        <string/>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="text">
        <string>Topic</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="ExtendedComboBox" name="topic_combo_box">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Expanding" vsizetype="Fixed">
         <horstretch>1</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>100</width>
         <height>0</height>
        </size>
       </property>
       <property name="toolTip">
        <string>Topic name to publish on</string>
       </property>
       <property name="editable">
        <bool>true</bool>
       </property>
       <property name="sizeAdjustPolicy">
        <enum>QComboBox::AdjustToMinimumContentsLength</enum>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_2">
       <property name="text">
        <string>Type</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="ExtendedComboBox" name="type_combo_box">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Expanding" vsizetype="Fixed">
         <horstretch>2</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>100</width>
         <height>0</height>
        </size>
       </property>
       <property name="toolTip">
        <string>Message type to publish</string>
       </property>
       <property name="editable">
        <bool>true</bool>
       </property>
       <property name="sizeAdjustPolicy">
        <enum>QComboBox::AdjustToMinimumContentsLength</enum>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_3">
       <property name="text">
        <string>Freq.</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QComboBox" name="frequency_combo_box">
       <property name="minimumSize">
        <size>
         <width>60</width>
         <height>0</height>
        </size>
       </property>
       <property name="toolTip">
        <string>Frequency for periodic subscribers in Hz (set to 0 for manual publishing)</string>
       </property>
       <property name="editable">
        <bool>true</bool>
       </property>
       <item>
        <property name="text">
         <string>1</string>
        </property>
       </item>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_4">
       <property name="text">
        <string>Hz</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="add_subscriber_button">
       <property name="toolTip">
        <string>Add new subscriber</string>
       </property>
       <property name="text">
        <string/>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="remove_subscriber_button">
       <property name="toolTip">
        <string>Remove selected subscriber</string>
       </property>
       <property name="text">
        <string/>
       </property>
       <property name="shortcut">
        <string>Del</string>
       </property>
      </widget>
     </item>
     <item>
      <spacer name="horizontalSpacer">
       <property name="orientation">
        <enum>Qt::Horizontal</enum>
       </property>
       <property name="sizeHint" stdset="0">
        <size>
         <width>20</width>
         <height>20</height>
        </size>
       </property>
      </spacer>
     </item>
     <item>
      <widget class="QPushButton" name="clear_button">
       <property name="toolTip">
        <string>Clear all subscribers</string>
       </property>
      </widget>
     </item>
    </layout>
   </item>
   <item>
    <layout class="QHBoxLayout" name="horizontalLayout_2"/>
   </item>
   <item>
    <widget class="SubscriberTreeWidget" name="subscriber_tree_widget">
     <property name="contextMenuPolicy">
      <enum>Qt::CustomContextMenu</enum>
     </property>
     <property name="toolTip">
      <string>Right click on item or selection for more options.</string>
     </property>
     <property name="dragEnabled">
      <bool>true</bool>
     </property>
     <property name="dragDropMode">
      <enum>QAbstractItemView::DragOnly</enum>
     </property>
     <property name="selectionMode">
      <enum>QAbstractItemView::ExtendedSelection</enum>
     </property>
     <property name="sortingEnabled">
      <bool>true</bool>
     </property>
    </widget>
   </item>
  </layout>
 </widget>
 <customwidgets>
  <customwidget>
   <class>ExtendedComboBox</class>
   <extends>QComboBox</extends>
   <header>rqt_py_common.extended_combo_box</header>
  </customwidget>
  <customwidget>
   <class>SubscriberTreeWidget</class>
   <extends>QTreeView</extends>
   <header>rqt_subscriber.subscriber_tree_widget</header>
  </customwidget>
 </customwidgets>
 <resources/>
 <connections/>
</ui>
