import QtQuick 2.9
import QtQuick.Window 2.2

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Property Binding Demo")

    Rectangle{
        id: redRectId
        width: 50
        height: width * 1.5
        color: "red"

    }
    Rectangle{
        id: blueRectId
        width: 100
        height: 100
        color: "blue"
        anchors.bottom: parent.bottom

        MouseArea{
            anchors.fill: parent
            onClicked: {
                redRectId.width = redRectId.width+10
            }
        }
    }


}
