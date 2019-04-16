import QtQuick 2.9
import QtQuick.Window 2.2

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("QML syntax demo")

    property string textToShow: ""

    Row{
        id: row1
        anchors.centerIn: parent
        spacing: 20

        Rectangle{
            id: redRectangle
            width: 150
            height: 150
            color: "red"
            radius: 20

            MouseArea{
                anchors.fill:  parent
                onClicked: {
                    console.log("red rectangle is clicked")
                    textToShow = "red"
                }
            }
        }
        Rectangle{
            id: greenRectangle
            width: 150
            height: 150
            color: "green"
            radius: 20

            MouseArea{
                anchors.fill: parent
                onClicked: {
                    console.log("green rectangle is clicked")
                    textToShow = "green"
                }
            }
        }
        Rectangle{
            id: blueRectangle
            width: 150
            height: 150
            color: "blue"
            radius: 20

            MouseArea{
                anchors.fill:  parent
                onClicked: {
                    console.log("blue rectangle is clicked")
                    textToShow = "blue"
                }
            }
        }
        Rectangle{
            id: textRectId
            width: 150
            height: 150
            color: "dodgerBlue"
            radius: 100

            Text {
                id: textId
                text: textToShow
                anchors.centerIn: parent
            }

            MouseArea{
                anchors.fill:  parent
                onClicked: {
                    console.log("blue rectangle is clicked")
                    textId.text = "loop"
                }
            }
        }
    }
}
