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

async function theChecker(loc = "") {
  if (loc == "login-integrated") {
    var htmlCode =
      '<form class="form-control py-2 my-2 border border-3 border-info" action="/check/" method="POST"> ' +
      "<h4>Check pre-defined account</h4>" +
      '<input class="form-control me-2" type="search" placeholder="Search Here" aria-label="Search" autocapitalize="characters" name="account_" id="account_"/>' +
      '<p>(Ex. If your name is John Blue, type in "John" or "JOHN" or "john")</p>' +
      '<input type="submit" value="Search!" class="btn-lg" />' +
      "</form>";
  } else {
    var htmlCode =
      '<form class="form-control py-2 my-2 border border-3 border-info" action="/check-account/by-first-name/" method="POST"> ' +
      "<h4>Check pre-defined account</h4>" +
      '<input class="form-control me-2" type="search" placeholder="Search Here" aria-label="Search" autocapitalize="characters" name="account_" id="account_"/>' +
      '<p>(Ex. If your name is John Blue, type in "John" or "JOHN" or "john")</p>' +
      '<input type="submit" value="Search!" class="btn-lg" />' +
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
