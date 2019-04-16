import QtQuick 2.9
import QtQuick.Window 2.2

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("external components with signals n slots")


    Notifier{
        id: notifierId
        rectColor: "yellowgreen"
        target: receiverId
//        Component.onCompleted: {
//            notify.connect(receiverId.receiverInfo)//connect notifier to receiver
//        }
    }
    Receiver{
        id: receiverId
        anchors.right: parent.right
        rectColor: "dodgerblue"
    }

//    Rectangle{
//        id: rectId
//        width: 200
//        height: 300
//        color: "blue"

//        signal greet(string message) //declare signal
//        function myGreeting(mMessage){
//            console.log("myGreeting slot is called.The parameter:" +mMessage)
//        }
//        MouseArea{
//            anchors.fill: parent
//            onClicked: {
//                rectId.greet("hello there")// fires the signal
//            }
//        }
//        Component.onCompleted: {
//            rectId.greet.connect(rectId.myGreeting)
//        }
//    }
}
