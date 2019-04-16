import QtQuick 2.9

Item {
    property alias rectColor: receiverRectId.color
    width: receiverRectId.width
    height: receiverRectId.height
    function receiverInfo(count){
        receiverDisplayTextId.text = count
        console.log("Receiver received number:" +count)

    }

    Rectangle{
        id: receiverRectId
        width: 200
        height: 200
        color: "red"
    }

    Text {
        id: receiverDisplayTextId
        anchors.centerIn: parent
        font.pointSize: 12
        text: "0"
    }


    }

