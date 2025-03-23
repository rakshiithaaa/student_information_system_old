document.getElementById('loginForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form submission
  
    // Get input values
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
  
    // Simple validation (replace with actual backend validation)
    if (username === "admin" && password === "1234") {
      window.location.href = "/dashboard"; // Redirect to dashboard
    } else {
      alert("Invalid Username or Password, Check Again");
    }
  });
  
  // Handle Edit and Delete Buttons
  document.getElementById('editButton').addEventListener('click', function () {
    const selectedStudent = document.querySelector('input[name="student"]:checked');
    if (selectedStudent) {
        window.location.href = `/edit_student/${selectedStudent.value}`;
    } else {
        alert("Please select a student to edit.");
    }
});

document.getElementById('deleteButton').addEventListener('click', function () {
  const selectedStudent = document.querySelector('input[name="student"]:checked');
  if (selectedStudent) {
      if (confirm("Are you sure you want to delete this student?")) {
          window.location.href = `/delete_student/${selectedStudent.value}`;
      }
  } else {
      alert("Please select a student to delete.");
  }
});
