// $(delete_button).on('click', '.confirm-delete', function(){
//         return confirm('Are you sure you want to delete this?');


let delete_button = document.getElementById("confirm-delete");

delete_button.addEventListener("click", confirmAction());


function confirmAction() {
    let confirmAction = confirm("Are you sure to execute this action?");
    if (confirmAction) {
      alert("Action successfully executed");
    } else {
      alert("Action canceled");
    }
  }

  if (confirmAction) {
    // if true
    alert("Action successfully executed");
  } else {
    // if false
    alert("Action canceled");
  }