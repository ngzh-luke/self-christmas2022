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

async function theChecker() {
  Swal.fire({
    title: "Submit your First Name",
    html:
      '<form class="form-control py-2 my-2 border border-3 border-info" action="/check-account/by-first-name/" method="POST"> ' +
      "<h4>Check pre-defined account</h4>" +
      '<input class="form-control me-2" type="search" placeholder="Search Here" aria-label="Search" autocapitalize="characters" name="account_" id="account_"/>' +
      '<p>Type in your first name (Ex. If your name is John Blue, type in "John" or "JOHN" or "john")</p>' +
      // <div class="my-2">
      '<input type="submit" value="Search!" class="btn-lg" />' +
      // </div>
      "</form>",
    showCancelButton: true,
    showConfirmButton: false,
    showLoaderOnConfirm: true,

    allowOutsideClick: () => !Swal.isLoading(),
  });
}
