var studentID;
var jsonData
var obj

function initialStudent()
{
    $("#stu_login").on("click", getStudentID);
}

function getStudentID()
{
	studentID = $("#stu_id").val();
	//parseJSON();
	window.location.href="page/student_display.html";
	
}

function parseJSON(){
	jsonData = require('../js/396.json');
}


function parseJSON2()
{
	var request = new XMLHttpRequest();
   request.open("GET", "../js/396.json", false);
   request.send(null)
   var my_JSON_object = JSON.parse(request.responseText);
   alert (my_JSON_object.result[0]);
}
