function hit() {
    Swal.fire({
    title: "Surprise Present is ready for you!",
    html: "Aren't you excited?",
    icon: "info",
    confirmButtonText: '<i class="fa fa-thumbs-up"></i> Exciting!',
    confirmButtonAriaLabel: "Thumbs up, sure!",
  }).then(() => {
    window.location.assign("/login");
  });}