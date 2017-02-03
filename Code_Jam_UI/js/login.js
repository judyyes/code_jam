
function initial() {
	$("#student").on("click", goStudent);
	$("#teacher").on("click", goTeacher);
	
}

function goStudent() {
	window.location.href="page/student_login.html";
}

function goTeacher() {
	window.location.href="page/teacher_login.html";
}

