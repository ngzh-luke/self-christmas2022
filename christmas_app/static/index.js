// Helper functions

// Welcome popup
function hit() {
  Swal.fire({
    title: "Surprise Present is ready for you!",
    html: "Aren't you excited?",
    icon: "info",
    confirmButtonText: '<i class="fa fa-thumbs-up"></i> Exciting!',
    confirmButtonAriaLabel: "Thumbs up, sure!",
  }).then(() => {
    window.location.assign("/login");
  });
}

// Pre-defined account checker
async function theChecker(loc = "") {
  if (loc == "login-integrated") {
    var htmlCode =
      '<form class="form" action="/check/" method="POST"> ' +
      "<h3>Check pre-defined account</h3>" +
      '<input class="col-8 my-2" type="search" placeholder="Search Here" aria-label="Search" autocapitalize="characters" name="account_" id="account_"/><br>' +
      // '<p>(Ex. If your name is John Blue, type in "John" or "JOHN" or "john")</p>' +
      '<input type="submit" value="Search Now!" class="btn-lg" />' +
      "</form>";
  } else {
    var htmlCode =
      '<form class="form" action="/check-account/by-first-name/" method="POST"> ' +
      "<h3>Check pre-defined account</h3>" +
      '<input class="col-8 my-2" type="search" placeholder="Search Here" aria-label="Search" autocapitalize="characters" name="account_" id="account_"/><br>' +
      // '<p>(Ex. If your name is John Blue, type in "John" or "JOHN" or "john")</p>' +
      '<input type="submit" value="Search Now!" class="btn-lg" />' +
      "</form>";
  }
  Swal.fire({
    title: "Submit your First Name",
    html: htmlCode,
    showCancelButton: true,
    showConfirmButton: false,
    showLoaderOnConfirm: true,

    allowOutsideClick: () => !Swal.isLoading(),
  });
}

// Account password changer
async function theChanger(alias = "") {
  if (alias != "") {
    var htmlCode =
      '<form class="form" action="/' +
      alias +
      '/account-management/change-password/" method="POST"> ' +
      "<h3 style='color:red;' >[]</h3>" +
      '<input class="col-8 my-2" type="password" placeholder="Current Password" aria-label="Search" autocapitalize="characters" name="account_" id="account_"/><br>' +
      '<input type="submit" value="Confirm Changes" class="btn-lg" />' +
      "</form>";
  } else {
    var htmlCode =
      "You can't change account password when you didn't login to the system";
  }
  Swal.fire({
    title: "Account Password Changer",
    html: htmlCode,
    showCancelButton: true,
    showConfirmButton: false,
    showLoaderOnConfirm: true,

    allowOutsideClick: () => !Swal.isLoading(),
  });
}
