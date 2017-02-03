var teacherID;
var jsonData

function initialTeacher()
{
	parseJSON();
    //$("#stu_login").on("click", getStudentID);
}

function getTeacherID()
{
	//studentID = $("#stu_id").val();
	//window.location.href="page/student_display.html";
	//alert(studentID);
}

function parseJSON()
{
	 jsonData = require('./396.json'); 
	 alert(jsonData);
}
