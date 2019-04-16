import QtQuick 2.9
import QtQuick.Window 2.2

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")
    Flickable{
        width: textInputId.width
        contentHeight:textInputId.implicitHeight
        height: 300
        clip: true
        anchors.centerIn: parent
        TextEdit{
            id: textInputId
            width: 240
            text: "<strong>Because</strong> shgsjdsdslldsdxsid"+
                "hhskxslkxdslxs;xsxiwjsiwsosxspxo"+
                "tsygswkjkasjsjwlhwswsqsjkwskswlqoklsssjs"+
                "hgshxlioqsiowswsuwswsopgskjkpqwops"+"hksjkjdslkxsxdsxksdxksujssjiudxoi"
                +"tsgsgsuxihysxiusxisduxdsuxsydxu"
            wrapMode: TextEdit.Wrap
            textFormat: TextEdit.RichText
            font.family: "Helvetica"
            font.pointSize: 20
            color: "blue"

    }
  }
}
