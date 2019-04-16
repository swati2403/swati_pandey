import QtQuick 2.9

Item {
    property alias rectColor: notifierRectId.color
    width: notifierRectId.width
    height: notifierRectId.height
    property int count: 0
    signal notify(string count)//declare signal

    property Receiver target: null

    onTargetChanged: {
        notify.connect(target.receiverInfo)
    }

    Rectangle{
        id: notifierRectId
        width: 200
        height: 200
        color: "red"
    }

    Text {
        id: displayTextId
        anchors.centerIn: parent
        font.pointSize: 12
        text: count
    }

    MouseArea{
        anchors.fill: parent
        onClicked: {
            count++
            notify(count)
        }
    }
}
