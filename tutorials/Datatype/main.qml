import QtQuick 2.9
import QtQuick.Window 2.2

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("QML Datatypes")
    property string mString: "Hello World"
    property int mInt: 45
    property bool isFemale: false
    property double mDouble: 77.8
    property url mUrl: "http://www.google.com"
    property var aNumber: 100
    property var aBool: true
    property var aString: "Hello World"
    property var anotherString: String("#FF008800")
    property var aColor: Qt.rgba(0.2, 0.3, 0.4, 0.5)
    property var aRectangle: Qt.rect(10, 10, 10, 10)
    property var aPoint: Qt.point(10, 10)
    property var size: Qt.size(10, 10)
    property var aVector3d: Qt.vector3d(100, 100, 100)
    property var aArray: [1, 2, 3, "four", "five", function(){return "six";}]
    property var aObject: {"foo":10, "bar": 20}
    property var aFunction:(function(){return "one";})
//    property var aFont: Qt.font({family: "consolas", pointSize: 30, bold: true})
    property date mDate: "2019-04-15"

    Rectangle{
        id: rectId
        width: 200
        height: 100 + mInt
        anchors.centerIn: parent
        color: aColor

        Text {
            id: mTextId
            anchors.centerIn: parent
            text: mString
//            font: aFont
            font.bold: isFemale?true:false
        }
    }
    Component.onCompleted: {
        console.log("The value of mString:" +mString)
        console.log("The value of mInt:" +mInt)
        if (isFemale){
            console.log("hello")
        } else{
            console.log("hi")
        }
        console.log("The value of mDouble:" +mDouble)
        console.log("The value of mUrl:" +mUrl)
        console.log("PLAYING WITH VAR DATATYPE")
        console.log("value of aNumber:" +aNumber)
        console.log("value of aBool:" +aBool)
        console.log("value of aString:" +aString)
        console.log("The value of anotherString:" +anotherString)
        console.log("The components of rectangle: x=" +aRectangle.x +"Y=" +aRectangle.y + " width=" +aRectangle.width + " height=" +aRectangle.height)
        console.log("The length of an array:" +aArray.length)
        aArray.forEach(function(value){
            console.log(value)
        })
        console.log("date:" + mDate)
    }
}
