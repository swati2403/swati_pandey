import QtQuick 2.9
import QtQuick.Window 2.2

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("QT Global Objects")
    property var fonts: Qt.fontFamilies()
    Rectangle{
       width: 300
       height: 100
       color: "red"
       MouseArea{
           anchors.fill: parent
           onClicked: {
               //quit the application
               console.log("quitting the App")
               Qt.quit()
               //listing font family
               for(var i =0; i< fonts.length; i++){
                   console.log("[" +i+"]" +fonts[i])
               }
               //hash a string
               var mName = "Swati Pandey"
               var mHashName = Qt.md5(mName)
               console.log("the hash of mName:" +mHashName)
               //open url externally
               Qt.openUrlExternally("http://www.google.com")
               //platform info
               console.log(Qt.platform.os)
           }
       }
    }
}
